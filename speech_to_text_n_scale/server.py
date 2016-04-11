# -*- coding: utf-8 -*-

import os
import time
import wave
import i2c_motor_driver
from Queue import Queue
from threading import Thread

from bottle import route, run, request, static_file, view

from recognition import recognize
#from docomo_voice_recognition import recognize
from textlogger import add_log, get_logs

upload_dir = 'upload_dir/'


@route('/', method='GET')
@view('logs')
def logs():
    return dict(logs=get_logs())


@route('/wave', method='POST')
def do_upload():
    wav_file = request.files.get('file')
    name, ext = os.path.splitext(wav_file.filename)
    # Listnr uploads audio data as “sample.r16”
    if ext not in ('.r16'):
        return 'File extension not allowed.'

    if not os.path.exists(upload_dir):
        os.mkdir(upload_dir)

    file_name = str(int(time.time())) + '.wav'
    file_path = os.path.join(upload_dir, file_name)
    write_wave(file_path, wav_file.file.read())
    q.put({
        "file_path": file_path,
        "file_name": file_name
    })
    return 'OK'


@route('/files/<filename:re:.+\.wav>')
def wav_files(filename):
    return static_file(filename, root=upload_dir)


@route('/img/<filename:re:.+\.png>')
def img_files(filename):
    return static_file(filename, root='img/')


@route('/css/<filename:re:.+\.css>')
def css_files(filename):
    return static_file(filename, root='css/')


@route('/js/<filename:re:.+\.js>')
def js_files(filename):
    return static_file(filename, root='js/')


def write_wave(file_path, wave_bin):
    wave_file = wave.open(file_path, 'wb')
    # Mono, 16bit, 16kHz
    wave_file.setparams((1, 2, 16000, 0, 'NONE', 'not compressed'))
    wave_file.writeframes(wave_bin)
    wave_file.close()

start_words = (u"進", u"勧", u"スタート", u"発車", u"出発", u"start")
stop_words = (u"止", u"ストップ", u"停", u"stop")
reverse_words = (u"バック", u"リバース", u"リターン", u"折り返し", u"reverse")
accelerate_words = (u"加速", u"アップ", u"アクセル", u"up")
decelerate_words = (u"減速", u"原則", u"ダウン", u"ブレーキ", u"down", u"brake")

def worker():
    is_normal = True
    while True:
        item = q.get()
        time.sleep(1)

        text = recognize(item["file_path"], language="ja-JP")
        add_log(item["file_name"], text)
        if any(x in text for x in start_words):
            i2c_motor_driver.start()
            is_normal = True
        elif any(x in text for x in stop_words):
            i2c_motor_driver.stop()
        elif any(x in text for x in reverse_words):
            if is_normal:
                i2c_motor_driver.reverse()
            else:
                i2c_motor_driver.start()
            is_normal = not is_normal
        elif any(x in text for x in accelerate_words):
            i2c_motor_driver.accelerate()
        elif any(x in text for x in decelerate_words):
            i2c_motor_driver.decelerate()
        q.task_done()


q = Queue()
t = Thread(target=worker)
t.daemon = True
t.start()

run(host='0.0.0.0', port=8080, debug=False, reloader=False)

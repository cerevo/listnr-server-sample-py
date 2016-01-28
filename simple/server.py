# -*- coding: utf-8 -*-

import os, wave, time
from bottle import route, run, request, static_file, view

upload_dir = 'upload_dir/'


@route('/', method='GET')
@view('files')
def file_list():
    files_info = []
    if os.path.exists(upload_dir):
        files = os.listdir(upload_dir)
        files.sort(reverse=True)
        files_info = [{
                          "url": 'files/' + filename,
                          "name": filename,
                          "time": int(os.path.getmtime(os.path.join(upload_dir, filename)))
                      } for filename in files if os.path.splitext(filename)[1] == '.wav']
    return dict(files=files_info)


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


run(host='0.0.0.0', port=8080, debug=True, reloader=True)

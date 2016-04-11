# -*- coding: utf-8 -*-

import speech_recognition as sr
from ConfigParser import SafeConfigParser

config = SafeConfigParser()
config.read('config.ini')

def recognize(file_path, language="en-US"):
    r = sr.Recognizer()
    with sr.WavFile(file_path) as source:
        audio = r.record(source)

    # recognize speech using Google Speech Recognition
    ret = ""
    try:
        # Please use your username and password of https://console.ng.bluemix.net/catalog/services/speech-to-text/ .
        ibm_username = config.get("ibm_bluemix_speech_to_text", "username")
        ibm_password = config.get("ibm_bluemix_speech_to_text", "password")
        ret = r.recognize_ibm(audio, username=ibm_username, password=ibm_password, language=language)
        print("IBM Speech Recognition thinks you said " + ret)
    except sr.UnknownValueError:
        print("IBM Speech Recognition could not understand audio")
    except sr.RequestError as e:
        print("Could not request results from IBM Speech Recognition service; {0}".format(e))

    return ret

# -*- coding: utf-8 -*-

# reference
# http://stackoverflow.com/questions/680305/using-multipartposthandler-to-post-form-data-with-python

from poster.encode import multipart_encode
from poster.streaminghttp import register_openers
import urllib2
import json
import sys
from ConfigParser import SafeConfigParser

config = SafeConfigParser()
config.read('config.ini')


def recognize(wav_filename, language=None):
    # Register the streaming http handlers with urllib2
    register_openers()

    datagen, headers = multipart_encode({"a": open(wav_filename)})

    # Create the Request object
    apikey = config.get("docomo_developer", "apikey")
    apiurl = "https://api.apigw.smt.docomo.ne.jp/amiVoice/v1/recognize?APIKEY={0}".format(apikey)
    request = urllib2.Request(apiurl, datagen, headers)
    # Actually do the request, and get the response
    result = urllib2.urlopen(request).read()
    # print(result.decode('unicode_escape'))

    result_json = json.loads(result)
    print(result_json["text"])
    return result_json["text"]


if __name__ == '__main__':
    argvs = sys.argv
    argc = len(argvs)
    if (argc != 2):
        print 'Usage: # python %s wav_filename' % argvs[0]
        quit()
    wav_filename = argvs[1]
    recognize(wav_filename)

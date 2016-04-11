# -*- coding: utf-8 -*-

import sqlite3
import time

sql = u"INSERT INTO textlogs (filename, text, created_at) values (?, ?, ?)"
db_file = './textlog.sqlite3'

def add_log(filename, text):
    conn = sqlite3.connect(db_file)
    cur = conn.cursor()
    cur.execute(sql, (filename, text, long(time.time())))
    conn.commit()
    cur.close()


def get_logs():
    conn = sqlite3.connect(db_file)
    cur = conn.cursor()
    logs = cur.execute(u"SELECT filename, text, created_at FROM textlogs ORDER BY created_at DESC")
    ret = [{
               "filename": row[0],
               "text": row[1],
               "created_at": row[2]
           } for row in logs]
    cur.close()
    return ret

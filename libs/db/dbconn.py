# 데이터베이스 연결 파일

import sqlite3

def getconn():
    conn = sqlite3.connect("c:/pydb/mydb.db")
    return conn

# member db에 연결하는 함수 - getconn()


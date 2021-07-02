from libs.db.dbconn import getconn

def drop_table():
    conn = getconn()
    cur = conn.cursor()
    # 테이블 삭제 - SQL DDL(데이터 정의어)
    sql = "drop table member"
    cur.execute(sql)
    conn.commit()
    conn.close()

if __name__ == "__main__":
    drop_table()
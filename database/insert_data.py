# 자료를 삽입하는 코드

from libs.db.dbconn import getconn

def insert_data():
    conn = getconn()
    cur = conn.cursor()
    # 자료 추가 - SQL
    cur.execute("insert into member values ('황진이', 20)")
    cur.execute("insert into member values ('성춘향', 30)")
    conn.commit()
    conn.close()

if __name__ == "__main__":
    insert_data()
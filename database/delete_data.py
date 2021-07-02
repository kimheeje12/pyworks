# 특정자료 삭제
from libs.db.dbconn import getconn

def delete_data():
    conn = getconn()
    cur = conn.cursor()
    sql = "delete from member where name = '이순신'"
    cur.execute(sql)

    conn.commit()
    conn.close()

if __name__ == "__main__":
    delete_data()
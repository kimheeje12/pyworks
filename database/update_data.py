# 자료 내용 변경

from libs.db.dbconn import getconn

def update_data():
    conn = getconn()
    cur = conn.cursor()
    sql = "update member set name='이몽룡' where mem_num = 104"
    cur.execute(sql)

    conn.commit()
    conn.close()

if __name__=="__main__":
    update_data()
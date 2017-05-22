import MySQLdb


class db:
    def __init__(self):
        self.conn = MySQLdb.connect(
            host='localhost',
            port=3306,
            user='root',
            passwd='jackjin820',
            db='image',
        )
        self.cur = self.conn.cursor()

    def insertNew(self, path, hamingWay, hamingAverage, hamingChange, hamingFeel, ):
        sql = "insert into imageWay (path,hamingWay,hamingAverage,hamingChange,hamingFeel) values ('" + path + "','" + hamingWay + "','" + hamingAverage + "','" + hamingChange + "','" + hamingFeel + "');"
        try:
            self.cur.execute(sql)
            self.conn.commit()
        except Exception as e:
            print e
            self.conn.rollback()
        self.cur.close()
        self.conn.close()

    def select(self, type):
        sql = "select id,+" + type + " from imageWay;"
        self.cur.execute(sql)
        rs = self.cur.fetchall()
        self.cur.close()
        self.conn.close()
        return rs

    def select_path(self):
        sql = 'select path from imageWay;'
        self.cur.execute(sql)
        rs = self.cur.fetchall()
        self.cur.close()
        self.conn.close()
        return rs

    def getPath(self, id):
        sql = "select path from imageWay where id = " + str(id) + ";"
        self.cur.execute(sql)
        rs = self.cur.fetchone()
        self.cur.close()
        self.conn.close()
        return rs[0]


if __name__ == "__main__":
    aa = db().select_path()
    print aa[0]

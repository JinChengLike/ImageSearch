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
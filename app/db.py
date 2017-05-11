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

    def insertNew(self, haming, path, way):
        return 0

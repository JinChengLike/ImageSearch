import MySQLdb

conn = MySQLdb.connect(
    host="127.0.0.1",
    port=3306,
    user="root",
    passwd="jackjin820",
    db="todo",
    charset='utf8'
)

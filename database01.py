import pymysql

db = pymysql.connect(host= 'local host',
                        user = 'root',
                        password = 'admin',
                        database = 'demo1',
                        cursorclass=pymysql.cursors.DistCursor)

cursor=db.cursor()
cursor.execute("SELECT VERSION()")

data = cursor.fetchone()
print("Data`base version : %s " % data)
import pymysql
db = pymysql.connect(host= 'localhost',
                        user = 'root',
                        password = 'admin',
                        database = 'demo1',
                        cursorclass=pymysql.cursors.DictCursor)

cursor = db.cursor()
query = "CREATE TABLE bankaccount1 (fname varchar(50),lname varchar(50),accno varchar(10),phoneno varchar(11),city varchar(20))"

try:
    cursor.execute(query)
    db.commit()
except:
    db.rollback()
db.close()

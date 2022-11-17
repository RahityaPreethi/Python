import pymysql
db = pymysql.connect(host= 'localhost',
                        password = 'admin',
                        user = 'root',
                        database = 'demo1',
                        cursorclass=pymysql.cursors.DictCursor)

cursor = db.cursor()
query = "DELETE FROM bankaccount1 WHERE city='Noida'"

try:
    cursor.execute(query)
    db.commit()
except:
    db.rollback()
db.close()

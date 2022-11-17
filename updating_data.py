import pymysql
db = pymysql.connect(host= 'localhost',
                        user = 'root',
                        password = 'admin',
                        database = 'demo1',
                        cursorclass=pymysql.cursors.DictCursor)

cursor = db.cursor()
query = 'UPDATE BANKACCOUNT1 SET phoneno = "9765432108" where fname = "Rupa"'


try:
    cursor.execute(query)
    db.commit()
except:
    db.rollback()
db.close()

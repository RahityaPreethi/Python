import pymysql
db = pymysql.connect(host= 'localhost',
                        user = 'root',
                        password = 'admin',
                        database = 'demo1',
                        cursorclass=pymysql.cursors.DictCursor)

cursor = db.cursor()
#query = 'INSERT INTO bankaccount1 VALUES("John","Wilkes","12034567",9988776655,"Hyderabad")'
query = 'INSERT INTO bankaccount1 VALUES("Abhika","Nandhigama","6543217","8765432190","Warangal")'

try:
    cursor.execute(query)
    db.commit()
except:
    db.rollback()
db.close()

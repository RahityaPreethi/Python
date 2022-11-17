import pymysql
connection = pymysql.connect(host= 'localhost',
                        user = 'root',
                        password = 'admin',
                        database = 'demo1',
                        cursorclass=pymysql.cursors.DictCursor)

with connection.cursor() as cursor:
    sql = "SELECT * FROM bankaccount1"
    cursor.execute(sql)
    result = cursor.fetchall()
    print(result)

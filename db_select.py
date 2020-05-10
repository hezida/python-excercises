import pymysql.cursors

# Connect to the database
with pymysql.connect(host='localhost',
                             user='root',
                             password='root',
                             db='test') as cursor:
        sql = "SELECT * FROM data"
        cursor.execute(sql)
        result = cursor.fetchall()
        print(result)

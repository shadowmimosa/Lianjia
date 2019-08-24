import pymysql
connection = pymysql.connect(host='localhost',
                             user='root',
                             password='root',
                             db='lianjia',
                             charset='utf8mb4',
                             cursorclass=pymysql.cursors.DictCursor)
print(connection.query('select * from users'))

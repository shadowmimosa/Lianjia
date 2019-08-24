import pymysql.cursors

# Connect to the database
connection = pymysql.connect(host='localhost',
                             user='root',
                             password='root',
                             db='lianjia',
                             cursorclass=pymysql.cursors.DictCursor)
cursor = connection.cursor()
effect_row = cursor.execute('select * from users')
# 获取剩余结果所有数据
result = cursor.fetchall()
print(result)

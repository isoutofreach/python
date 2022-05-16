import pymysql

db = pymysql.connect(
    host='localhost',
    user='root',
    password='123456',
    database="s32",
    port=3306,
    charset='utf8'
)

cursor = db.cursor()

exe = cursor.execute("show databases")
print(exe)

result = cursor.fetchall()

print(result)

db.commit()
cursor.close()
db.close()
import mysql.connector

# 连接 MySQL
conn = mysql.connector.connect(
    host="130.209.157.51",
    user="zhongyuezhao",
    password="123456",
    database="mydatabase"  # 确保替换为正确的数据库名
)

cursor = conn.cursor()
cursor.execute("SHOW TABLES;")  # 显示数据库中的所有表

print("📌 数据库中的表:")
for table in cursor.fetchall():
    print(table)

cursor.close()
conn.close()
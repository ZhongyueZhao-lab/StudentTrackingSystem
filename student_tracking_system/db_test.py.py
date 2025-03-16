import mysql.connector

# Connecting to MySQL
conn = mysql.connector.connect(
    host="130.209.157.51",
    user="zhongyuezhao",
    password="123456",
    database="mydatabase"  # Make sure to replace the database name with the correct one
)

cursor = conn.cursor()
cursor.execute("SHOW TABLES;")  # 显Show all tables in the database

print("Tables in the database:")
for table in cursor.fetchall():
    print(table)

cursor.close()
conn.close()

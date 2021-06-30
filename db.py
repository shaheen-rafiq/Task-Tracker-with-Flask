import psycopg2

conn=psycopg2.connect(
    host="localhost",
    database="todo_app",
    user="postgres",
    password="cheesecake222"
)
cur=conn.cursor()
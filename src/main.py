import psycopg2
import pandas as pd


#conn = psycopg2.connect("dbname=excel user=vijay password=vijay123")

conn = psycopg2.connect(
    host="127.0.0.1",
    database="crm",
    user="vijay",
    password="vijay123")

print("database connected successfully")

cur = conn.cursor()

cur.execute("""CREATE TABLE excel(REFNO INT PRIMARY KEY NOT NULL,
                       col1 INT NOT NULL,
                       col2 INT NOT NULL,
                       col3 TEXT NOT NULL,
                       col4 TEXT NOT NULL,
                       col5 TEXT NOT NULL,
                       col6 INT NOT NULL,
                       col7 TEXT NOT NULL) """)

conn.commit()
print("table created")



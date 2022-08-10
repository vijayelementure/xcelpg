import psycopg2
import pandas as pd

x = pd.read_excel('dumLeads.xlsx')
va = x.columns[0]
vb = x.columns[1]
vc = x.columns[2]
vd = x.columns[3]
ve = x.columns[4]
vf = x.columns[5]
vg = x.columns[6]

print(va)
print(vb)
print(vc)
print(vd)
print(ve)
print(vf)
print(vg)


#conn = psycopg2.connect("dbname=excel user=vijay password=vijay123")

conn = psycopg2.connect(
    host="127.0.0.1",
    database="crm",
    user="vijay",
    password="vijay123")

print("database connected successfully")

query = f"""CREATE TABLE excel(REFNO INT PRIMARY KEY NOT NULL,
                {va}  INT NOT NULL,
                {vb}  INT NOT NULL,
                {vc}  TEXT NOT NULL,
                {vd}  TEXT NOT NULL,
                {ve}  TEXT NOT NULL,
                {vf}  SERIAL NOT NULL,
                {vg}  TEXT NOT NULL)  """
                
print(query)

cur = conn.cursor()
cur.execute(query)

conn.commit()
print("table created")



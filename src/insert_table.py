import psycopg2
import pandas as pd


x = pd.read_excel('dumLeads.xlsx')

#conn = psycopg2.connect("dbname=excel user=vijay password=vijay123")

conn = psycopg2.connect(
    host="127.0.0.1",
    database="crm1",
    user="vijay",
    password="vijay123")


print("database connected successfully")

x = pd.read_excel('dumLeads.xlsx')
print(x)
va = x.columns[0]
vb = x.columns[1]
vc = x.columns[2]
vd = x.columns[3]
ve = x.columns[4]
vf = x.columns[5]
vg = x.columns[6]



query = f"""INSERT INTO excel(REFNO,{va},{vb},{vc},{vd},{ve},{vf},{vg})
                VALUES(1,1,12-2-1998,'digital','website','vijay',9741113585,'vijay@gmail.com')"""





cur = conn.cursor()

cur.execute(query)

conn.commit()
           
           
           
           
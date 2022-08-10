import pandas as pd
import openpyxl
import psycopg2


conn = psycopg2.connect(
    host="127.0.0.1",
    database="crm1",
    user="vijay",
    password="vijay123")




path = "vijay.xlsx"
file = openpyxl.load_workbook(path)
sheet = file.active

for cell in sheet.iter_rows(min_row=2, max_row=2, min_col=1, max_col=3,values_only=True):
    print(cell)

va = cell[0]
print(va)
vb = cell[1]
print(vb)
vc = cell[2]
print(vc)

query = f"""INSERT INTO excel(REFNO,id,name,role)
                VALUES(0,{va},{vb},{vc})"""



cur = conn.cursor()

cur.execute(query)
conn.commit()

print("data inserted")
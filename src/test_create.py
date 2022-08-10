import openpyxl
import psycopg2

conn = psycopg2.connect(
    host="127.0.0.1",
    database="crm1",
    user="vijay",
    password="vijay123")

print("database connected successfully")

path = "vijay.xlsx"
file = openpyxl.load_workbook(path)
sheet = file.active

for cell in sheet.iter_rows(min_row=1, max_row=1, min_col=1, max_col=3,values_only=True):
    print(cell)
    
va = cell[0]
print(va)
vb = cell[1]
print(vb)
vc = cell[2]
print(vc)

query = f"""CREATE TABLE excel(REFNO INT PRIMARY KEY NOT NULL,
                {va}  INT NOT NULL,
                {vb}  TEXT NOT NULL,
                {vc}  TEXT NOT NULL)  """
                
                
cur = conn.cursor()
cur.execute(query)

conn.commit()

print("table created")








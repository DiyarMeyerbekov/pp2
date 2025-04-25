import psycopg2
import csv

#1
def find(cur,pattern):
    cur.execute("SELECT * FROM phonebook1 WHERE name = %s OR surname = %s OR phone=%s;", (pattern,pattern,pattern))
    result=cur.fetchall()
    if result:
        for row in result:
            print(row)
    else:
        print("None")
#2
def add_or_update(cur,nme,surnme,new_phone):
    cur.execute(""" 
        SELECT EXISTS (
                SELECT 1 FROM phonebook1 WHERE name=%s AND surname=%s
                )
""",(nme,surnme))
    exist=cur.fetchone()[0]

    if exist:
        cur.execute("UPDATE phonebook1 SET phone=%s WHERE name=%s AND surname=%s;", (new_phone,nme,surnme))
        print("phone of contact updated")
    else:
        cur.execute("INSERT INTO phonebook1 (name,surname,phone) VALUES(%s,%s,%s);",(nme,surnme,new_phone))
        print("contact added ")
#3
def many_numbers(cur,naame,suurname,pone):
    cur.execute("INSERT INTO phonebook1 (name,surname,phone) VALUES(%s,%s,%s);",(naame,suurname,pone))
#4
def lim_query(cur,limit,offset):
    cur.execute("SELECT * FROM phonebook1 ORDER BY id LIMIT %s OFFSET %s;",(limit,offset))
    result=cur.fetchall()
    for row in result:
        print(row)
#5
def delete(cur,value,surnm=None):
    cur.execute("DELETE FROM phonebook1 WHERE name=%s OR surname=%s OR phone=%s;",(value,surnm,value))
    print("contact was deleted")
try:
    conn = psycopg2.connect(
        dbname="suppliers",
        user="postgres",
        password="110906",
        host="localhost",
        port="5432"
    )
    cur = conn.cursor()

    # Создание таблицы
    cur.execute("""
        CREATE TABLE IF NOT EXISTS phonebook1 (
            id SERIAL PRIMARY KEY,
            name TEXT NOT NULL,
            surname TEXT NOT NULL,
            phone TEXT NOT NULL
        );
    """)
    conn.commit()

    print("to add or update phone of existing contact write add")
    print("to find write find")
    print("to add many contacts write toomany ")
    print("to get limitted query write lim ")
    print("write delete")

    choise=input("What do u want brou ")
    bad_list=[]

    if choise=='add':
        nam=input("Write name: ")
        sur=input("Write surname: ")
        ph=input("phone ")
        add_or_update(cur,nam,sur,ph)
        conn.commit()
    
    if choise=='find':
        value=input("Write phone or name,surname ")
        find(cur,value)
        conn.commit()

    if choise=='toomany':
        print("to stop write stop in name")
        run=True
        while run:
            name1=input("name:")
            if name1=='stop':
                run=False
                print("all data saved")
                print(bad_list)
                break
            sur1=input("surname: ")
            ph1=input("phone: ")
            if len(ph1)==11:
                many_numbers(cur,name1,sur1,ph1)
                conn.commit()
            else:
                bad_list.append((name1,sur1,ph1))

    if choise=='lim':
        lim=int(input("Write limit: "))
        offset=int(input("Write offset: "))
        lim_query(cur,lim,offset)
        conn.commit()
    
    if choise=='delete':
        value=input("Write name or surname or phone ")
        surnm=input("Write surname as u wish or none") or None
        delete(cur,value,surnm)
        conn.commit()
    
    cur.execute("SELECT name,surname,phone FROM phonebook1;")
    rows = cur.fetchall()
    with open('phonebook1.csv', mode='w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(['name','surname','phone']) 
        writer.writerows(rows)
except Exception as e:
    print("Eror:", e)

cur.close()
conn.close()
#print("Файл сохранён сюда:", os.path.abspath('phonebook1.csv'))
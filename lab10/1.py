import csv
import psycopg2

DB_NAME = "suppliers"
DB_USER = "postgres"
DB_PASSWORD = "110906"
DB_HOST = "localhost"
DB_PORT = "5432"

CSV_FILE = "phonebook.csv"

def create_table(cursor):
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS phonebook (
            id SERIAL PRIMARY KEY,
            name VARCHAR(100),
            phone VARCHAR(100)
        );
    """)

def import_csv(cursor, filename):
    with open(filename, newline='', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            cursor.execute("""
                INSERT INTO phonebook (name,phone)
                VALUES (%s, %s)
            """, (row['name'], row['phone']))

def add_user(cursor, name, phone):
    cursor.execute("""
        INSERT INTO phonebook (name, phone)
        VALUES (%s, %s)
    """, (name, phone))


def update_user(cursor, old_phone, new_name=None, new_phone=None):
    if new_name:
        cursor.execute("""
            UPDATE phonebook SET name = %s WHERE phone = %s
        """, (new_name, old_phone))
    if new_phone:
        cursor.execute("""
            UPDATE phonebook SET phone = %s WHERE phone = %s
        """, (new_phone, old_phone))

def query_users(cursor, name=None, phone=None):
    if name:
        cursor.execute("SELECT * FROM phonebook WHERE name = %s", (name,))
    elif phone:
        cursor.execute("SELECT * FROM phonebook WHERE phone = %s", (phone,))
    else:
        cursor.execute("SELECT * FROM phonebook")
    
    rows = cursor.fetchall()
    for row in rows:
        print(row)

def delete_user(cursor, name=None, phone=None):
    if name:
        cursor.execute("DELETE FROM phonebook WHERE name = %s", (name,))
    elif phone:
        cursor.execute("DELETE FROM phonebook WHERE phone = %s", (phone,))

def main():
    try:
        conn = psycopg2.connect(
            dbname=DB_NAME,
            user=DB_USER,
            password=DB_PASSWORD,
            host=DB_HOST,
            port=DB_PORT
        )
        cur = conn.cursor()
        create_table(cur)
        import_csv(cur, CSV_FILE)

        add_user(cur, name="Amina", phone="67")
        query_users(cur, name="di")
        conn.commit()
        print("Succesful")
    except Exception as e:
        print(f"Error: {e}")
    finally:
        if conn:
            cur.close()
            conn.close()

if __name__ == "__main__":
    main()



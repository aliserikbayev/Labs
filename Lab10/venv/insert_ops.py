import csv
from db import connect

def insert_from_console():
    first_name = input("Enter name: ")
    phone = input("Enter phone: ")
    conn = connect()
    cur = conn.cursor()
    try:
        cur.execute("INSERT INTO phonebook (first_name, phone) VALUES (%s, %s)", (first_name, phone))
        conn.commit()
        print("Data inserted successfully!")
    except Exception as e:
        print(f"Error: {e}")
        conn.rollback()
    conn.close()

def insert_from_csv(file_path):
    conn = connect()
    cur = conn.cursor()
    with open(file_path, 'r') as f:
        reader = csv.reader(f)
        next(reader)
        for row in reader:
            try:
                cur.execute("INSERT INTO phonebook (first_name, phone) VALUES (%s, %s)", (row[0], row[1]))
            except:
                conn.rollback()
    conn.commit()
    conn.close()
    print("CSV Data inserted successfully!")
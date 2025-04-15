import psycopg2

def connect():
    return psycopg2.connect(
        dbname="phonebook_db", user="koltykwaw", password="21271113ali", host="localhost", port="5432"
    )

def create_table():
    conn = connect()
    cur = conn.cursor()
    cur.execute("""
        CREATE TABLE IF NOT EXISTS phonebook (
            id SERIAL PRIMARY KEY,
            first_name VARCHAR(50) NOT NULL,
            phone VARCHAR(15) UNIQUE NOT NULL
        )
    """)
    conn.commit()
    conn.close()
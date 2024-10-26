import mysql.connector
from mysql.connector import Error

def create_connection():
    try:
        connection = mysql.connector.connect(
            host='localhost',
            user='root',
            password='',
            database='rule_engine'
        )
        return connection
    except Error as e:
        print("Error connecting to MySQL:", e)

def create_table():
    connection = create_connection()
    cursor = connection.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS rules (
                        id INT AUTO_INCREMENT PRIMARY KEY,
                        rule_string TEXT NOT NULL,
                        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
                    )''')
    connection.commit()
    cursor.close()
    connection.close()

if __name__ == "__main__":
    create_table()

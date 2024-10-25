import mysql.connector
from dotenv import load_dotenv
import os


load_dotenv()
db_password = os.environ["MYSQL_ROOT_PASSWORD"]


def connect_to_db():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password=db_password,
        database="clinic"
    )


def get_table_structure(cursor, table_name):
    cursor.execute(f"DESCRIBE {table_name};")
    structure = cursor.fetchall()
    print(f"\nСтруктура таблиці {table_name}:")
    print(f"{'Field':<30} {'Type':<20} {'Null':<10} {'Key':<10} {'Default':<15} {'Extra':<15}")
    print('-' * 100)
    for row in structure:
        field = row[0] if row[0] is not None else "NULL"
        type_ = row[1] if row[1] is not None else "NULL"
        null = row[2] if row[2] is not None else "NULL"
        key = row[3] if row[3] is not None else "NULL"
        default = row[4] if row[4] is not None else "NULL"
        extra = row[5] if row[5] is not None else "NULL"
        print(f"{field:<30} {type_:<20} {null:<10} {key:<10} {default:<15} {extra:<15}")

def get_table_data(cursor, table_name):
    cursor.execute(f"SELECT * FROM {table_name};")
    data = cursor.fetchall()
    headers = [i[0] for i in cursor.description]
    print(f"\nДані з таблиці {table_name}:")
    print(" | ".join(f"{header:<20}" for header in headers))
    print('-' * (len(headers) * 20 + (len(headers) - 1) * 3))  # Dynamic width for separators
    for row in data:
        print(" | ".join(f"{str(value):<20}" for value in row))

def execute_query(cursor, query, description):
    cursor.execute(query)
    data = cursor.fetchall()
    headers = [i[0] for i in cursor.description]
    print(f"\n{description}:")
    print(" | ".join(f"{header:<20}" for header in headers))
    print('-' * (len(headers) * 20 + (len(headers) - 1) * 3))
    for row in data:
        print(" | ".join(f"{str(value):<20}" for value in row))




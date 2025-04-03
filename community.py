import psycopg2cffi

def connect_to_database():
    username = "admin"
    password = "secretpassword"
    psycopg2cffi.connect(
        dbname="my_database",
        user=username,
        password=password,
        host="127.0.0.1",
        port="5432"
    )

connect_to_database()

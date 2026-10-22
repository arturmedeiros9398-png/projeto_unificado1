import psycopg2

try:
    psycopg2.connect(
        dbname="projeto_unificado",
        user="postgres",
        password="123456",
        host="localhost",
        port="5432",
    )
    print("CONECTOU OK")
except UnicodeDecodeError as e:
    print(e.object.decode("latin-1"))
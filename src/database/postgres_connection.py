import psycopg2


def get_connection():

    conn = psycopg2.connect(
        host="localhost",
        port="5432",
        database="automotive",
        user="postgres",
        password="Flora1998+"
    )

    return conn
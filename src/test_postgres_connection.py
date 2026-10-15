import psycopg2


try:

    conn = psycopg2.connect(
        host="localhost",
        port="5432",
        database="automotive",
        user="postgres",
        password="xxx"
    )

    print("✅ Verbindung erfolgreich")

    conn.close()

except Exception as e:

    print("❌ Fehler:")
    print(e)
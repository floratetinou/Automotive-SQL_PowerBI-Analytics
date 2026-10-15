import sqlite3


def create_database():
    """
    Erstellt die Automotive-Testdatenbank.
    """

    conn = sqlite3.connect("automotive.db")# connect() erstellt diese Verbindung.

    cursor = conn.cursor() #Der Cursor ist der "Arbeiter", der die SQL-Befehle zur Datenbank bringt.

    # ==========================================
    # Tabelle: vehicles
    # ==========================================
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS vehicles (
        vehicle_id INTEGER PRIMARY KEY AUTOINCREMENT,
        vin TEXT NOT NULL,
        model TEXT NOT NULL,
        sw_version TEXT NOT NULL
    )
    """)

    # ==========================================
    # Tabelle: test_cases
    # ==========================================
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS test_cases (
        testcase_id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        category TEXT NOT NULL
    )
    """)

    # ==========================================
    # Tabelle: test_runs
    # ==========================================
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS test_runs (
        run_id INTEGER PRIMARY KEY AUTOINCREMENT,
        vehicle_id INTEGER NOT NULL,
        testcase_id INTEGER NOT NULL,
        result TEXT NOT NULL,
        test_date DATE NOT NULL,

        FOREIGN KEY (vehicle_id)
            REFERENCES vehicles(vehicle_id),

        FOREIGN KEY (testcase_id)
            REFERENCES test_cases(testcase_id)
    )
    """)

    # ==========================================
    # Tabelle: errors
    # ==========================================
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS errors (
        error_id INTEGER PRIMARY KEY AUTOINCREMENT,
        run_id INTEGER NOT NULL,
        severity TEXT NOT NULL,
        description TEXT NOT NULL,

        FOREIGN KEY (run_id)
            REFERENCES test_runs(run_id)
    )
    """)

    conn.commit() # Speichert alle Änderungen dauerhaft.
    conn.close() #Schließt die Verbindung.

    print("✅ automotive.db wurde erfolgreich erstellt")
    print("✅ Tabellen erzeugt:")
    print("   - vehicles")
    print("   - test_cases")
    print("   - test_runs")
    print("   - errors")


if __name__ == "__main__":
    create_database()# Hier erstellen wir später die Datenbank

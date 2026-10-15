from src.database.postgres_connection import get_connection


def create_database():
    """
    Erstellt die Automotive-Testdatenbank in PostgreSQL.
    """

    conn = get_connection()

    cursor = conn.cursor()

    # ==========================================
    # Tabelle: vehicles
    # ==========================================
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS vehicles (
        vehicle_id SERIAL PRIMARY KEY,
        vin VARCHAR(100) NOT NULL,
        model VARCHAR(100) NOT NULL,
        sw_version VARCHAR(100) NOT NULL
    )
    """)

    # ==========================================
    # Tabelle: test_cases
    # ==========================================
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS test_cases (
        testcase_id SERIAL PRIMARY KEY,
        name VARCHAR(100) NOT NULL,
        category VARCHAR(100) NOT NULL
    )
    """)

    # ==========================================
    # Tabelle: test_runs
    # ==========================================
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS test_runs (
        run_id SERIAL PRIMARY KEY,
        vehicle_id INTEGER NOT NULL,
        testcase_id INTEGER NOT NULL,
        result VARCHAR(20) NOT NULL,
        test_date DATE NOT NULL,

        CONSTRAINT fk_vehicle
            FOREIGN KEY (vehicle_id)
            REFERENCES vehicles(vehicle_id),

        CONSTRAINT fk_testcase
            FOREIGN KEY (testcase_id)
            REFERENCES test_cases(testcase_id)
    )
    """)

    # ==========================================
    # Tabelle: errors
    # ==========================================
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS errors (
        error_id SERIAL PRIMARY KEY,
        run_id INTEGER NOT NULL,
        severity VARCHAR(20) NOT NULL,
        description TEXT NOT NULL,

        CONSTRAINT fk_run
            FOREIGN KEY (run_id)
            REFERENCES test_runs(run_id)
    )
    """)

    conn.commit()

    print(" PostgreSQL Tabellen erfolgreich erstellt")
    print(" Tabellen erzeugt:")
    print("   - vehicles")
    print("   - test_cases")
    print("   - test_runs")
    print("   - errors")

    cursor.close()
    conn.close()


if __name__ == "__main__":
    create_database()
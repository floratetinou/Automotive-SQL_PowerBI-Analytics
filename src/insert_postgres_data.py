from src.database.postgres_connection import (
    get_connection
)


def insert_sample_data():

    conn = get_connection()

    cursor = conn.cursor()

    # =====================================
    # Vehicles
    # =====================================

    vehicles = [
        ("WVW001", "Golf 8", "1.0.0"),
        ("WVW002", "ID.4", "1.2.0"),
        ("WVW003", "Tiguan", "2.0.1")
    ]

    cursor.executemany("""
    INSERT INTO vehicles
    (vin, model, sw_version)

    VALUES (%s, %s, %s)
    """, vehicles)

    # =====================================
    # Test Cases
    # =====================================

    test_cases = [
        ("Lane Assist", "ADAS"),
        ("Emergency Braking", "ADAS"),
        ("Traffic Sign Detection", "Vision")
    ]

    cursor.executemany("""
    INSERT INTO test_cases
    (name, category)

    VALUES (%s, %s)
    """, test_cases)

    # =====================================
    # Test Runs
    # =====================================

    test_runs = [
        (1, 1, "PASSED", "2026-10-15"),
        (1, 2, "FAILED", "2026-10-15"),
        (2, 1, "PASSED", "2026-10-15"),
        (3, 3, "FAILED", "2026-10-15")
    ]

    cursor.executemany("""
    INSERT INTO test_runs
    (
        vehicle_id,
        testcase_id,
        result,
        test_date
    )

    VALUES (%s, %s, %s, %s)
    """, test_runs)

    # =====================================
    # Errors
    # =====================================

    errors = [
        (
            2,
            "HIGH",
            "Emergency braking response timeout"
        ),
        (
            4,
            "MEDIUM",
            "Traffic sign classification error"
        )
    ]

    cursor.executemany("""
    INSERT INTO errors
    (
        run_id,
        severity,
        description
    )

    VALUES (%s, %s, %s)
    """, errors)

    conn.commit()

    print("✅ Testdaten eingefügt")

    cursor.close()
    conn.close()


if __name__ == "__main__":

    insert_sample_data()
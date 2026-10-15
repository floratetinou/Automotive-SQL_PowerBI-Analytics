import sqlite3

conn = sqlite3.connect("automotive.db")

cursor = conn.cursor()

# Fahrzeuge
vehicles = [
    ("WVW001", "Golf 8", "1.0.0"),
    ("WVW002", "ID.4", "1.2.0"),
    ("WVW003", "Tiguan", "2.0.1")
]

cursor.executemany("""
INSERT INTO vehicles
(vin, model, sw_version)
VALUES (?, ?, ?)
""", vehicles)

# Testfälle
test_cases = [
    ("Lane Assist", "ADAS"),
    ("Emergency Braking", "ADAS"),
    ("Traffic Sign Detection", "Vision")
]

cursor.executemany("""
INSERT INTO test_cases
(name, category)
VALUES (?, ?)
""", test_cases)

# Testläufe
test_runs = [
    (1, 1, "PASSED", "2026-10-14"),
    (1, 2, "FAILED", "2026-10-14"),
    (2, 1, "PASSED", "2026-10-14"),
    (3, 3, "FAILED", "2026-10-14")
]

cursor.executemany("""
INSERT INTO test_runs
(vehicle_id,
 testcase_id,
 result,
 test_date)
VALUES (?, ?, ?, ?)
""", test_runs)

# Fehler
errors = [
    (2, "HIGH", "Emergency braking response timeout"),
    (4, "MEDIUM", "Traffic sign classification error")
]

cursor.executemany("""
INSERT INTO errors
(run_id, severity, description)
VALUES (?, ?, ?)
""", errors)

conn.commit()
conn.close()

print("✅ Beispieldaten erfolgreich eingefügt")# Hier erzeugen wir Beispieldaten

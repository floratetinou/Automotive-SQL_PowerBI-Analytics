import sqlite3
import pandas as pd

#Pandas
   #↓
#SQL Query
   #↓
#automotive.db
   #↓
#Ergebnis holen
   #↓
#DataFrame erstellen
import sqlite3
import pandas as pd
#from src.database_connection import (get_connection)
#from src.database.sqlite_connection import (get_connection)
from src.database.postgres_connection import (get_connection)


DATABASE_PATH = "automotive.db"


def get_all_vehicles():
    """
    Liest alle Fahrzeuge aus der Datenbank.
    """

    #conn = sqlite3.connect(DATABASE_PATH)
    conn = get_connection()

    query = """
    SELECT *
    FROM vehicles
    """

    df = pd.read_sql(query, conn)

    conn.close()

    return df


def get_vehicle_by_model(model_name):
    """
    Gibt alle Fahrzeuge eines bestimmten Modells zurück.

    Beispiel:
        get_vehicle_by_model("Golf 8")
    """

    #conn = sqlite3.connect(DATABASE_PATH)
    conn = get_connection()

    query = """
    SELECT *
    FROM vehicles
    WHERE model = ?
    """

    df = pd.read_sql(
        query,
        conn,
        params=(model_name,)
    )

    conn.close()

    return df
def get_vehicles_sorted_by_model():
    """
    Retourne tous les véhicules triés par modèle. de A a Z
    """

    #conn = sqlite3.connect(DATABASE_PATH)
    conn = get_connection()

    query = """
    SELECT *
    FROM vehicles
    ORDER BY model ASC
    """

    df = pd.read_sql(query, conn)

    conn.close()

    return df

def get_vehicles_sorted_desc():
    """
    Retourne les véhicules du Z vers A.
    """

    #conn = sqlite3.connect(DATABASE_PATH)
    conn = get_connection()

    query = """
    SELECT *
    FROM vehicles
    ORDER BY model DESC
    """

    df = pd.read_sql(query, conn)

    conn.close()

    return df

def count_vehicles():

    #conn = sqlite3.connect(DATABASE_PATH)
    conn = get_connection()

    query = """
    SELECT COUNT(*) AS total_vehicles
    FROM vehicles
    """

    df = pd.read_sql(query, conn)

    conn.close()

    return df

def count_test_runs():

    #conn = sqlite3.connect(DATABASE_PATH)
    conn = get_connection()

    query = """
    SELECT COUNT(*) AS total_runs
    FROM test_runs
    """

    df = pd.read_sql(query, conn)

    conn.close()

    return df
def get_test_results_summary():

    #conn = sqlite3.connect(DATABASE_PATH)
    conn = get_connection()

    query = """
    SELECT
        result,
        COUNT(*) AS total
    FROM test_runs
    GROUP BY result
    """

    df = pd.read_sql(query, conn)

    conn.close()

    return df

def count_testcases_per_category():

    #conn = sqlite3.connect(DATABASE_PATH)
    conn = get_connection()

    query = """
    SELECT
        category,
        COUNT(*) AS total
    FROM test_cases
    GROUP BY category
    """

    df = pd.read_sql(query, conn)

    conn.close()

    return df

def get_vehicle_test_results():

    #conn = sqlite3.connect(DATABASE_PATH)
    conn = get_connection()

    query = """
    SELECT
        vehicles.vehicle_id,
        vehicles.model,
        test_runs.run_id,
        test_runs.result,
        test_runs.test_date

    FROM vehicles

    INNER JOIN test_runs

    ON vehicles.vehicle_id = test_runs.vehicle_id
    """

    df = pd.read_sql(query, conn)

    conn.close()

    return df
def get_failed_tests_with_vehicle():

    #conn = sqlite3.connect(DATABASE_PATH)
    conn = get_connection()

    query = """
    SELECT
        vehicles.model,
        test_runs.result,
        test_runs.test_date

    FROM vehicles

    INNER JOIN test_runs

    ON vehicles.vehicle_id = test_runs.vehicle_id

    WHERE test_runs.result = 'FAILED'
    """

    df = pd.read_sql(query, conn)

    conn.close()

    return df
def get_vehicle_testcase_results():

    #conn = sqlite3.connect(DATABASE_PATH)
    conn = get_connection()

    query = """
    SELECT
        vehicles.model,
        test_cases.name AS test_case,
        test_runs.result,
        test_runs.test_date

    FROM test_runs

    INNER JOIN vehicles
        ON test_runs.vehicle_id =
           vehicles.vehicle_id

    INNER JOIN test_cases
        ON test_runs.testcase_id =
           test_cases.testcase_id
    """

    df = pd.read_sql(query, conn)

    conn.close()

    return df

def get_failed_tests_per_vehicle():

    #conn = sqlite3.connect(DATABASE_PATH)
    conn = get_connection()

    query = """
    SELECT
        vehicles.model,
        COUNT(*) AS failed_tests

    FROM test_runs

    INNER JOIN vehicles
        ON test_runs.vehicle_id =
           vehicles.vehicle_id

    WHERE test_runs.result = 'FAILED'

    GROUP BY vehicles.model

    ORDER BY failed_tests DESC
    """

    df = pd.read_sql(query, conn)

    conn.close()

    return df

if __name__ == "__main__":

    print("\n==============================")
    print("ALLE FAHRZEUGE")
    print("==============================")

    all_vehicles = get_all_vehicles()
    print(all_vehicles)

    print("\n==============================")
    print("NUR GOLF 8")
    print("==============================")

    golf_vehicles = get_vehicle_by_model("Golf 8")
    print(golf_vehicles)

    print("\n==============================")
    print("FAHRZEUGE SORTIERT NACH MODELL (A-Z)")
    print("==============================")

    vehicles_sorted_asc = get_vehicles_sorted_by_model()
    print(vehicles_sorted_asc)

    print("\n==============================")
    print("FAHRZEUGE SORTIERT NACH MODELL (Z-A)")
    print("==============================")

    vehicles_sorted_desc = get_vehicles_sorted_desc()
    print(vehicles_sorted_desc)

    print("\n==============================")
    print("ANZAHL DER FAHRZEUGE")
    print("==============================")

    total_vehicles = count_vehicles()
    print(total_vehicles)

    print("\n==============================")
    print("ANZAHL DER TESTLAUFEN")
    print("==============================")

    total_test_runs = count_test_runs()
    print(total_test_runs)

    print("\n==============================")
    print("ZUSAMMENFASSUNG DER TESTERGEBNISSE")
    print("==============================")

    test_results_summary = get_test_results_summary()
    print(test_results_summary)

    print("\n==============================")
    print("ANZAHL DER TESTFÄLLE PRO KATEGORIE")
    print("==============================")

    testcases_per_category = count_testcases_per_category()
    print(testcases_per_category)

    print("\n==============================")
    print("TESTERGEBNISSE PRO FAHRZEUG")
    print("==============================")

    vehicle_test_results = get_vehicle_test_results()
    print(vehicle_test_results)

    print("\n==============================")
    print("FEHLGESCHLAGENE TESTS MIT FAHRZEUG")
    print("==============================")

    failed_tests_with_vehicle = get_failed_tests_with_vehicle()
    print(failed_tests_with_vehicle)

    print("\n==============================")
    print("TESTERGEBNISSE PRO FAHRZEUG UND TESTFALL")
    print("==============================")

    vehicle_testcase_results = get_vehicle_testcase_results()
    print(vehicle_testcase_results)
    print("\n==============================")
    print("get_vehicle_testcase_results")
    print("==============================")
    print(get_vehicle_testcase_results())


 
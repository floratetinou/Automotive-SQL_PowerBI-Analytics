import pandas as pd

from src.database.postgres_connection import get_connection


def execute_query(query, params=None):
    """
    Führt eine SELECT-Abfrage in PostgreSQL aus
    und gibt das Ergebnis als Pandas DataFrame zurück.
    """

    conn = get_connection()

    try:
        df = pd.read_sql_query(
            query,
            conn,
            params=params
        )

        return df

    finally:
        conn.close()


def get_all_vehicles():
    """
    Liest alle Fahrzeuge aus PostgreSQL.
    """

    query = """
    SELECT
        vehicle_id,
        vin,
        model,
        sw_version
    FROM vehicles
    ORDER BY vehicle_id
    """

    return execute_query(query)


def get_vehicle_by_model(model_name):
    """
    Gibt alle Fahrzeuge eines bestimmten Modells zurück.

    Beispiel:
        get_vehicle_by_model("Golf 8")
    """

    query = """
    SELECT
        vehicle_id,
        vin,
        model,
        sw_version
    FROM vehicles
    WHERE model = %s
    ORDER BY vehicle_id
    """

    return execute_query(
        query,
        params=(model_name,)
    )


def get_vehicles_sorted_by_model():
    """
    Gibt alle Fahrzeuge alphabetisch nach Modell zurück.
    Sortierung: A bis Z
    """

    query = """
    SELECT
        vehicle_id,
        vin,
        model,
        sw_version
    FROM vehicles
    ORDER BY model ASC
    """

    return execute_query(query)


def get_vehicles_sorted_desc():
    """
    Gibt alle Fahrzeuge absteigend nach Modell zurück.
    Sortierung: Z bis A
    """

    query = """
    SELECT
        vehicle_id,
        vin,
        model,
        sw_version
    FROM vehicles
    ORDER BY model DESC
    """

    return execute_query(query)


def count_vehicles():
    """
    Zählt alle Fahrzeuge.
    """

    query = """
    SELECT
        COUNT(*) AS total_vehicles
    FROM vehicles
    """

    return execute_query(query)


def count_test_runs():
    """
    Zählt alle Testläufe.
    """

    query = """
    SELECT
        COUNT(*) AS total_runs
    FROM test_runs
    """

    return execute_query(query)


def get_test_results_summary():
    """
    Gruppiert die Testläufe nach Ergebnis
    und zählt die Tests pro Ergebnis.
    """

    query = """
    SELECT
        result,
        COUNT(*) AS total
    FROM test_runs
    GROUP BY result
    ORDER BY result
    """

    return execute_query(query)


def count_testcases_per_category():
    """
    Zählt die Testfälle pro Kategorie.
    """

    query = """
    SELECT
        category,
        COUNT(*) AS total
    FROM test_cases
    GROUP BY category
    ORDER BY category
    """

    return execute_query(query)


def get_vehicle_test_results():
    """
    Verknüpft Fahrzeuge mit ihren Testläufen.
    """

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
    ORDER BY test_runs.test_date, test_runs.run_id
    """

    return execute_query(query)


def get_failed_tests_with_vehicle():
    """
    Gibt nur fehlgeschlagene Tests mit Fahrzeugmodell zurück.
    """

    query = """
    SELECT
        vehicles.model,
        test_runs.result,
        test_runs.test_date
    FROM vehicles
    INNER JOIN test_runs
        ON vehicles.vehicle_id = test_runs.vehicle_id
    WHERE test_runs.result = 'FAILED'
    ORDER BY test_runs.test_date, vehicles.model
    """

    return execute_query(query)


def get_vehicle_testcase_results():
    """
    Triple JOIN:
    Verknüpft Testläufe, Fahrzeuge und Testfälle.
    """

    query = """
    SELECT
        vehicles.model,
        test_cases.name AS test_case,
        test_cases.category,
        test_runs.result,
        test_runs.test_date
    FROM test_runs
    INNER JOIN vehicles
        ON test_runs.vehicle_id = vehicles.vehicle_id
    INNER JOIN test_cases
        ON test_runs.testcase_id = test_cases.testcase_id
    ORDER BY test_runs.test_date, vehicles.model
    """

    return execute_query(query)


def get_failed_tests_per_vehicle():
    """
    Zählt die fehlgeschlagenen Tests pro Fahrzeug.
    """

    query = """
    SELECT
        vehicles.model,
        COUNT(*) AS failed_tests
    FROM test_runs
    INNER JOIN vehicles
        ON test_runs.vehicle_id = vehicles.vehicle_id
    WHERE test_runs.result = 'FAILED'
    GROUP BY vehicles.model
    ORDER BY failed_tests DESC, vehicles.model
    """

    return execute_query(query)


def print_section(title, dataframe):
    """
    Zeigt ein Abfrageergebnis übersichtlich im Terminal an.
    """

    print("\n" + "=" * 50)
    print(title)
    print("=" * 50)

    if dataframe.empty:
        print("Keine Daten gefunden.")
    else:
        print(dataframe.to_string(index=False))


def main():
    """
    Führt alle SQL-Abfragen zum Testen aus.
    """

    print("PostgreSQL-Abfragen werden ausgeführt ...")

    print_section(
        "ALLE FAHRZEUGE",
        get_all_vehicles()
    )

    print_section(
        "NUR GOLF 8",
        get_vehicle_by_model("Golf 8")
    )

    print_section(
        "FAHRZEUGE SORTIERT NACH MODELL (A-Z)",
        get_vehicles_sorted_by_model()
    )

    print_section(
        "FAHRZEUGE SORTIERT NACH MODELL (Z-A)",
        get_vehicles_sorted_desc()
    )

    print_section(
        "ANZAHL DER FAHRZEUGE",
        count_vehicles()
    )

    print_section(
        "ANZAHL DER TESTLÄUFE",
        count_test_runs()
    )

    print_section(
        "ZUSAMMENFASSUNG DER TESTERGEBNISSE",
        get_test_results_summary()
    )

    print_section(
        "ANZAHL DER TESTFÄLLE PRO KATEGORIE",
        count_testcases_per_category()
    )

    print_section(
        "TESTERGEBNISSE PRO FAHRZEUG",
        get_vehicle_test_results()
    )

    print_section(
        "FEHLGESCHLAGENE TESTS MIT FAHRZEUG",
        get_failed_tests_with_vehicle()
    )

    print_section(
        "TESTERGEBNISSE PRO FAHRZEUG UND TESTFALL",
        get_vehicle_testcase_results()
    )

    print_section(
        "FEHLGESCHLAGENE TESTS PRO FAHRZEUG",
        get_failed_tests_per_vehicle()
    )

    print("\n✅ Alle PostgreSQL-Abfragen wurden ausgeführt.")


if __name__ == "__main__":
    main()
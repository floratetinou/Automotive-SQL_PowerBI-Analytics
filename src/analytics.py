import pandas as pd

from src.sql_queries_postgres import (
    get_all_vehicles,
    get_vehicle_testcase_results,
    get_failed_tests_per_vehicle
)# Hier kommen Pandas-Analysen hinein

def calculate_total_vehicles():

    df = get_all_vehicles()

    total = len(df)

    return total  

def calculate_total_tests():

    df = get_vehicle_testcase_results()

    total = len(df)

    return total
def calculate_pass_rate():

    df = get_vehicle_testcase_results()

    passed = len(
        df[df["result"] == "PASSED"]
    )

    total = len(df)

    if total == 0:
        return 0

    return round(
        passed / total * 100,
        2
    )

def calculate_failure_rate():

    df = get_vehicle_testcase_results()

    failed = len(
        df[df["result"] == "FAILED"]
    )

    total = len(df)

    if total == 0:
        return 0

    return round(
        failed / total * 100,
        2
    )
def get_worst_vehicle():

    df = get_failed_tests_per_vehicle()

    if df.empty:
        return "Keine Daten"

    return df.iloc[0]["model"]
def dashboard_summary():

    summary = {
        "total_vehicles":
            calculate_total_vehicles(),

        "total_tests":
            calculate_total_tests(),

        "pass_rate":
            calculate_pass_rate(),

        "failure_rate":
            calculate_failure_rate(),
        "worst_vehicle":
            get_worst_vehicle()
    }

    return summary

if __name__ == "__main__":

    print()

    print("===== DASHBOARD KPI =====")

    print(
        dashboard_summary()
    )

    print()

    print(
        "Worst vehicle:"
    )

    print(
        get_worst_vehicle()
    )

from pathlib import Path

from src.analytics import (
    dashboard_summary
)

from src.sql_queries import (
    get_vehicle_testcase_results,
    get_failed_tests_per_vehicle
)


EXPORT_FOLDER = "reports/output"


def create_output_folder():

    Path(EXPORT_FOLDER).mkdir(
        parents=True,
        exist_ok=True
    )


def export_vehicle_test_results():

    df = get_vehicle_testcase_results()

    file_path = (
        f"{EXPORT_FOLDER}/vehicle_test_results.csv"
    )

    df.to_csv(
        file_path,
        index=False
    )

    print(
        f"✅ Exportiert: {file_path}"
    )


def export_failed_tests():

    df = get_failed_tests_per_vehicle()

    file_path = (
        f"{EXPORT_FOLDER}/failed_tests_per_vehicle.csv"
    )

    df.to_csv(
        file_path,
        index=False
    )

    print(
        f"✅ Exportiert: {file_path}"
    )


def export_dashboard_summary():

    summary = dashboard_summary()

    import pandas as pd

    df = pd.DataFrame([summary])

    file_path = (
        f"{EXPORT_FOLDER}/dashboard_summary.csv"
    )

    df.to_csv(
        file_path,
        index=False
    )

    print(
        f"✅ Exportiert: {file_path}"
    )


if __name__ == "__main__":

    create_output_folder()

    export_vehicle_test_results()

    export_failed_tests()

    export_dashboard_summary()

    print()
    print("✅ Alle Reports exportiert")# Exportfunktionen

import sys
from pathlib import Path

ROOT_DIR = Path(__file__).resolve().parent.parent

sys.path.append(str(ROOT_DIR))

import streamlit as st
import plotly.express as px

from src.analytics import (
    dashboard_summary
)

from src.sql_queries_postgres import (
    get_vehicle_testcase_results,
    get_failed_tests_per_vehicle
)


# =====================================
# Configuration de la page
# =====================================

st.set_page_config(
    page_title="Automotive Analytics",
    page_icon="🚗",
    layout="wide"
)


# =====================================
# Titre
# =====================================

st.title("🚗 Automotive Test Analytics Platform")

st.markdown(
    "Dashboard SQL + Python + Pandas"
)


# =====================================
# KPIs
# =====================================

summary = dashboard_summary()

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric(
        "Vehicles",
        summary["total_vehicles"]
    )

with col2:
    st.metric(
        "Tests",
        summary["total_tests"]
    )

with col3:
    st.metric(
        "Pass Rate",
        f"{summary['pass_rate']} %"
    )

with col4:
    st.metric(
        "Failure Rate",
        f"{summary['failure_rate']} %"
    )


st.divider()


# =====================================
# Vehicle Test Results
# =====================================

st.subheader(
    "Vehicle Test Results"
)

df_results = get_vehicle_testcase_results()

st.dataframe(
    df_results,
    use_container_width=True
)


st.divider()


# =====================================
# Failed Tests per Vehicle
# =====================================

st.subheader(
    "Failed Tests per Vehicle"
)

df_failed = get_failed_tests_per_vehicle()

st.dataframe(
    df_failed,
    use_container_width=True
)

st.subheader("Test Results Overview")

df_results = get_vehicle_testcase_results()

result_counts = (
    df_results["result"]
    .value_counts()
    .reset_index()
)

result_counts.columns = [
    "result",
    "count"
]

fig = px.pie(
    result_counts,
    values="count",
    names="result",
    title="Pass vs Failed Tests"
)

st.plotly_chart(
    fig,
    use_container_width=True
)
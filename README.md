# Automotive SQL & Power BI Analytics Platform

## Overview

This end-to-end data analytics project uses an automotive testing use case to demonstrate how data moves from a relational database to analysis and interactive dashboards.

The project was developed progressively:

1. Database design and SQL learning with SQLite
2. Migration from SQLite to PostgreSQL
3. Data analysis and KPI calculation with Python and Pandas
4. Interactive dashboard development with Streamlit
5. Business reporting with Power BI
6. Containerization of the application and PostgreSQL with Docker and Docker Compose

## Technologies

- Python
- SQL
- SQLite
- PostgreSQL
- Pandas
- Streamlit
- Power BI
- Docker
- Docker Compose
- psycopg2
- SQLAlchemy

## Main Features

- Relational database model for automotive test data
- Vehicle, test-case, test-run, and error management
- Parameterized SQL queries from Python
- Data filtering, sorting, grouping, and aggregation
- Multi-table SQL joins
- Automated KPI calculation
- CSV report generation
- Interactive Streamlit dashboard
- Power BI dashboard connected to PostgreSQL
- Docker image for the Python application
- PostgreSQL container with persistent storage

## Data Model

The platform uses four principal tables:

### `vehicles`

Stores vehicle information:

- `vehicle_id`
- `vin`
- `model`
- `sw_version`

### `test_cases`

Stores test-case definitions:

- `testcase_id`
- `name`
- `category`

### `test_runs`

Stores executed test runs:

- `run_id`
- `vehicle_id`
- `testcase_id`
- `result`
- `test_date`

### `errors`

Stores errors associated with test runs:

- `error_id`
- `run_id`
- `severity`
- `description`

## Database Relationships

```text
vehicles (1) ────────< test_runs >──────── (1) test_cases
                          |
                          |
                          v
                       errors
```

- One vehicle can have multiple test runs.
- One test case can be executed in multiple test runs.
- One test run can be associated with error records.

## SQL Skills Demonstrated

The project contains practical examples of:

- `CREATE TABLE`
- `INSERT INTO`
- `SELECT`
- `WHERE`
- `ORDER BY`
- `COUNT()`
- `GROUP BY`
- `INNER JOIN`
- Multi-table joins
- Primary keys
- Foreign keys
- Parameterized queries

Example query:

```sql
SELECT
    vehicles.model,
    test_cases.name AS test_case,
    test_runs.result,
    test_runs.test_date
FROM test_runs
INNER JOIN vehicles
    ON test_runs.vehicle_id = vehicles.vehicle_id
INNER JOIN test_cases
    ON test_runs.testcase_id = test_cases.testcase_id;
```

## Analytics and KPIs

The Python analytics layer calculates:

- Total number of vehicles
- Total number of executed tests
- Pass rate
- Failure rate
- Failed tests per vehicle
- Vehicle with the highest number of failed tests
- Test distribution by result and category

## Architecture

```text
SQLite / PostgreSQL
        |
        v
     SQL Queries
        |
        v
  Pandas Analytics
        |
        +-------------------+
        |                   |
        v                   v
Streamlit Dashboard     Power BI Dashboard
        |
        v
 Docker / Docker Compose
```

## Project Structure

```text
Automotive_SQL_PowerBI/
|
├── dashboard/
│   └── app.py
|
├── reports/
│   ├── export_csv.py
│   └── output/
|
├── screenshots/
│   ├── streamlit_dashboard.png
│   └── powerbi_dashboard.png
|
├── src/
│   ├── database/
│   │   ├── __init__.py
│   │   ├── postgres_connection.py
│   │   └── sqlite_connection.py
│   ├── __init__.py
│   ├── analytics.py
│   ├── create_database.py
│   ├── create_postgres_tables.py
│   ├── insert_sample_data.py
│   ├── insert_postgres_data.py
│   ├── sql_queries.py
│   └── sql_queries_postgres.py
|
├── .dockerignore
├── .gitignore
├── Dockerfile
├── docker-compose.yml
├── requirements.txt
└── README.md
```

> The exact file names can be adjusted to match the current repository structure.

## Local Setup

### 1. Clone the repository

```bash
git clone <REPOSITORY_URL>
cd Automotive_SQL_PowerBI
```

### 2. Create a virtual environment

Windows PowerShell:

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

### 3. Install dependencies

```powershell
pip install -r requirements.txt
```

### 4. Configure PostgreSQL credentials

Do not store database passwords directly in source code or commit them to GitHub.

Create a local `.env` file and add it to `.gitignore`:

```text
POSTGRES_HOST=localhost
POSTGRES_PORT=5432
POSTGRES_DB=automotive
POSTGRES_USER=postgres
POSTGRES_PASSWORD=your_password
```

### 5. Create the PostgreSQL tables

```powershell
python -m src.create_postgres_tables
```

### 6. Insert sample data

```powershell
python -m src.insert_postgres_data
```

### 7. Run the analytics module

```powershell
python -m src.analytics
```

### 8. Start the Streamlit dashboard

```powershell
streamlit run dashboard/app.py
```

## Docker Setup

### Build the application image

```powershell
docker build -t automotive-analytics .
```

### Start PostgreSQL with Docker Compose

```powershell
docker compose up -d
```

### Check running containers

```powershell
docker ps
```

### View PostgreSQL logs

```powershell
docker logs automotive-postgres
```

### Stop the Compose services

```powershell
docker compose down
```

The PostgreSQL Docker volume keeps database data persistent when the container is stopped and restarted.

## Power BI Dashboard

The Power BI report connects to PostgreSQL and presents:

- Total Vehicles
- Total Tests
- Pass Rate
- Failure Rate
- Failed Tests per Vehicle
- Passed vs. Failed Tests
- Detailed test-result table
- Interactive filters by vehicle and test result

Add a screenshot after placing the image in the `screenshots` directory:

```markdown
![Power BI Dashboard](screenshots/powerbi_dashboard.png)
```

## Streamlit Dashboard

The Streamlit application provides a Python-based interactive view of the same automotive test analytics.

Add a screenshot after placing the image in the `screenshots` directory:

```markdown
![Streamlit Dashboard](screenshots/streamlit_dashboard.png)
```

## Security Notes

- Never commit PostgreSQL passwords or other credentials.
- Keep `.env` in `.gitignore`.
- Do not upload confidential company data, VINs, test results, or proprietary code.
- Use synthetic sample data for the public GitHub repository.
- Review Power BI files and screenshots before publishing them.

## Learning Outcomes

This project demonstrates practical experience with:

- Relational data modeling
- SQL querying and joins
- SQLite and PostgreSQL
- Python database integration
- Data analysis with Pandas
- KPI design and calculation
- Streamlit dashboard development
- Power BI reporting
- Docker images and containers
- Docker Compose and persistent PostgreSQL storage

## Future Improvements

- Use SQLAlchemy throughout the application
- Move all credentials to environment variables
- Add database migrations
- Add data-validation rules
- Add automated tests with `pytest`
- Add a larger synthetic automotive dataset
- Add additional Power BI pages and DAX measures
- Containerize the Streamlit application together with PostgreSQL
- Add continuous integration with GitHub Actions

## Author

Flora Tetinou-Sawouo

## License

This repository is intended as a learning and portfolio project. Add an open-source license before permitting reuse or redistribution.

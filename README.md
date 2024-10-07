[![CI](https://github.com/nogibjj/Mobasserul_Haque_MiniProject5/actions/workflows/cicd.yml/badge.svg)](https://github.com/nogibjj/Mobasserul_Haque_MiniProject5/actions/workflows/cicd.yml)

# Airline Safety Database ETL and Query Tool

This project provides an ETL (Extract, Transform, Load) and querying tool for managing and analyzing the Airline Safety Database. It is built using Python and SQLite, enabling users to perform various operations on airline safety records, including extraction, loading, updating, deleting, creating, and querying records.

## Features

- **ETL Operations**: 
  - Extract data from a source.
  - Transform and load data into the SQLite database.
  
- **Query Operations**:
  - Update existing records in the database.
  - Delete records based on a unique identifier.
  - Create new records in the database.
  - Execute custom SQL queries.
  - Read a limited number of records from the database.

- **Logging and Output**:
  - All executed queries are logged in a markdown file for reference.
  - Query results are outputted in a formatted markdown file for easier readability.

## Directory Structure

├── .devcontainer/
│   ├── devcontainer.json
│   └── Dockerfile
├── .github/
│   └── workflows/cicd.yml
├── data/
│   └── airline_safety.csv
├── myLib/
│   ├── __init__.py
│   ├── __pycache__/
│   ├── extract.py
│   ├── query.py
│   └── transform_load.py
├── AirlineSafetyDB.db
├── main.py
├── Makefile
├── query_log.md
├── query_output.md
├── README.md  
├── ServeTimesDB.db  requirements.txt
└── test_main.py

## CRUD operations : 

## Usage

Run the script using the following command:

```python
python main.py <action> [arguments]
```
## Arguments: 

`record_id`, `airline`, `avail_seat_km_per_week`, `incidents_85_99`, `fatal_accidents_85_99`, `fatalities_85_99`, `incidents_00_14`, `fatal_accidents_00_14`, `fatalities_00_14`

## Actions:

extract: Extract data from the source.

```python
python main.py extract
```
transform_load: Transform and load data into the database.

```python
python main.py transform_load
```
update_record: Update an existing record in the database.

```python
python main.py update_record(1, "Air Canada", 2000000000, 3, 1, 5, 2, 0, 0)
```
create_record: Create a new record in the database

```python
python main.py create_record("Air Canada", 1865253802, 2, 0, 0, 2, 0, 0)
```
delete_record: delete an existing record in the database.

```python
python main.py delete_record(1)
```
read_data: Read and display the top N rows from the database.

```python
python main.py read_data(10)  # Reads the top 10 rows
```
general_query: Run a custom SQL query on the database.

```python
python main.py "SELECT * FROM AirlineSafety WHERE airline = 'Aeroflot*'"
```

## Testing
To run the test suite, use:

```python
python -m pytest -vv --cov=main --cov=myLib test_*.py
```
## References 
https://github.com/nogibjj/sqlite-lab
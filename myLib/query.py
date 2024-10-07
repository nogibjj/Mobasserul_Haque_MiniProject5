"""Query the AirlineSafetyDB database"""

import sqlite3
from tabulate import tabulate

# Define a global variable for the log file
LOG_FILE = "query_log.md"


def log_query(query):
    """Adds to a query markdown file"""
    with open(LOG_FILE, "a") as file:
        file.write(f"```sql\n{query}\n```\n\n")


def general_query(query):
    """Runs a query the user inputs"""
    # Connect to the SQLite database
    conn = sqlite3.connect("AirlineSafetyDB.db")
    cursor = conn.cursor()

    # Execute the query
    cursor.execute(query)

    # If the query modifies the database, commit the changes
    if query.strip().lower().startswith(("insert", "update", "delete")):
        conn.commit()

    # Close the cursor and connection
    cursor.close()
    conn.close()

    # Log the query
    log_query(f"{query}")


def create_record(airline, avail_seat_km_per_week, incidents_85_99, fatal_accidents_85_99, 
                  fatalities_85_99, incidents_00_14, fatal_accidents_00_14, fatalities_00_14):
    """Create a new record in the AirlineSafetyDB"""
    conn = sqlite3.connect("AirlineSafetyDB.db")
    cursor = conn.cursor()
    cursor.execute(
        """
        INSERT INTO AirlineSafety 
        (airline, avail_seat_km_per_week, incidents_85_99, fatal_accidents_85_99, fatalities_85_99, 
        incidents_00_14, fatal_accidents_00_14, fatalities_00_14) 
        VALUES (?, ?, ?, ?, ?, ?, ?, ?)
        """,
        (airline, avail_seat_km_per_week, incidents_85_99, fatal_accidents_85_99, fatalities_85_99, 
         incidents_00_14, fatal_accidents_00_14, fatalities_00_14),
    )
    conn.commit()
    conn.close()

    # Log the query
    log_query(
        f"""INSERT INTO AirlineSafety VALUES (
            {airline}, {avail_seat_km_per_week}, {incidents_85_99}, {fatal_accidents_85_99}, {fatalities_85_99}, 
            {incidents_00_14}, {fatal_accidents_00_14}, {fatalities_00_14});"""
    )


def update_record(record_id, airline, avail_seat_km_per_week, incidents_85_99, fatal_accidents_85_99, 
                  fatalities_85_99, incidents_00_14, fatal_accidents_00_14, fatalities_00_14):
    """Update a record in the AirlineSafetyDB"""
    conn = sqlite3.connect("AirlineSafetyDB.db")
    cursor = conn.cursor()
    cursor.execute(
        """
        UPDATE AirlineSafety 
        SET airline=?, avail_seat_km_per_week=?, incidents_85_99=?, fatal_accidents_85_99=?, 
            fatalities_85_99=?, incidents_00_14=?, fatal_accidents_00_14=?, fatalities_00_14=? 
        WHERE id=?
        """,
        (
            airline, avail_seat_km_per_week, incidents_85_99, fatal_accidents_85_99, fatalities_85_99, 
            incidents_00_14, fatal_accidents_00_14, fatalities_00_14, record_id,
        ),
    )
    conn.commit()
    conn.close()

    # Log the query
    log_query(
        f"""UPDATE AirlineSafety SET 
            airline={airline}, avail_seat_km_per_week={avail_seat_km_per_week}, 
            incidents_85_99={incidents_85_99}, fatal_accidents_85_99={fatal_accidents_85_99}, 
            fatalities_85_99={fatalities_85_99}, incidents_00_14={incidents_00_14}, 
            fatal_accidents_00_14={fatal_accidents_00_14}, fatalities_00_14={fatalities_00_14} 
        WHERE id={record_id};"""
    )


def delete_record(record_id):
    """Delete a record from the AirlineSafetyDB"""
    conn = sqlite3.connect("AirlineSafetyDB.db")
    cursor = conn.cursor()
    cursor.execute("DELETE FROM AirlineSafety WHERE id=?", (record_id,))
    conn.commit()
    conn.close()

    # Log the query
    log_query(f"DELETE FROM AirlineSafety WHERE id={record_id};")


def read_data(limit=10):
    """Read the top N rows from the AirlineSafety table"""
    conn = sqlite3.connect("AirlineSafetyDB.db")
    cursor = conn.cursor()
    cursor.execute(f"SELECT * FROM AirlineSafety LIMIT {limit}")
    data = cursor.fetchall()
    
    # Get column names
    col_names = [description[0] for description in cursor.description]

    # Log the query
    log_query(f"SELECT * FROM AirlineSafety LIMIT {limit};")

    # Display the data using tabulate
    if data:
        print(tabulate(data, headers=col_names, tablefmt="grid"))
    else:
        print("No data found.")
    
    conn.close()
    return data





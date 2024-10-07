"""
Transforms and Loads airline safety data into a local SQLite3 database
"""
import sqlite3
import csv


# Load the csv file and insert data into a new SQLite3 database
def load(dataset="data/airline-safety.csv"):
    """Transforms and Loads airline safety data into the local SQLite3 database"""
    
    # Open the dataset and skip the header
    with open(dataset, newline="") as csvfile:
        payload = csv.reader(csvfile, delimiter=",")
        next(payload)  # Skips the header row
        
        # Connect to the SQLite database (or create it if it doesn't exist)
        conn = sqlite3.connect("AirlineSafetyDB.db")
        c = conn.cursor()
        
        # Drop the table if it already exists to avoid duplicate data
        c.execute("DROP TABLE IF EXISTS AirlineSafety")
        
        # Create a new table for airline safety data
        c.execute(
            """
            CREATE TABLE AirlineSafety (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                airline TEXT,
                avail_seat_km_per_week INTEGER,
                incidents_85_99 INTEGER,
                fatal_accidents_85_99 INTEGER,
                fatalities_85_99 INTEGER,
                incidents_00_14 INTEGER,
                fatal_accidents_00_14 INTEGER,
                fatalities_00_14 INTEGER
            )
            """
        )
        
        # Insert data into the table
        c.executemany(
            """
            INSERT INTO AirlineSafety (
                airline, 
                avail_seat_km_per_week, 
                incidents_85_99, 
                fatal_accidents_85_99, 
                fatalities_85_99,
                incidents_00_14,
                fatal_accidents_00_14,
                fatalities_00_14
            ) 
            VALUES (?, ?, ?, ?, ?, ?, ?, ?)
            """,
            payload
        )
        
        conn.commit()
        conn.close()
        
    return "AirlineSafetyDB.db"

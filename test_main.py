"""
Test cases for AirlineSafetyDB

"""

import subprocess


def test_extract():
    """Tests extract()"""
    result = subprocess.run(
        ["python", "main.py", "extract"],
        capture_output=True,
        text=True,
        check=True,
    )
    assert result.returncode == 0
    assert "Extracting data..." in result.stdout


def test_transform_load():
    """Tests transform_load()"""
    result = subprocess.run(
        ["python", "main.py", "transform_load"],
        capture_output=True,
        text=True,
        check=True,
    )
    assert result.returncode == 0
    assert "Transforming data..." in result.stdout


def test_update_record():
    """Tests update_record()"""
    result = subprocess.run(
        [
            "python",
            "main.py",
            "update_record",
            "1",  # Record ID to update
            "Updated Airline A",  # Airline name
            "600000",  # Avail seat km per week
            "3",  # Incidents 85-99
            "0",  # Fatal accidents 85-99
            "1",  # Fatalities 85-99
            "0",  # Incidents 00-14
            "1",  # Fatal accidents 00-14
            "0"   # Fatalities 00-14
        ],
        capture_output=True,
        text=True,
        check=True,
    )
    assert result.returncode == 0


def test_delete_record():
    """Tests delete_record()"""
    result = subprocess.run(
        ["python", "main.py", "delete_record", "1"],  # Record ID to delete
        capture_output=True,
        text=True,
        check=True,
    )
    assert result.returncode == 0


def test_create_record():
    """Tests create_record()"""
    result = subprocess.run(
        [
            "python",
            "main.py",
            "create_record",
            "New Airline",  # Airline name
            "1000000",  # Avail seat km per week
            "2",  # Incidents 85-99
            "0",  # Fatal accidents 85-99
            "0",  # Fatalities 85-99
            "1",  # Incidents 00-14
            "0",  # Fatal accidents 00-14
            "0"   # Fatalities 00-14
        ],
        capture_output=True,
        text=True,
        check=True,
    )
    assert result.returncode == 0


def test_general_query():
    """Tests general_query()"""
    result = subprocess.run(
        [
            "python",
            "main.py",
            "general_query",
            "SELECT * FROM AirlineSafetyDB WHERE airline = 'Aeroflot*'",
        ],
        capture_output=True,
        text=True,
        check=True,
    )
    assert result.returncode == 0


def test_read_data():
    """Tests read_data()"""
    result = subprocess.run(
        ["python", "main.py", "read_data"],
        capture_output=True,
        text=True,
        check=True,
    )
    assert result.returncode == 0


if __name__ == "__main__":
    test_extract()
    test_transform_load()
    test_create_record()
    test_read_data()
    test_update_record()
    test_delete_record()
    test_general_query()

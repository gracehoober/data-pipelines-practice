"""Question 2: Data Quality Monitoring (Medium - 25 min)
Scenario: The data labeling team reports that some flight videos have "gaps" where
telemetry data is missing for several seconds. This causes problems for training
AI models. You need to build a data quality checker.
Given:

A SQLite database with a telemetry table
(columns: flight_id, timestamp, altitude, speed)
Flights should have readings every 1 second
Acceptable gap: up to 2 seconds
Problem gap: 3+ seconds missing

Tasks:

Write a Python function that identifies flights with problematic gaps
Return a report showing: flight_id, number of gaps, longest gap duration
Discuss: How would you modify this for a time series database like InfluxDB
instead of SQL?

What they're testing:

SQL query skills (window functions, time arithmetic)
Data quality thinking
Understanding of time series vs relational trade-offs
Communication about design decisions"""

import sqlite3


def open_db_connection(db_name: str):
    if db_name is None:
        db_name = "drone_data.db"

    return sqlite3.connect(db_name)


def close_db_connection(db_connection):
    db_connection.close()
    return


def fetch_rows(db_conn, table_name, flight_id: str | None):
    try:
        cursor = db_conn.cursor()
        if flight_id:
            cursor.execute(
                f"SELECT * FROM {table_name} WHERE flight_id = ? ORDER BY timestamp",
                (flight_id,),
            )
        else:
            print("flight_id was not provided, all flights being obtained")
            cursor.execute(
                f"SELECT * FROM {table_name} ORDER BY flight_id, timestamp ASC"
            )
        rows = cursor.fetchall()
    except sqlite3.DatabaseError:
        raise sqlite3.DatabaseError(f"Unable to obtain table rows from {table_name}.")
    finally:
        close_db_connection(db_connection=db_conn)

    return rows


def flight_gap_handler_python(flight_id: str) -> list:
    table_name = "flight_telemetry"
    db_conn = open_db_connection(table_name)
    rows = fetch_rows(db_conn=db_conn, table_name=table_name, flight_id=flight_id)
    # [{row1}, {row2]}
    report = []
    # TODO: fix nested if possible
    for i in range(0, len(rows) - 1):
        flight_report = {"flight_id": "", "gaps": 0, "longest_gap": 0}
        gap = rows[i + 1]["timestamp"] - rows[i]["timestamp"]  # TODO: fix time calc
        if gap > 3:
            flight_report["flight_id"] = rows[i]["flight_id"]
            flight_report["gaps"] += 1
            if gap > flight_report["longest_gap"]:
                flight_report["longest_gap"] = gap
            report.append(flight_report)

    return report


def flight_gap_handler_sql():
    pass

"""Scenario: FlightShepherd drones send JSON packets every second during flight
containing basic telemetry. You need to design a Python service that receives
this data and stores it.
Sample data format:
json{
  "flight_id": "FS-2025-001",
  "timestamp": "2025-11-02T10:30:45Z",
  "latitude": 37.7749,
  "longitude": -122.4194,
  "altitude_meters": 120.5,
  "battery_percent": 85
}
Tasks:

Design a simple relational database schema to store this data (just describe t
he table structure)
Write a Python class that validates incoming JSON and inserts it into a SQLite
database.
Handle edge cases: duplicate timestamps, missing fields, invalid coordinates"""
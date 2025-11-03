"""Scenario: drones send JSON packets every second during flight
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

- Design a simple relational database schema to store this data (just describe
the table structure)
- Write a Python class that validates incoming JSON and inserts it into a SQLite
database.
- Handle edge cases: duplicate timestamps, missing fields, invalid coordinates."""

import sqlite3
from datetime import datetime


class FlightDBConnection:
    def __init__(self):
        self.create_table_if_not_exists()

    def open(self):
        self.db = sqlite3.connect("drone_data.db")
        self.cursor = self.db.cursor()

    def close(self):
        self.db.close()

    def create_table_if_not_exists(self):
        try:
            self.open()
            self.cursor.execute(
                "CREATE TABLE IF NOT EXISTS flight_telemetry ("
                "flight_id TEXT NOT NULL,"
                "timestamp DATETIME NOT NULL,"
                "latitude REAL NOT NULL,"
                "longitude REAL NOT NULL,"
                "altitude_meters REAL NOT NULL,"
                "battery_percent INTEGER,"
                "PRIMARY KEY (flight_id, timestamp)"
                ")"
            )
            self.db.commit()
        except sqlite3.DatabaseError as e:
            raise sqlite3.DatabaseError(e)
        finally:
            self.db.close()


class FlightSerializer:
    def __init__(self, db_connection):
        self.db = db_connection

    def save(self, data: dict) -> None:
        """Saves validated data to the database and returns success or
        failure message.
        """

        self.db.open()
        try:
            self.db.cursor.execute(
                """INSERT INTO flight_telemetry
                                (flight_id,
                                timestamp,
                                latitude,
                                longitude,
                                altitude_meters,
                                battery_percent)
                                values(?,?,?,?,?,?)""",
                (
                    data["flight_id"],
                    data["timestamp"],
                    data["latitude"],
                    data["longitude"],
                    data["altitude_meters"],
                    data.get("battery_percent"),
                ),
            )

            self.db.db_connection.commit()

        except sqlite3.IntegrityError as e:
            raise ValueError(f"Failed to save data: {e}")

        finally:
            self.db.close()

    def validate_and_save(self, data: dict) -> dict:
        validated_data = self.validate_data(data)
        result = self.save(validated_data)
        return result

    def validate_data(self, data: dict) -> dict:
        """Ensure all data is serialized correctly for saving in db."""

        # valid feilds
        valid_feilds = [
            "flight_id",
            "timestamp",
            "latitude",
            "longitude",
            "altitude_meters",
        ]

        missing = [feild for feild in valid_feilds if feild not in data]

        if missing:
            raise KeyError(f"The following keys are required: {missing}")

        # validate feild data
        flight_id = self._validate_flight_id(data.get("flight_id"))
        timestamp = self._validate_timestamp(data.get("timestamp"))
        latitude = self._validate_latitude(data.get("latitude"))
        longitude = self._validate_longitude(data.get("longitude"))
        altitude_meters = self._validate_altitude_meters(data.get("altitude_meters"))
        battery_percent = self._validate_battery_percent(data.get("battery_percent"))

        validated_data = {
            "flight_id": flight_id,
            "timestamp": timestamp,
            "latitude": latitude,
            "longitude": longitude,
            "altitude_meters": altitude_meters,
            "battery_percent": battery_percent,
        }

        return validated_data

    def _validate_flight_id(self, flight_id):

        if not flight_id or not isinstance(flight_id, str):
            raise ValueError("provided flight_id is not a string, must be of type str.")

        return flight_id

    def _validate_timestamp(self, timestamp):
        if not timestamp:
            raise ValueError("timestamp value must be provided.")
        try:
            isoformat_timestamp = datetime.fromisoformat(timestamp)
        except ValueError:
            raise ValueError("timestamp must be a valid iso format.")

        return isoformat_timestamp

    def _validate_latitude(self, latitude):
        if latitude is None:
            raise ValueError("latitude value must be provided")
        lat = float(latitude)
        if lat < -90 or lat > 90:
            raise ValueError("latitude must be between -90 and 90 to be valid")
        return lat

    def _validate_longitude(self, longitude):
        if longitude is None:
            raise ValueError("latitude value must be provided")
        long = float(longitude)
        if long < -180 or long > 180:
            raise ValueError("longitude must be between -180 and 180 to be valid")
        return long

    def _validate_altitude_meters(self, altitude):
        if altitude is None:
            raise ValueError("altitude_meters value must be provided")
        return float(altitude)

    def _validate_battery_percent(self, battery_percent):
        if battery_percent is None:
            return
        bat_per = float(battery_percent)
        if bat_per < 0 or bat_per > 100:
            raise ValueError("battery_percent must be between 0 and 100 to be valid")
        return bat_per


data_1 = {
    "flight_id": "FS-2025-001",
    "timestamp": "2025-11-02T10:30:45Z",
    "latitude": 37.7749,
    "longitude": -122.4194,
    "altitude_meters": 120.5,
    "battery_percent": 85,
}


def test_flight_serializer(data):
    x = FlightSerializer(FlightDBConnection)
    success = x.validate_data(data)
    print(success)
    return


test_flight_serializer(data_1)

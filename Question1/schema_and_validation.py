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
import sqlite3


class DroneDBConnection:
    def __init__(self):
        self.open()

        # drop current Drone and Location tables if present
        # create Drone and Location tables with feilds listed in classes below
        # confirm tables were created
        self.close()

    def open(self):
        self.db_connection = sqlite3.connect('drone_data.db')
        self.cursor = self.db_connection.cursor()

    def close(self):
        self.db_connection.close()


class DroneDataSerializer(DroneDBConnection):

    def validate_data(self, models):
        """Ensure all data is serialized correctly for saving in db. Handle serialization failures."""
        # get all the model feilds and their restraints
        # does the json match the model feilds? Yes-> return true, No-> return list of additional or missing felids
        # do all the feilds meet their restraint reqs? Yes -> return true, No -> return list of errors
        pass

    def validate_lat_and_long(self, lat, long):
        """Validates the lat and long as being accurate"""
        pass

    def save(self, validated_data):
        """Saves validated data to the database and returns success or failure message"""

        self.open()
        try:
            # Create rows in tables with validated_data
            self.cursor.execute("""INSERT INTO DRONE VALUES ()""")
            self.cursor.execute("""INSERT INTO LOCATION VALUES ()""")

            self.db_connection.commit()

        except Exception as e:
            raise (f"Failed to save data: {validated_data}, error: {e}")

        self.close()
        return True

# class Drone:
#     def __init__(self, id, flight_id, location_id,):
#         self.id = id
#         self.flight_id = flight_id
#         self.location_id = location_id


# class Location:
#     def __init__(self,
#                  id,
#                  long: int,
#                  lat: int,
#                  time_stamp: datetime,
#                  altitude_meters: int,
#                  battery_percent: int
#                  ):
#         self.id = id
#         self.long = long
#         self.lat = lat
#         self.time_stamp = time_stamp
#         self.altitude_meters = altitude_meters
#         self.battery_percent = battery_percent

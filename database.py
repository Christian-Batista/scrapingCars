import mysql.connector
from mysql.connector import Error
from config import DATABASE_CONFIG

class database:
    def __init__(self):
        "Initialize the database connection"
        self.connection = None
        try:
            print("⏳ Connecting to MySQL database...")
            # CONNECT TO DATABASE
            self.connection = mysql.connector.connect(**DATABASE_CONFIG)
            # CREATE CURSOR
            self.cursor = self.connection.cursor(dictionary=True)
            print("✅ Connected to MySQL database")
        except Error as e:
            print(f"❌ Error connecting to MySQL database: {e}")

    def execute_query(self, query, params=None):
        "Execute a query on the database"
        try:
            self.cursor.execute(query, params or ())
            self.connection.commit()
            print("✅ Query executed successfully")
            return self.cursor.lastrowid
        except Error as e:
            print(f"❌ Error executing query: {e}")
            return None
        
    def fetch_all(self, query, params=None):
        "Fetch all rows from the database"
        try:
            self.cursor.execute(query, params or ())
            result = self.cursor.fetchall()
            print("✅ Query fetched successfully")
            return result
        except Error as e:
            print(f"❌ Error fetching data: {e}")
            return None
        
    def fetch_query(self, query, params=None):
        "Fetch data from the database"
        try:
            self.cursor.execute(query, params or ())
            result = self.cursor.fetchall()
            print("✅ Query fetched successfully")
            return result
        except Error as e:
            print(f"❌ Error fetching data: {e}")
            return None
        
    def close(self):
        "Close the database connection"
        try:
            self.cursor.close()
            self.connection.close()
            print("✅ Connection closed")
        except Error as e:
            print(f"❌ Error closing connection: {e}")

if __name__ == "__main__":
    db = database()
    db.close()
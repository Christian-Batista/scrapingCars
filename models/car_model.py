from database import database

class CarModel:
    def __init__(self):
        self.db = database

    def save_car(self, reference_id, brand, model, year, price, source, page):
        """Save a car to the database"""
        query = "INSERT INTO cars (reference_id, brand, model, year, price, source, page) VALUES (%s, %s, %s, %s, %s, %s, %s)"
        params = (reference_id, brand, model, year, price, source, page)
        return self.db.execute_query(query, params)
    
    def get_cars(self):
        """Get all cars from the database"""
        query = "SELECT * FROM vehicles"
        return self.db.fetch_all(query)
    
    def get_filtered_cars(self, brand, model, year):
        """Get cars filtered by brand, model, and year"""
        query = "SELECT * FROM vehicles WHERE brand = %s AND model = %s AND year = %s"
        params = (brand, model, year)
        return self.db.fetch_all(query, params)
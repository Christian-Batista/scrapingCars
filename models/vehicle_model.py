from database import database

class VehicleModel:
    def __init__(self):
        self.db = database()

    def save_car(self, brand, model, year, price, url, image_url,  fuel_type, source, page_number):
        """
        Save a car to the database.
        Args:
            reference_id (str): The reference ID of the car.
            brand (str): The brand of the car.
            model (str): The model of the car.
            year (str): The year of the car.
            price (str): The price of the car.
            url (str): The URL of the car.
            image_url (str): The image URL of the car.
            fuel_type (str): The fuel type of the car.
            car_condition (str): The condition of the car.
            source (str): The source of the car.
            page (int): The page number of the car.
        """
        query = "INSERT INTO vehicles (brand, model, year, price, url, image_url, source, page_number, fuel_type) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)"
        params = (brand, model, year, price, url, image_url, source, page_number, fuel_type)
        return self.db.execute_query(query, params)
    
    def get_cars(self):
        """Get all cars from the database"""
        query = "SELECT * FROM vehicles"
        return self.db.fetch_all(query)
    
    def get_filtered_cars(self, brand, model, year):
        """
        Get cars filtered by brand, model, and year.
        Args:
            brand (str): The brand of the car.
            model (str): The model of the car.
            year (str): The year of the car.
        """
        query = "SELECT * FROM vehicles WHERE brand = %s AND model = %s AND year = %s"
        params = (brand, model, year)
        return self.db.fetch_all(query, params)
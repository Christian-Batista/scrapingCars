from database import database

class VehicleModel:
    def __init__(self):
        self.db = database()

    def save(self, brand, model, year, price, url, image_url,  fuel_type, source, page_number):
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
        query = "SELECT * FROM vehicles WHERE 1=1"
        params = []
        if brand:
            query += " AND LOWER(brand) = LOWER(%s) AND status != 'inactive'"
            params.append(brand)
        if model:
            query += " AND LOWER(model) like LOWER(%s) AND status != 'inactive'"
            params.append(f"%{model}%")
        if year:
            query += " AND year like LOWER(%s) AND status != 'inactive'"
            params.append(f"%{year}%")

        return self.db.fetch_all(query, params)
    
    def get_cars_by_id(self, id):
        """
        Get car details by car ID.
        Args:
            id (int): The ID of the car.
        Returns:
            dict: A dictionary containing car details if found, otherwise None.
        """
        query = "SELECT * FROM vehicles WHERE id = %s"
        params = (id,)
        return self.db.fetch_query(query, params)
    
    
from models.vehicle_model import VehicleModel
from services.image_service import ImageService

class VehicleService:
    def __init__(self):
        # create vehicle model
        self.vehicle_model = VehicleModel()
        # create image service
        self.image_service = ImageService()
        # load urls from database
        self.existing_urls = self._load_existing_urls()

    def save_vehicle(self, cars):
        """
        Save the cars data in a database.
        """
        futures = []
        for car in cars:
            try:
                 # Check if the vehicle already exists
                if car["url"] not in self.existing_urls:
                    # Vehicle does not exist, so we save it
                    self._process_and_save_vehicle(car=car)
                else:
                    # Vehicle already exists, so we do nothing
                    print(f"✅ Vehicle already exists: {car['url']}")
            except Exception as e:
                print(f"❌ Error saving vehicle: {e}")

    def _process_and_save_vehicle(self, car):
        try:
            # Save the image
            car["image_url"] = self.image_service.save_image(car["image_url"])
            # Save the car
            self.vehicle_model.save(**car)
            # Add the new URL to the set of existing URLs
            self.existing_urls.add(car["url"])
            print(f"✅ Vehicle saved: {car['url']}")
        except Exception as e:
            print(f"❌ Error saving vehicle: {e}")
    
    def mark_vehicle_inactive(self, url):
        """
        Mark the vehicle as inactive in the database.
        """
        try:
            # Check if the URL exists before marking it as inactive
            if url in self.existing_urls:
                query = "UPDATE vehicles SET status = 'inactive' WHERE url = %s"
                params = (url,)
                self.vehicle_model.execute_query(query=query, params=params)
                print(f"✅ Vehicle marked as inactive: {url}")
            else:
                print(f"❌ Vehicle not found: {url}")
        except Exception as e:
            print(f"❌ Error marking vehicle as inactive: {e}")

    def _load_existing_urls(self):
        """
        Load all existing URLs from the database into a set for fast lookup.
        """
        try:
            query = "SELECT url FROM vehicles"
            vehicles = self.vehicle_model.db.fetch_all(query)
            return {vehicle['url'] for vehicle in vehicles}
        except Exception as e:
            print(f"❌ Error loading existing URLs: {e}")
            return set()  # Return an empty set if there's an error
    
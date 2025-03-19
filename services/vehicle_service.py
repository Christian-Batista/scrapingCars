from models.vehicle_model import VehicleModel
from services.image_service import ImageService

class VehicleService:
    def __init__(self):
        self.vehicle_model = VehicleModel()
        self.image_service = ImageService()
        # load urls from database
        self.existing_urls = self._load_existing_urls()

def save_vehicle(self, cars):
    """
    Save the cars data in a database.
    """
    for car in cars:
        try:
            # Check if the vehicle already exists
            if car["url"] not in self.existing_urls:
                # Save the image
                car["image_url"] = self.image_service.save_image(car["image_url"])
                # Save the car
                self.vehicle_model.save(**car)
                # Add the new URL to the set of existing URLs
                self.existing_urls.add(car["url"])
            else:
                # Vehicle already exists, so we do nothing
                print(f"✅ Vehicle already exists: {car['url']}")
        except Exception as e:
            print(f"❌ Error saving vehicle: {e}")
    
    def mark_vehicle_inactive(self, url):
        """
        Mark the vehicle as inactive in the database.
        """
        query = "UPDATE vehicles SET status = 'inactive' WHERE url = %s"
        params = (url,)
        result =  self.vehicle_model.execute_query(query=query, params=params)

    def _load_existing_urls(self):
        """
        Load existing URLs from the database.
        """
        query = "SELECT url FROM vehicles"
        vehicles = self.vehicle_model.db.fetch_all(query)
        return {vehicle['url'] for vehicle in vehicles}
    
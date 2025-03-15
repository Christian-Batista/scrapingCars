from models.vehicle_model import VehicleModel
from services.image_service import ImageService

class VehicleService:
    def __init__(self):
        self.vehicle_model = VehicleModel()
        self.image_service = ImageService()

    def save_vehicle(self, cars):
        """
        Save the cars data in a database.
        """
        for car in cars:
            try:
                car["image_url"] = self.image_service.save_image(car["image_url"])
                self.vehicle_model.save(**car)
            except Exception as e:
                print(f"❌ Error saving vehicle: {e}")
import os
import requests
from urllib.parse import urlparse, parse_qs

class ImageService:
    IMAGES_DIR = "images/vehicles"

    def __init__(self):
        os.makedirs(self.IMAGES_DIR, exist_ok=True)

    def save_image(self, image_url):
        """
        Save an image to the images directory.
        Args:
            image_url (str): The URL of the image.
            vehicle_id (int): The ID of the vehicle.
        """
        try:
            response = requests.get(image_url)
            if response.status_code == 200:
                # parse the image url
                parse_url = urlparse(image_url)
                # get the correct filename
                query_params = parse_qs(parse_url.query)
                # create a unique filename
                filename = query_params.get("id", [""])[0]
                if not filename:
                    filename = os.path.basename(parse_url.path)
                if not filename.endswith(".jpg"):
                    filename += ".jpg"
                # create the file path
                file_path = os.path.join(self.IMAGES_DIR, filename)
                # save the image to the images directory
                with open(file_path, "wb") as file:
                    for chunk in response.iter_content(1024):
                        file.write(chunk)
                return filename
            else:
                print(f"❌Failed to fetch image. Status code: {response.status_code}")
                return None
        except Exception as e:
            print(f"❌Error saving image: {e}")
            return None

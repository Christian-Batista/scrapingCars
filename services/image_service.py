import os
import time
import requests
import requests.exceptions
from urllib.parse import urlparse
from config import IMAGES_PATH

class ImageService:
    def __init__(self):
        self.IMAGES_PATH = IMAGES_PATH
        os.makedirs(self.IMAGES_PATH, exist_ok=True)

    def save_image(self, image_url):
        """
        Save an image to the images directory.
        Args:
            image_url (str): The URL of the image.
        Returns:
            str: The filename of the saved image, or None if there was an error.
        """
        if not image_url:
            print("❌ Image URL is empty or None")
            return None

        try:
            response = requests.get(image_url)
            response.raise_for_status()
        except requests.exceptions.RequestException as e:
            print(f"❌ Error fetching image: {e}")
            return None

        try:
            # Parse the image URL
            parse_url = urlparse(image_url)
            # Get the filename from the URL path
            filename = os.path.basename(parse_url.path)
            # If the filename is empty, generate a unique name
            if not filename:
                filename = f"image_{int(time.time())}.jpg"
            # Ensure the filename has a valid extension
            if not filename.lower().endswith(('.jpg', '.jpeg', '.png', '.gif')):
                filename += ".jpg"
            # Create the file path
            file_path = os.path.join(self.IMAGES_PATH, filename)
            # Save the image to the images directory
            with open(file_path, "wb") as file:
                for chunk in response.iter_content(1024):
                    file.write(chunk)
            return filename
        except IOError as e:
            print(f"❌ Error saving image to disk: {e}")
            return None
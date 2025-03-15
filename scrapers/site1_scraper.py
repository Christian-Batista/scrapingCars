"""
En esta pagina se extrae informcaion de la pagina carrosrd.com
"""
import requests
from bs4 import BeautifulSoup
from models.vehicle_model import VehicleModel

# Define the URL
url = "https://carrosrd.com/carros"

def scrape_site1():
    """
    Scrape car data from carrosrd.com.
    This function scrapes the website and returns a list of dictionaries containing the car data.
    """

    # define the user agent
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.142.86 Safari/537.36"
    }

    # List to store all cars data
    all_cars = []

    # make a request to the URL to get the HTML content of the first 10 pages
    for i in range(1, 11):
        # make a request to the URL
        response = requests.get(f"{url}?p={i}", headers=headers)
        # check if the request was successful
        if response.status_code != 200:
            return {"error": f"Failed to fetch data. Status code: {response.status_code}"}
        # parse the HTML content
        soup = BeautifulSoup(response.content, "html.parser")

        # container for the cars
        cars_container = soup.find("div", {"class": "container-car"})

        # loop through the cars and extract the information
        for car in cars_container.find_all("div", {"class": "car"}):
            # Extract the url reference
            a_tag = car.find("a")
            url_reference = a_tag.get("href") if a_tag else "No URL"
            # Extract the title (which contains the brand and model)
            title = car.find("span", {"class": "title"}).text.strip()
            
            # Extract the image url
            image_url = car.find("img").get("src")
            # Extract the fuel type
            fuel_info = car.find("div", {"class": "dtil"}).text.strip()
            fuel_type = fuel_info.split('|')[0].strip()

            # Split the title into brand and model
            brand_model = title.split()
            brand = brand_model[0]
            model = " ".join(brand_model[1:])

            # Extract the year
            year = car.find("span", {"class": "uk-text-primary"}).text.strip()
            # Extract the price
            price = car.find("div", {"class": "price"}).text.strip()

            # append the car data to the list
            all_cars.append({
                "brand": brand,
                "model": model,
                "year": year,
                "price": price,
                "url": url_reference,
                "image_url": image_url,
                "fuel_type": fuel_type,
                "source": "carrosrd.com",
                "page_number": i
            })

    return all_cars
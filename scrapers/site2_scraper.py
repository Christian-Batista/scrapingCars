"""
En esta pagina se extrae informcaion de la pagina supercarros.com
"""
import requests
from bs4 import BeautifulSoup
from  models.vehicle_model import VehicleModel

# Define the URL
url = "https://www.supercarros.com/carros/"

def scrape_site2():
    """
    Scrape car data from supercarros.com
    """

    # define the user agent
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.142.86 Safari/537.36"
    }

    # List to store all cars data
    all_cars = []

    # make a request to the URL to get the HTML content of the first 10 pages
    for i in range(1, 11):
        print(url)

        response = requests.get(f"{url}?PagingPageSkip={i}", headers=headers)

        if response.status_code != 200:
            return {"error": f"Failed to fetch data. Status code: {response.status_code}"}
    
        soup = BeautifulSoup(response.content, "html.parser")

        # container for the cars
        cars_container = soup.find("div", {"id": "bigsearch-results-inner-results"})

        # loop through the cars and extract the information
        for car in cars_container.find_all("li", {"class": "normal"}):
            # Extract the url reference
            url_info = car.find("a")["href"]
            url_reference = "https://www.supercarros.com" + url_info
            # Extract the title (which contains the brand and model)
            title = car.find("div", {"class": "title1"}).text.strip()

            # Extract image url
            image_url = car.find("img", {"class": "real"})["src"]
            print(image_url)

            # Extract the fuel type
            fuel_info = car.find("div", {"class": "title2"}).text.strip()
            fuel_type = fuel_info.split("-")[1].strip()

            # Split the title into brand and model
            brand_model = title.split()
            brand = brand_model[0]
            model = " ".join(brand_model[1:])

            # Extract the year
            year = car.find("div", {"class": "year"}).text.strip()
            # Extract the price
            price = car.find("div", {"class": "price"}).text.strip()

            # append the car data to the list
            all_cars.append({
                "brand": brand,
                "model": model,
                "year": year,
                "price": price,
                "source": "supercarros.com",
                "url": url_reference,
                "image_url": image_url,
                "fuel_type": fuel_type,
                "page_number": i
            })

    # save the cars to the database
    vehicle_model = VehicleModel()
    for car in all_cars:
        vehicle_model.save_car(**car)

    return all_cars
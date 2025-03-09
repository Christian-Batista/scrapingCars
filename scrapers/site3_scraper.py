import requests
from bs4 import BeautifulSoup
from models.vehicle_model import VehicleModel

# Define the URL
url = "https://montao.do/searchvehiculo.php"

def scrape_site3():
    """
    Scrape car data from montao.do
    """

    # define the user agent
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.142.86 Safari/537.36"
    }

    # List to store all cars data
    all_cars = []

    # make a request to the URL to get the HTML content of the first 10 pages
    for i in range(1, 11):
        response = requests.get(f"{url}?page={i}", headers=headers)

        if response.status_code != 200:
            return {"error": f"Failed to fetch data. Status code: {response.status_code}"}
    
        soup = BeautifulSoup(response.content, "html.parser")

        # container for the cars
        cars_items = soup.find_all("div", {"class": "listing-grid-item"})

        # loop through the cars and extract the information
        for car in cars_items:
            try:
                # Extract the title (which contains the brand and model)
                title_element = car.find("h6", {"class": "title"})
                # Extract the url reference
                url_reference = "https://montao.do/" + title_element.find("a")["href"]
                # Extract image url
                image_url = car.find("div", {"class": "wrap-hover-listing"}).find("img")["src"]


                title = title_element.text.strip() if title_element else ""
                # Extract the fuel type
                fuel_type = car.find("div", {"class": "inner"}).find("p").text.strip()

                # Verify if title isn't empty before the split
                if title:
                    brand_model = title.split()

                    # Verificar que hay al menos un elemento antes de acceder a índices
                    if len(brand_model) >= 3:
                        brand = brand_model[0]
                        model = " ".join(brand_model[1:-1])
                        last_element = brand_model[-1]

                        # Verify that the year is a number
                        if last_element.isdigit() and len(last_element) == 4:
                            year = last_element

                    elif len(brand_model) == 2:
                        brand = brand_model[0]
                        model = brand_model[1]
                        year = 1
                

                # Extract the price
                price_element = car.find("p", {"class": "price-sale"})
                price = price_element.text.strip() if price_element else 1

                # append the car data to the list
                all_cars.append({
                    "brand": brand,
                    "model": model,
                    "year": year,
                    "price": price,
                    "url": url_reference,
                    "image_url": image_url,
                    "fuel_type": fuel_type,
                    "source": "montao.do",
                    "page_number": i
                })
            except AttributeError as e:
                # Handle cases where some fields are missing
                print(f"Error extracting data for a car: {e}")
                continue

    # Save the data to database
    vehicle_model = VehicleModel()
    for car in all_cars:
        vehicle_model.save(**car)

    return all_cars
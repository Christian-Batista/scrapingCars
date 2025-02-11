import requests
from bs4 import BeautifulSoup

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
                title_element = car.find("h6", {"class": "title"}).text.strip()
                title = title_element.text.strip() if title_element else ""

                # Verify if title isn't empty before the split
                if title:
                    brand_model = title.split()

                    # Verificar que hay al menos un elemento antes de acceder a índices
                    if len(brand_model) >= 3:
                        brand = brand_model[0]
                        model = " ".join(brand_model[1:-1])
                        year = brand_model[-1]
                    elif len(brand_model) == 2:
                        brand = brand_model[0]
                        model = brand_model[1]
                        year = "Unknown"
                    elif len(brand_model) == 1:
                        brand = brand_model[0]
                        model, year = "Unknown", "Unknown"
                    else:
                        brand, model, year = "Unknown", "Unknown", "Unknown"
                else:
                    brand, model, year = "Unknown", "Unknown", "Unknown"
                

                # Extract the price
                price_element = car.find("p", {"class": "price-sale"})
                price = price_element.text.strip() if price_element else "Unknown"

                # append the car data to the list
                all_cars.append({
                    "brand": brand,
                    "model": model,
                    "year": year,
                    "price": price,
                    "source": "montao.do",
                    "page": i
                })
            except AttributeError as e:
                # Handle cases where some fields are missing
                print(f"Error extracting data for a car: {e}")
                continue

    return all_cars


if __name__ == "__main__":
    cars = scrape_site3()
    print(cars)
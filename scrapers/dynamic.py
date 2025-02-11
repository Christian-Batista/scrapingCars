from selenium import webdriver
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
import time

def scrape_site3_with_selenium():
    # Configura el navegador
    driver = webdriver.Chrome()

    # List to store all cars data
    all_cars = []

    # make a request to the URL to get the HTML content of the first 10 pages
    for i in range(1, 11):
        driver.get(f"https://montao.do/searchvehiculo.php?page={i}")

        # Espera a que el contenido se cargue
        time.sleep(5)  # Ajusta este tiempo según sea necesario

        # Obtén el HTML renderizado
        html = driver.page_source
        soup = BeautifulSoup(html, "html.parser")

        # container for the cars
        cars_items = soup.find_all("div", {"class": "listing-grid-item"})

        # loop through the cars and extract the information
        for car in cars_items:
            try:
                # Extract the title (which contains the brand and model)
                title = car.find("h6", {"class": "title"}).text.strip()

                # Split the title into brand and model
                brand_model = title.split()
                brand = brand_model[0]
                model = " ".join(brand_model[1:-1])  # Excluye la última palabra (el año)

                # Extract the year (última palabra del título)
                year = brand_model[-1] if len(brand_model) > 1 else "Unknown"

                # Extract the price
                price = car.find("p", {"class": "price-sale"}).text.strip()

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

    # Cierra el navegador
    driver.quit()

    return all_cars


if __name__ == "__main__":
    cars = scrape_site3_with_selenium()
    print(cars)
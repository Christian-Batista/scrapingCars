import re
import requests
from bs4 import BeautifulSoup

def get_year(titulo):
    """
    Extrae el año del título si existe, de lo contrario, devuelve 1.
    """
    match = re.search(r'\b(19|20)\d{2}\b', titulo)  # Busca años entre 1900-2099
    return int(match.group()) if match else 1  # Si encuentra, devuelve el año, sino 1

def scrape_site3():
    url = "https://montao.do/searchvehiculo.php"
    headers = {"User-Agent": "Mozilla/5.0"}
    all_cars = []

    for i in range(1, 11):
        response = requests.get(f"{url}?page={i}", headers=headers)
        if response.status_code != 200:
            return {"error": f"Failed to fetch data. Status code: {response.status_code}"}

        soup = BeautifulSoup(response.content, "html.parser")
        cars_items = soup.find_all("div", {"class": "listing-grid-item"})

        for car in cars_items:
            try:
                title_element = car.find("h6", {"class": "title"})
                title = title_element.text.strip() if title_element else ""
                
                url_reference = "https://montao.do/" + title_element.find("a")["href"]
                image_url = car.find("div", {"class": "wrap-hover-listing"}).find("img")["src"]
                fuel_type = car.find("div", {"class": "inner"}).find("p").text.strip()

                # Extraer año con la función obtener_anio()
                year = get_year(title)

                # Separar marca y modelo eliminando el año
                brand_model = re.sub(r'\b(19|20)\d{2}\b', '', title).strip().split()
                
                if len(brand_model) >= 2:
                    brand = brand_model[0]
                    model = " ".join(brand_model[1:])
                else:
                    brand, model = title, ""

                price_element = car.find("p", {"class": "price-sale"})
                price = price_element.text.strip() if price_element else "1"

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
                print(f"Error extracting data for a car: {e}")
                continue

    return all_cars

import sys
import os
import threading

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from scrapers import site1_scraper, site2_scraper, site3_scraper
from services.vehicle_service import VehicleService

# Variables to store the results
results = {
    "site1": [],
    "site2": [],
    "site3": []
}

def scraper1():
    """
    Function to scrape carrosrd.com
    """
    print("🚀 Starting scraper for carrosrd.com")
    data = site1_scraper.scrape_site1()
    if isinstance(data, dict) and "error" in data:
        print(f"Error scraping carrosrd.com: {data['error']}")
    else:
        results["site1"] = data
    print("✅ Scraper carrosrd.com finished")

def scraper2():
    """
    Function to scrape supercarros.com
    """
    print("🚀 Starting scraper for supercarros.com")
    data = site2_scraper.scrape_site2()
    if isinstance(data, dict) and "error" in data:
        print(f"Error scraping supercarros.com: {data['error']}")
    else:
        results["site2"] = data
    print("✅ Scraper supercarros.com finished")

def scraper3():
    """
    Function to scrape montao.do
    """
    print("🚀 Starting scraper for montao.do")
    data = site3_scraper.scrape_site3()
    if isinstance(data, dict) and "error" in data:
        print(f"Error scraping montao.do: {data['error']}")
    else:
        results["site3"] = data
    print("✅ Scraper montao.do finished")

def scrape_all_sites():
    # Create threads
    thread1 = threading.Thread(target=scraper1)
    thread2 = threading.Thread(target=scraper2)
    thread3 = threading.Thread(target=scraper3)

    # Start threads
    thread1.start()
    thread2.start()
    thread3.start()

    # Wait for threads to finish
    thread1.join()
    thread2.join()
    thread3.join()

    # Combine the results
    all_cars = results["site1"] + results["site2"] + results["site3"]

    # Store the data
    vehicle_service = VehicleService()
    vehicle_service.save_vehicle(all_cars)

    return all_cars


if __name__ == "__main__":
    all_cars_data = scrape_all_sites()
    print(f"🚗 Total de autos obtenidos: {len(all_cars_data)}")

import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from scrapers import site1_scraper, site2_scraper, site3_scraper
from services.vehicle_service import VehicleService

def scrape_all_sites():
    """
    Call all scraper functions and combine their results.
    """
    cars_site1 = site1_scraper.scrape_site1()
    cars_site2 = site2_scraper.scrape_site2()
    cars_site3 = site3_scraper.scrape_site3()

    # Check if any scraper returned an error
    if isinstance(cars_site1, dict) and "error" in cars_site1:
        print(f"Error scraping site 1: {cars_site1['error']}")
        cars_site1 = []
    
    if isinstance(cars_site2, dict) and "error" in cars_site2:
        print(f"Error scraping site 2: {cars_site2['error']}")
        cars_site2 = []
    
    if isinstance(cars_site3, dict) and "error" in cars_site3:
        print(f"Error scraping site 3: {cars_site3['error']}")
        cars_site3 = []

    # Combine the results
    cars = cars_site1 + cars_site2 + cars_site3

    # Use the service to save in tha database
    vehice_service = VehicleService()
    vehice_service.save_vehicle(cars)
    return cars
    

if __name__ == "__main__":
    all_cars_data = scrape_all_sites()
    print(all_cars_data)
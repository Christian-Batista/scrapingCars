from scrapers import site1_scraper, site2_scraper, site3_scraper

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

    # Combine all lists into one
    all_cars = cars_site1 + cars_site2 + cars_site3
    return all_cars

if __name__ == "__main__":
    all_cars_data = scrape_all_sites()
    print(all_cars_data)
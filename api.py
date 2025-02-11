from fastapi import FastAPI, Query
from scraper_service import scrape_all_sites

app = FastAPI()

# Cache para almacenar los datos luego de la primera solicitud
cached_cars = None

@app.get("/cars")
def get_cars(
    brand: str = Query(None, description="Filter by car brand"),
    model: str = Query(None, description="Filter by car model"),
    year: str = Query(None, description="Filter by car year")
):
    """
    Endpoint to fetch all cars with optional filters for brand, model, and year.
    Uses cached data after the first request.
    """
    global cached_cars

    # Si cached_cars es None, hacer scraping
    if cached_cars is None:
        print("⏳ Fetching data for the first time, please wait...")
        cached_cars = scrape_all_sites()
        print("✅ Data successfully scraped and stored in cache!")

    # Aplicar filtros si hay parámetros
    filtered_cars = cached_cars
    if brand:
        filtered_cars = [car for car in filtered_cars if car["brand"].lower() == brand.lower()]
    if model:
        filtered_cars = [car for car in filtered_cars if model.lower() in car["model"].lower()]
    if year:
        filtered_cars = [car for car in filtered_cars if car["year"] == year]

    return {"total": len(filtered_cars), "cars": filtered_cars}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)

from fastapi import FastAPI, HTTPException, Query
from fastapi.staticfiles import StaticFiles
from models.vehicle_model import VehicleModel
from config import IMAGES_PATH
import math

app = FastAPI()

# Mount the static files directory
app.mount("/static", StaticFiles(directory=IMAGES_PATH), name="static")

@app.get("/cars")
def get_cars(
    brand: str = Query(None, description="Filter by car brand"),
    model: str = Query(None, description="Filter by car model"),
    year: str = Query(None, description="Filter by car year"),
    page: int = Query(1, description="Page number"),
    limit: int = Query(10, description="Number of items per page"),
):
    """
    Endpoint to fetch all cars with optional filters for brand, model, and year.
    """
    try:
        # Create a VehicleModel instance
        vehicle_model = VehicleModel()

        # Get filtered cars
        if brand or model or year:
            filtered_cars = vehicle_model.get_filtered_cars(brand, model, year)
        else:
            filtered_cars = vehicle_model.get_cars()

        # Apply pagination
        start = (page - 1) * limit
        end = start + limit
        paginated_cars = filtered_cars[start:end]

        # Convert cars to a list of dictionaries
        cars_data = [
            {
                "brand": car["brand"],
                "model": car["model"],
                "year": car["year"],
                "price": car["price"],
                "url": car["url"],
                "image_url": f"http://0.0.0.0:8000/static/{car['image_url']}",
                "fuel_type": car["fuel_type"],
                "source": car["source"],
                "page_number": car["page_number"],
                "status": car["status"],
            }
            for car in paginated_cars
        ]

        # here I have to calculate the total number of cars
        total_pages = math.ceil(len(filtered_cars) / limit)

        return {
            "total": len(filtered_cars),
            "page": page,
            "limit": limit,
            "total_pages": total_pages,
            "cars": cars_data
        }
    
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
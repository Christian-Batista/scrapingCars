from celery import Celery
from services.scraper_service import scrape_all_sites


app = Celery('tasks', broker='redis://localhost:6379/0', backend='redis://localhost:6379/0')

@app.task
def test_task():
    # return "Hello from Celery!"
    all_cars_data = scrape_all_sites()
    print(all_cars_data)

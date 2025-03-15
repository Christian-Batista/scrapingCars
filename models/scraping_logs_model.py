from database import database

class ScrapingLogsModel:
    def __init__(self):
        self.db = database
    
    def save_log(self, resource, total_records):
        """"
        Save a scraping log to the database.
        Args:
            resource (str): The resource that was scraped.
            total_records (int): The total number of records that were scraped.
        """
        query = "INSERT INTO scraping_logs (resource, total_records) VALUES (%s, %s)"
        params = (resource, total_records)
        return self.db.execute_query(query, params)
    
    def get_logs(self):
        """Get all scraping logs from the database"""
        query = "SELECT * FROM scraping_logs"
        return self.db.fetch_all(query)
    
    def get_logs_by_resource(self, resource):
        """Get all scraping logs for a specific resource from the database"""
        query = "SELECT * FROM scraping_logs WHERE resource = %s"
        params = (resource,)
        return self.db.fetch_all(query, params)
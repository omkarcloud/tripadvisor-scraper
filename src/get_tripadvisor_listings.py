from botasaurus.task import task
from .tripadvisor import Tripadvisor

@task
def get_tripadvisor_listings(data):
    # Fixed the function calls by removing the trailing commas and improving the formatting
    if data['type'] == "hotel":
        return Tripadvisor.get_hotels(data["search_queries"], data["max_results"], data["api_key"], data["enable_detailed_extraction"])
    elif data['type'] == "restaurant":
        return Tripadvisor.get_restaurants(data["search_queries"], data["max_results"], data["api_key"], data["enable_detailed_extraction"])
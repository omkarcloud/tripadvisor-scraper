import re
from botasaurus_server.server import Server
from src.get_tripadvisor_listings import get_tripadvisor_listings
from botasaurus_server.ui import (
    filters,
    sorts,
)

def clean_search_string(s):
    if isinstance(s, str):
        return re.sub(r"\s+", " ", s.strip().lower())    


# split_task accepts a data dictionary and returns a list of URLs for each task.
def split_task(data):
    tasks = []
    for query in data['search_queries']:
        task = data.copy()
        task['search_queries'] = clean_search_string(query)
        tasks.append(task)
    return tasks

def get_task_name(data):
    return  data["type"][:1].upper() + data["type"][1:] + "s in " + data["search_queries"]

Server.add_scraper(
    get_tripadvisor_listings,
    split_task=split_task,
    get_task_name=get_task_name,
    filters=[
        filters.SearchTextInput("name"),
        filters.MinNumberInput("reviews", label="Min Reviews"),
        filters.MaxNumberInput("reviews", label="Max Reviews"),
    ],
    sorts=[
        sorts.NumericDescendingSort("reviews"),
        sorts.NumericAscendingSort("reviews"),
        sorts.AlphabeticAscendingSort("name"),
    ],
)

Server.set_rate_limit(task=1)

Server.configure(
    title="Tripadvisor Scraper",
    header_title="Made with Botasaurus",
    description="Tripadvisor Scraper helps you collect Hotels and Restaurants from Tripadvisor.",
    right_header={
        "text": "Love It? Star It! ★",
        "link": "https://github.com/omkarcloud/tripadvisor-scraper",
    },
)
from botasaurus.cache import DontCache
from .helpers import convert_unicode_dict_to_ascii_dict
from botasaurus.task import task
from time import sleep
from .utils import default_request_options
import requests

FAILED_DUE_TO_CREDITS_EXHAUSTED = "FAILED_DUE_TO_CREDITS_EXHAUSTED"
FAILED_DUE_TO_NOT_SUBSCRIBED = "FAILED_DUE_TO_NOT_SUBSCRIBED"
FAILED_DUE_TO_NO_KEY = "FAILED_DUE_TO_NO_KEY"
FAILED_DUE_TO_UNKNOWN_ERROR = "FAILED_DUE_TO_UNKNOWN_ERROR"


def do_request(data, retry_count=3):
    params = data["params"]
    key = data["key"]
    endpoint = data["endpoint"]

    if retry_count == 0:
        print(f"Failed to get data, after 3 retries")
        return DontCache(None)

    rapidapi = "https://tripadvisor-scraper.p.rapidapi.com/"
    # rapidapi = "http://127.0.0.1:5000/"
    url = rapidapi + endpoint.rstrip("/").lstrip(
        "/"
    )
    querystring = params
    headers = {
        "X-RapidAPI-Key": key,
        "X-RapidAPI-Host": "tripadvisor-scraper.p.rapidapi.com",
    }
    try:
      response = requests.get(url, headers=headers, params=querystring)
      response_data = response.json()
    except Exception as e:
        return DontCache({"data": None, "error": str(e)})
    
    
    if response.status_code == 200 or response.status_code == 404:
        if isinstance(response_data, dict):
            message = response_data.get("message", "")
            if "API doesn't exists" in message:
                return DontCache({"data": None, "error": FAILED_DUE_TO_UNKNOWN_ERROR})
        if response.status_code == 404:
            print(f"Not Found for ", data, response_data )
            return DontCache({"data": None, "error": response_data.get("message", "")})
        return {
            "data": convert_unicode_dict_to_ascii_dict(response_data),
            "error": None,
        }
    else:
        message = response_data.get("message", "")
        if "exceeded the MONTHLY quota" in message:
            return DontCache({"data": None, "error": FAILED_DUE_TO_CREDITS_EXHAUSTED})
        elif (
            "exceeded the rate limit per second for your plan" in message
            or "many requests" in message
        ):
            sleep(2)
            return do_request(data, retry_count - 1)
        elif "You are not subscribed to this API." in message:

            return DontCache({"data": None, "error": FAILED_DUE_TO_NOT_SUBSCRIBED})

        print(f"Error: {response.status_code}", response_data)
        return DontCache(
            {
                "data": None,
                "error": FAILED_DUE_TO_UNKNOWN_ERROR,
            }
        )


@task(**default_request_options, parallel=5, cache=True)
def get_listings(data: dict, metadata):
    if not metadata.get("key"):
        return DontCache({"data": None, "error": FAILED_DUE_TO_NO_KEY})

    data = {
        **metadata,
        "endpoint": data.pop("endpoint"),
        "params": data,
    }

    return do_request(
        data,
    )

# python -m src.tripadvisor.get_listings
if __name__ == "__main__":
    x = get_listings({'endpoint': '/hotels/detail', 'id': "208453"}, metadata={"key":"e78ae5d201mshf878ec8fec0a188p12c911jsn78c12c161b78"})
    print(x)
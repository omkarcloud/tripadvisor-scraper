![TripAdvisor Scraper Featured Image](https://raw.githubusercontent.com/omkarcloud/tripadvisor-scraper/master/tripadvisor-scraper-featured-image.png)

# TripAdvisor Scraper API

REST API to comprehensively get reviews, search hotels/restaurants/attractions, browse listings, and get hotel details from TripAdvisor. Detailed Data and Supports 45+ locales and 145+ currencies.

Get any TripAdvisor data via this well developed API.

## Key Features

- Get reviews with ratings, trip type, reviewer profiles, and photos
- Search and list hotels, restaurants, attractions, and cruises
- Get detailed property data (amenities, hours, pricing, photos, rating breakdowns)
- Filter by star rating, traveler type, date range, cuisine, and more
- Supports 45+ locales and 145+ currencies
- **1,000 requests/month on free tier**
- Example Response:
```json
{
  "review_id": "940716685",
  "title": "Great experience with the family",
  "text": "We visited in December and had an amazing time. The park was beautifully decorated for the holidays...",
  "rating": 5,
  "published_date": "2025-01-15",
  "trip_type": "Family",
  "travel_date": "2024-12",
  "url": "https://www.tripadvisor.com/ShowUserReviews-g29092-d103346-r940716685-Disneyland_Park.html",
  "user": {
    "username": "TravelMom2024",
    "review_count": 42,
    "location": "Los Angeles, CA"
  }
}
```

## Get API Key

Create an account at [omkar.cloud](https://www.omkar.cloud/auth/sign-up?redirect=/api-key) to get your API key.

It takes just 2 minutes to sign up. You get 1,000 free requests every month—more than enough for most users to get detailed TripAdvisor data without paying a dime.

This is a well built product, and your search for the best TripAdvisor Scraper API ends right here. 

## Quick Start

```bash
curl -X GET "https://tripadvisor-scraper-api.omkar.cloud/tripadvisor/hotels/search?query=Swissotel%20Chicago" \
  -H "API-Key: YOUR_API_KEY"
```

## Quick Start (Python)

```bash
pip install requests
```

```python
import requests

# Search for hotels
response = requests.get(
    f"{base_url}/hotels/search",
    params={"query": "Swissotel Chicago"},
    headers={"API-Key": api_key}
)

print(response.json())
```

## API Reference

### Hotel Search

```
GET https://tripadvisor-scraper-api.omkar.cloud/tripadvisor/hotels/search
```

#### Parameters

| Parameter | Required | Default | Description |
|-----------|----------|---------|-------------|
| `query` | Yes | — | Search text (e.g., `new york`, `Swissotel Chicago`). |
| `locale` | No | `en-US` | Localization code. |

#### Example

```python
import requests

response = requests.get(
    "https://tripadvisor-scraper-api.omkar.cloud/tripadvisor/hotels/search",
    params={"query": "new york"},
    headers={"API-Key": "YOUR_API_KEY"}
)

print(response.json())
```

#### Response

<details>
<summary>Sample Response (click to expand)</summary>

```json
{
  "count": 4,
  "results": [
    {
      "tripadvisor_entity_id": 60763,
      "name": "New York City",
      "link": "https://www.tripadvisor.com/Hotels-g60763-New_York_City_New_York-Hotels.html",
      "place_type": "CITY",
      "is_tripadvisor_entity": false,
      "featured_image": "https://dynamic-media-cdn.tripadvisor.com/media/photo-o/1c/c5/7c/68/caption.jpg",
      "coordinates": {
        "latitude": 40.713238,
        "longitude": -74.00584
      },
      "parent_location": {
        "tripadvisor_entity_id": 28953,
        "name": "New York"
      },
      "other_links": {
        "root": "https://www.tripadvisor.com/Tourism-g60763-New_York_City_New_York-Vacations.html",
        "attractions": "https://www.tripadvisor.com/Attractions-g60763-Activities-New_York_City_New_York.html",
        "restaurants": "https://www.tripadvisor.com/Restaurants-g60763-New_York_City_New_York.html",
        "hotels": "https://www.tripadvisor.com/Hotels-g60763-New_York_City_New_York-Hotels.html",
        "vacation_rentals": "https://www.tripadvisor.com/VacationRentals-g60763-Reviews-New_York_City_New_York-Vacation_Rentals.html"
      }
    },
    ...
  ]
}
```

</details>

---

### Hotel List

```
GET https://tripadvisor-scraper-api.omkar.cloud/tripadvisor/hotels/list
```

#### Parameters

| Parameter | Required | Default | Description |
|-----------|----------|---------|-------------|
| `query` | Yes | — | City name, TripAdvisor URL, or entity ID. |
| `page` | No | `1` | Page number (30 hotels per page). |
| `check_in_date` | No | — | Check-in date (`YYYY-MM-DD`). |
| `check_out_date` | No | — | Check-out date (`YYYY-MM-DD`). |
| `rooms` | No | `1` | Number of rooms. |
| `adults` | No | `2` | Number of adults. |
| `min_rating` | No | — | Minimum rating: `2`, `3`, `4`, `5`. |
| `is_5_star` | No | — | Filter for 5-star hotels: `true`, `false`. |
| `awards` | No | — | Filter: `travelers_choice`, `travelers_choice_best_of_the_best`. |
| `currency` | No | `USD` | Currency code. |
| `locale` | No | `en-US` | Localization code. |

#### Example

```python
import requests

response = requests.get(
    "https://tripadvisor-scraper-api.omkar.cloud/tripadvisor/hotels/list",
    params={"query": "new york", "page": "1"},
    headers={"API-Key": "YOUR_API_KEY"}
)

print(response.json())
```

#### Response

<details>
<summary>Sample Response (click to expand)</summary>

```json
{
  "count": 1005,
  "per_page": 30,
  "current_page": 1,
  "total_pages": 34,
  "next": "https://tripadvisor-scraper-api.omkar.cloud/hotels/list?query=60763&page=2",
  "previous": null,
  "results": [
    {
      "tripadvisor_entity_id": 23448880,
      "name": "Motto by Hilton New York City Chelsea",
      "link": "https://www.tripadvisor.com/Hotel_Review-g60763-d23448880-Reviews-Motto_by_Hilton_New_York_City_Chelsea-New_York_City_New_York.html",
      "description": "Modern NYC hotel with a central location and breathtaking views of landmarks like the Statue of Liberty and Empire State Building. Stylish, clean rooms with great amenities and comfortable beds. Highly rated bar, restaurant, and outdoor spaces. Friendly staff and excellent service.",
      "rating": 4.8,
      "reviews": 1758,
      "website": "https://www.tripadvisor.com/Commerce?p=TABAIndependentHotels&src=207825639&geo=23448880...",
      "phone": "1 (855) 605-0316",
      "email": null,
      "featured_image": "https://dynamic-media-cdn.tripadvisor.com/media/photo-o/31/be/a9/38/exterior.jpg",
      "award": {
        "award_name": "Travelers Choice",
        "year": 2025,
        "award_type": "travelers_choice"
      },
      "ranking": {
        "current_rank": 25,
        "total": 770,
        "text": "#23 of 517 hotels in New York City"
      },
      "hotel_class": 3.5,
      "hotel_styles": [
        {
          "name": "Business",
          "rank": 3,
          "rating": 4.66
        },
        {
          "name": "Modern",
          "rank": 4,
          "rating": 4.71
        },
        {
          "name": "City View",
          "rank": 4,
          "rating": 4.66
        }
      ],
      "address": "113 West 24th Street, New York City, NY 10001",
      "detailed_address": {
        "street1": "113 West 24th Street",
        "street2": null,
        "city": "New York City",
        "state": "New York",
        "country": "United States",
        "country_code": "US",
        "postal_code": "10001",
        "address": "113 West 24th Street, New York City, NY 10001"
      },
      "coordinates": {
        "latitude": 40.74406,
        "longitude": -73.99294
      },
      "price": 203,
      "price_range": {
        "min": 203,
        "max": 805
      },
      "containing_neighborhoods": [
        {
          "tripadvisor_entity_id": 15565668,
          "name": "Tenderloin"
        },
        {
          "tripadvisor_entity_id": 7102343,
          "name": "Chelsea"
        }
      ],
      "parent_location": {
        "tripadvisor_entity_id": 60763,
        "name": "New York City"
      },
      "booking_offers": null,
      "subratings": {
        "location": 4.72,
        "cleanliness": 4.62,
        "service": 4.78,
        "value": 4.54,
        "sleep_quality": 4.88,
        "rooms": 4.9,
        "food": 4.68
      },
      "review_snippet": {
        "review_id": 884782464,
        "title": "Great hotel, great location!",
        "snippet_text": "Hotel staff were friendly and eager to accommodate, bar/restaurant was comfy and fun and offered delicious options, and the room was clean and wonderfully modest.",
        "rating": 5
      },
      "is_ad": false
    },
    ...
  ],
  "suggested_hotels": []
}
```

</details>

---

### Hotel Details

```
GET https://tripadvisor-scraper-api.omkar.cloud/tripadvisor/hotels/detail
```

#### Parameters

| Parameter | Required | Default | Description |
|-----------|----------|---------|-------------|
| `query` | Yes | — | TripAdvisor Hotel URL, hotel name, or entity ID. |
| `locale` | No | `en-US` | Localization code. |

#### Example

```python
import requests

response = requests.get(
    "https://tripadvisor-scraper-api.omkar.cloud/tripadvisor/hotels/detail",
    params={"query": "114581"},
    headers={"API-Key": "YOUR_API_KEY"}
)

print(response.json())
```

#### Response Fields

Response redacted due to too long length. Please make an HTTP request to retrieve the full hotel details.

---

### Restaurant Search

```
GET https://tripadvisor-scraper-api.omkar.cloud/tripadvisor/restaurants/search
```

#### Parameters

| Parameter | Required | Default | Description |
|-----------|----------|---------|-------------|
| `query` | Yes | — | Search text (e.g., `new york`, `Piccola Cucina, New York`). |
| `locale` | No | `en-US` | Localization code. |

#### Example

```python
import requests

response = requests.get(
    "https://tripadvisor-scraper-api.omkar.cloud/tripadvisor/restaurants/search",
    params={"query": "new york"},
    headers={"API-Key": "YOUR_API_KEY"}
)

print(response.json())
```

#### Response

<details>
<summary>Sample Response (click to expand)</summary>

```json
{
  "count": 5,
  "results": [
    {
      "tripadvisor_entity_id": 60763,
      "name": "New York City",
      "link": "https://www.tripadvisor.com/Restaurants-g60763-New_York_City_New_York.html",
      "place_type": "CITY",
      "is_tripadvisor_entity": false,
      "featured_image": "https://dynamic-media-cdn.tripadvisor.com/media/photo-o/1c/c5/7c/68/caption.jpg",
      "coordinates": {
        "latitude": 40.713238,
        "longitude": -74.00584
      },
      "parent_location": {
        "tripadvisor_entity_id": 28953,
        "name": "New York"
      },
      "other_links": {
        "root": "https://www.tripadvisor.com/Tourism-g60763-New_York_City_New_York-Vacations.html",
        "attractions": "https://www.tripadvisor.com/Attractions-g60763-Activities-New_York_City_New_York.html",
        "restaurants": "https://www.tripadvisor.com/Restaurants-g60763-New_York_City_New_York.html",
        "hotels": "https://www.tripadvisor.com/Hotels-g60763-New_York_City_New_York-Hotels.html",
        "vacation_rentals": "https://www.tripadvisor.com/VacationRentals-g60763-Reviews-New_York_City_New_York-Vacation_Rentals.html"
      }
    },
    ...
  ]
}
```

</details>

---

### Restaurant List

```
GET https://tripadvisor-scraper-api.omkar.cloud/tripadvisor/restaurants/list
```

#### Parameters

| Parameter | Required | Default | Description |
|-----------|----------|---------|-------------|
| `query` | Yes | — | City name, TripAdvisor URL, or entity ID. |
| `page` | No | `1` | Page number (30 restaurants per page). |
| `min_rating` | No | — | Minimum rating: `3`, `4`, `5`. |
| `establishment_types` | No | — | Filter: `restaurants`, `quick_bites`, `coffee_tea`, `bakeries`, `dessert`, `bars_pubs`, etc. |
| `meal_types` | No | — | Filter: `breakfast`, `brunch`, `lunch`, `dinner`. |
| `currency` | No | `USD` | Currency code. |
| `locale` | No | `en-US` | Localization code. |

#### Example

```python
import requests

response = requests.get(
    "https://tripadvisor-scraper-api.omkar.cloud/tripadvisor/restaurants/list",
    params={"query": "new york", "establishment_types": "restaurants"},
    headers={"API-Key": "YOUR_API_KEY"}
)

print(response.json())
```

#### Response

<details>
<summary>Sample Response (click to expand)</summary>

```json
{
  "count": 10000,
  "per_page": 30,
  "current_page": 1,
  "total_pages": 334,
  "next": "https://tripadvisor-scraper-api.omkar.cloud/restaurants/list?query=60763&establishment_types=restaurants&page=2",
  "previous": null,
  "results": [
    {
      "tripadvisor_entity_id": 655719,
      "name": "Benjamin Steakhouse",
      "link": "https://www.tripadvisor.com/Restaurant_Review-g60763-d655719-Reviews-Benjamin_Steakhouse-New_York_City_New_York.html",
      "rating": 4.3,
      "reviews": 2546,
      "phone": "+1 212-297-9177",
      "featured_image": "https://dynamic-media-cdn.tripadvisor.com/media/photo-o/26/d6/40/87/poterhouse-steak.jpg",
      "award": {
        "award_name": "Travelers Choice",
        "year": 2025,
        "award_type": "travelers_choice"
      },
      "address": {
        "address": "52 East 41st Street, New York City, NY 10017",
        "country": "United States",
        "country_code": "US",
        "postal_code": "10017"
      },
      "coordinates": {
        "latitude": 40.75174,
        "longitude": -73.97906
      },
      "price_range": "$",
      "parent_location": {
        "tripadvisor_entity_id": 60763,
        "name": "New York City"
      },
      "is_open_now": true,
      "status_text": "Open now",
      "hours": [
        {
          "day": "Monday",
          "times": [
            { "open": "07:00", "close": "11:15" },
            { "open": "11:30", "close": "15:45" },
            { "open": "16:00", "close": "22:00" }
          ]
        },
        ...
      ],
      "cuisines": [
        "Steakhouse",
        "Seafood"
      ],
      "establishment_types": [
        {
          "tag_id": 10591,
          "name": "Restaurants"
        }
      ],
      "review_snippets": [
        {
          "snippet_text": "They portion for each person at the table, so each of us had half a lobster,...",
          "review_link": "https://www.tripadvisor.com/ShowUserReviews-g60763-d655719-r918895952-Benjamin_Steakhouse-New_York_City_New_York.html"
        }
      ],
      "reservation_providers": [
        {
          "provider_id": "15910",
          "provider_name": "OpenTable",
          "has_timeslots": true
        }
      ],
      "has_reservation": true,
      "has_delivery": false,
      "is_ad": true
    }
  ]
}
```

</details>

---

### Restaurant Details

```
GET https://tripadvisor-scraper-api.omkar.cloud/tripadvisor/restaurants/detail
```

#### Parameters

| Parameter | Required | Default | Description |
|-----------|----------|---------|-------------|
| `query` | Yes | — | TripAdvisor Restaurant URL, restaurant name, or entity ID. |
| `locale` | No | `en-US` | Localization code. |

#### Example

```python
import requests

response = requests.get(
    "https://tripadvisor-scraper-api.omkar.cloud/tripadvisor/restaurants/detail",
    params={"query": "Piccola Cucina, New York"},
    headers={"API-Key": "YOUR_API_KEY"}
)

print(response.json())
```

#### Response Fields

Response redacted due to too long length. Please make an HTTP request to retrieve the full restaurant details.

---

### Attraction Search

```
GET https://tripadvisor-scraper-api.omkar.cloud/tripadvisor/attractions/search
```

#### Parameters

| Parameter | Required | Default | Description |
|-----------|----------|---------|-------------|
| `query` | Yes | — | Search text (e.g., `new york`, `Disneyland Park, California`). |
| `locale` | No | `en-US` | Localization code. |

#### Example

```python
import requests

response = requests.get(
    "https://tripadvisor-scraper-api.omkar.cloud/tripadvisor/attractions/search",
    params={"query": "new york"},
    headers={"API-Key": "YOUR_API_KEY"}
)

print(response.json())
```

#### Response

<details>
<summary>Sample Response (click to expand)</summary>

```json
{
  "count": 3,
  "results": [
    {
      "tripadvisor_entity_id": 60763,
      "name": "New York City",
      "link": "https://www.tripadvisor.com/Attractions-g60763-Activities-New_York_City_New_York.html",
      "place_type": "CITY",
      "is_tripadvisor_entity": false,
      "featured_image": "https://dynamic-media-cdn.tripadvisor.com/media/photo-o/1c/c5/7c/68/caption.jpg",
      "coordinates": {
        "latitude": 40.713238,
        "longitude": -74.00584
      },
      "parent_location": {
        "tripadvisor_entity_id": 28953,
        "name": "New York"
      },
      "other_links": {
        "root": "https://www.tripadvisor.com/Tourism-g60763-New_York_City_New_York-Vacations.html",
        "attractions": "https://www.tripadvisor.com/Attractions-g60763-Activities-New_York_City_New_York.html",
        "restaurants": "https://www.tripadvisor.com/Restaurants-g60763-New_York_City_New_York.html",
        "hotels": "https://www.tripadvisor.com/Hotels-g60763-New_York_City_New_York-Hotels.html",
        "vacation_rentals": "https://www.tripadvisor.com/VacationRentals-g60763-Reviews-New_York_City_New_York-Vacation_Rentals.html"
      }
    },
    ...
  ]
}
```

</details>

---

### Attractions List

```
GET https://tripadvisor-scraper-api.omkar.cloud/tripadvisor/attractions/list
```

#### Parameters

| Parameter | Required | Default | Description |
|-----------|----------|---------|-------------|
| `query` | Yes | — | City name, TripAdvisor URL, or entity ID. |
| `page` | No | `1` | Page number (30 attractions per page). |
| `good_for` | No | — | Filter: `good_for_kids`, `good_for_couples`, `free_entry`, `hidden_gems`, `adventurous`, etc. |
| `min_rating` | No | — | Minimum rating: `2`, `3`, `4`, `5`. |
| `awards` | No | — | Filter: `travelers_choice`, `travelers_choice_best_of_the_best`. |
| `currency` | No | `USD` | Currency code. |
| `locale` | No | `en-US` | Localization code. |

#### Example

```python
import requests

response = requests.get(
    "https://tripadvisor-scraper-api.omkar.cloud/tripadvisor/attractions/list",
    params={"query": "new york"},
    headers={"API-Key": "YOUR_API_KEY"}
)

print(response.json())
```

#### Response

<details>
<summary>Sample Response (click to expand)</summary>

```json
{
  "count": 8073,
  "per_page": 30,
  "current_page": 1,
  "total_pages": 270,
  "next": "https://tripadvisor-scraper-api.omkar.cloud/attractions/list?query=60763&page=2",
  "previous": null,
  "results": [
    {
      "tripadvisor_entity_id": 105127,
      "name": "Central Park",
      "description": "For more than 150 years, visitors have flocked to Central Park's 843 green acres in the heart of Manhattan. Since 1980, the Park has been managed by the Central Park Conservancy, in partnership with the public. Central Park is open 6 am to 1 am daily. Visit the official website of Central Park to learn more about Park happenings and activities and to learn how you to help Central Park!",
      "neighborhood": "Central Park",
      "link": "https://www.tripadvisor.com/Attraction_Review-g60763-d105127-Reviews-Central_Park-New_York_City_New_York.html",
      "rating": 4.7,
      "reviews": 134359,
      "categories": [
        {
          "id": 11160,
          "name": "Points of Interest & Landmarks"
        },
        {
          "id": 11092,
          "name": "Parks"
        }
      ],
      "award": {
        "award_name": "Travelers Choice Best of the Best",
        "year": "2025",
        "award_type": "travelers_choice_best_of_the_best"
      },
      "featured_image": "https://dynamic-media-cdn.tripadvisor.com/media/photo-o/2f/c4/c8/4b/caption.jpg",
      "pricing_text": null,
      "commerce": {
        "tickets_link": null,
        "tours_link": "https://www.tripadvisor.com/Attraction_Products-g60763-d105127-Central_Park-New_York_City_New_York.html"
      },
      "experiences": {
        "experiences_link": "https://www.tripadvisor.com/Attraction_Products-g60763-d105127-Central_Park-New_York_City_New_York.html",
        "experiences_count": 144
      },
      "review_snippet": null
    },
    ...
  ]
}
```

</details>

---

### Attraction Details

```
GET https://tripadvisor-scraper-api.omkar.cloud/tripadvisor/attractions/detail
```

#### Parameters

| Parameter | Required | Default | Description |
|-----------|----------|---------|-------------|
| `query` | Yes | — | TripAdvisor Attraction URL, attraction name, or entity ID. |
| `locale` | No | `en-US` | Localization code. |

#### Example

```python
import requests

response = requests.get(
    "https://tripadvisor-scraper-api.omkar.cloud/tripadvisor/attractions/detail",
    params={"query": "Central Park, New York"},
    headers={"API-Key": "YOUR_API_KEY"}
)

print(response.json())
```

#### Response Fields

Response redacted due to too long length. Please make an HTTP request to retrieve the full attraction details.

---

### Cruise Destinations

```
GET https://tripadvisor-scraper-api.omkar.cloud/tripadvisor/cruises
```

No additional parameters required. Returns all available cruise destinations.

#### Example

```python
import requests

response = requests.get(
    "https://tripadvisor-scraper-api.omkar.cloud/tripadvisor/cruises",
    headers={"API-Key": "YOUR_API_KEY"}
)

print(response.json())
```

#### Response

<details>
<summary>Sample Response (click to expand)</summary>

```json
{
  "count": 19,
  "results": [
    {
      "tripadvisor_entity_id": 147237,
      "name": "Caribbean"
    },
    {
      "tripadvisor_entity_id": 147414,
      "name": "Bahamas"
    },
    {
      "tripadvisor_entity_id": 150768,
      "name": "Mexico"
    },
    {
      "tripadvisor_entity_id": 28923,
      "name": "Alaska"
    },
    {
      "tripadvisor_entity_id": 147255,
      "name": "Bermuda"
    },
    {
      "tripadvisor_entity_id": 153339,
      "name": "Canada"
    },
    {
      "tripadvisor_entity_id": 14114078,
      "name": "Mediterranean"
    },
    {
      "tripadvisor_entity_id": 6,
      "name": "Africa"
    },
    {
      "tripadvisor_entity_id": 12,
      "name": "Antarctica"
    },
    {
      "tripadvisor_entity_id": 2,
      "name": "Asia"
    },
    {
      "tripadvisor_entity_id": 255055,
      "name": "Australia"
    },
    {
      "tripadvisor_entity_id": 291958,
      "name": "Central America"
    },
    {
      "tripadvisor_entity_id": 294211,
      "name": "China"
    },
    {
      "tripadvisor_entity_id": 4,
      "name": "Europe"
    },
    {
      "tripadvisor_entity_id": 28932,
      "name": "Hawaii"
    },
    {
      "tripadvisor_entity_id": 670819,
      "name": "Indian Ocean"
    },
    {
      "tripadvisor_entity_id": 21,
      "name": "Middle East"
    },
    {
      "tripadvisor_entity_id": 13,
      "name": "South America"
    },
    {
      "tripadvisor_entity_id": 8,
      "name": "South Pacific"
    }
  ]
}
```

</details>

---

### Cruise List

```
GET https://tripadvisor-scraper-api.omkar.cloud/tripadvisor/cruises/list
```

#### Parameters

| Parameter | Required | Default | Description |
|-----------|----------|---------|-------------|
| `destination_name` | Yes | — | Destination: `Caribbean`, `Alaska`, `Mediterranean`, `Europe`, etc. (19 destinations). |
| `page` | No | `1` | Page number (20 cruises per page). |
| `departure_date` | No | — | Departure month (`YYYY-MM`). |
| `min_price` | No | — | Minimum price filter. |
| `max_price` | No | — | Maximum price filter. |
| `cruise_length` | No | — | Duration: `3-5`, `6-9`, `10-14`, `15`. |
| `cabin_type` | No | — | Filter: `inside`, `outside`, `balcony`, `suite`. |
| `sort_by` | No | `popularity` | Sort: `popularity`, `departure_date`, `price`, `cruise_length`, `cruise_ship`. |
| `currency` | No | `USD` | Currency code. |
| `locale` | No | `en-US` | Localization code. |

#### Example

```python
import requests

response = requests.get(
    "https://tripadvisor-scraper-api.omkar.cloud/tripadvisor/cruises/list",
    params={"destination_name": "Caribbean"},
    headers={"API-Key": "YOUR_API_KEY"}
)

print(response.json())
```

#### Response

<details>
<summary>Sample Response (click to expand)</summary>

```json
{
  "count": 504,
  "per_page": 20,
  "current_page": 1,
  "total_pages": 26,
  "next": "https://tripadvisor-scraper-api.omkar.cloud/cruises/list?destination_name=Caribbean&page=2",
  "previous": null,
  "results": [
    {
      "cruise_id": 177986,
      "cruise_title": "7 NIGHT Bahamas CRUISE",
      "duration_nights": 7,
      "cruise_company": {
        "cruise_company_id": 80,
        "cruise_company_name": "MSC Cruises",
        "tripadvisor_entity_id": 17391445,
        "company_cruises_link": "https://www.tripadvisor.com/Cruises-a_cl.17391445-MSC-Cruises",
        "icon_link": "https://images.r.cruisecritic.com/cruise-lines/msc_cruises_smallicon.png"
      },
      "ship": {
        "ship_id": 996,
        "ship_name": "MSC Meraviglia",
        "tripadvisor_entity_id": 15691636,
        "tripadvisor_entity_link": "https://www.tripadvisor.com/Cruise_Review-d15691636-Reviews-MSC_Meraviglia",
        "launch_year": 2017,
        "passenger_capacity": 4475,
        "crew_size": 1536,
        "amenities": [
          "New ship",
          "Mega ship",
          "Bowling alley",
          "Dance club",
          "Indoor pool",
          "Multiple restaurants",
          "Specialty restaurants",
          "Thermal suite",
          "Vibrant nightlife"
        ],
        "reviews": 489,
        "rating": 3,
        "review_snippets": [
          {
            "review_id": 1024876027,
            "review_link": "https://www.tripadvisor.com/ShowUserReviews-g1-d15691636-r1024876027-MSC_Meraviglia-World.html",
            "text": "Family vacation",
            "rating": 3,
            "reviewer_id": "E2BB5CD88E2EFFC15902EE7F21F6CA73"
          }
        ],
        "reasons_to_pick": [
          "You want a cutting-edge family cruise with European flair",
          "You like nonstop activities with round-the-clock fun for all",
          "You want dozens of different bars, lounges and restaurants"
        ],
        "reasons_to_skip": [
          "You don't want cruise catering to European tastes first",
          "You dislike announcements made in up to six different languages"
        ]
      },
      "destination": {
        "destination_id": 118,
        "destination_name": "Bahamas",
        "destination_seo_name": "the Bahamas",
        "destination_image_link": "https://images.r.cruisecritic.com/destinations/rewrite_bahamas.jpg"
      },
      "departure_port": {
        "port_id": 152,
        "port_name": "New York (Brooklyn, Red Hook)",
        "ancestors": [
          { "name": "New York  - All" },
          { "name": "U.S.A. - East Coast" }
        ]
      },
      "arrival_port": {
        "port_id": 152,
        "port_name": "New York (Brooklyn, Red Hook)"
      },
      "itinerary": [
        { "day": 1, "port_name": "New York (Brooklyn, Red Hook)", "tripadvisor_entity_id": 48473 },
        { "day": 2, "port_name": "Cruising", "tripadvisor_entity_id": null },
        { "day": 3, "port_name": "Port Canaveral (Orlando)", "tripadvisor_entity_id": 34574 },
        { "day": 4, "port_name": "Nassau", "tripadvisor_entity_id": 147416 },
        { "day": 5, "port_name": "Ocean Cay MSC Marine Reserve", "tripadvisor_entity_id": null },
        { "day": 6, "port_name": "Cruising", "tripadvisor_entity_id": null },
        { "day": 7, "port_name": "Cruising", "tripadvisor_entity_id": null },
        { "day": 8, "port_name": "New York (Brooklyn, Red Hook)", "tripadvisor_entity_id": 48473 }
      ],
      "sailings": {
        "count": 1,
        "lowest_priced_sailing_id": 2004472,
        "featured_deal_sailing_id": 2004472,
        "results": [
          {
            "sailing_id": 2004472,
            "departure_date": "2025-12-07"
          }
        ]
      }
    },
    ...
  ]
}
```

</details>

---

### Location Reviews

```
GET https://tripadvisor-scraper-api.omkar.cloud/tripadvisor/reviews
```

#### Parameters

| Parameter | Required | Default | Description |
|-----------|----------|---------|-------------|
| `query` | Yes | — | TripAdvisor URL, entity ID, or location name. |
| `page` | No | `1` | Page number (30 reviews per page). |
| `rating_is` | No | — | Filter by star ratings: `1`, `2`, `3`, `4`, `5` (comma-separated). |
| `since` | No | — | Only reviews on or after this date (`YYYY-MM-DD`). |
| `traveler_type` | No | — | Filter: `business`, `couples`, `family`, `friends`, `solo`. |
| `months_of_visit` | No | — | Filter by visit month: `jan`, `feb`, ... `dec`. |
| `keyword` | No | — | Search within review text. |
| `sort_by` | No | `most_recent` | Sort: `most_recent`, `detailed_reviews`. |
| `lang` | No | — | Language filter: `en`, `es`, `fr`, etc. |
| `locale` | No | `en-US` | Localization code (45+ supported). |

#### Example

```python
import requests

response = requests.get(
    "https://tripadvisor-scraper-api.omkar.cloud/tripadvisor/reviews",
    params={"query": "Disneyland Park, California", "rating_is": "4,5"},
    headers={"API-Key": "YOUR_API_KEY"}
)

print(response.json())
```

#### Response

<details>
<summary>Sample Response (click to expand)</summary>

```json
{
  "count": 24317,
  "per_page": 20,
  "current_page": 1,
  "total_pages": 1216,
  "next": "https://tripadvisor-scraper-api.omkar.cloud/reviews?query=https%3A%2F%2Fwww.tripadvisor.com%2FAttraction_Review-g29092-d103346-Reviews-Disneyland_Park-Anaheim_California.html&page=2",
  "previous": null,
  "results": [
    {
      "review_id": 1039040048,
      "review_link": "https://www.tripadvisor.com/ShowUserReviews-g29092-d103346-r1039040048-Disneyland_Park-Anaheim_California.html",
      "title": "Lightning Lane Is a Complete Rip-Off — Not Worth It",
      "text": "Lightning Lane Is a Complete Rip-Off — Not Worth It\n\nThe Lightning Lane system at Disneyland has become one of the most disappointing and misleading parts of the entire experience...",
      "review_tip": "Avoid the cash grabbing lightning",
      "rating": 3,
      "subratings": [],
      "like_count": 1,
      "language": "en",
      "is_translated": false,
      "original_language": "en",
      "owner_response": null,
      "trip": {
        "trip_type": "family",
        "stay_date": "2025-11-30"
      },
      "reviewer": {
        "reviewer_id": "4D3D3860D8DE40C9EDBD9FE37AF2547A",
        "name": "HBlas",
        "profile_link": "https://www.tripadvisor.com/Profile/HBlas",
        "username": "HBlas",
        "avatar": null,
        "contribution_count": 24,
        "hometown": {
          "tripadvisor_entity_id": 152773,
          "location_name": "Puebla",
          "location_name_detailed": "Puebla, Mexico"
        },
        "is_verified": false
      },
      "images": [],
      "created_at_date": "2025-11-15",
      "published_at_date": "2025-11-14"
    }
  ],
  "rating_distribution": {
    "1": 1047,
    "2": 1181,
    "3": 2463,
    "4": 5661,
    "5": 17943
  },
  "original_language_distribution": {
    "en": { "language_name": "English", "reviews": 24224 },
    "es": { "language_name": "Spanish", "reviews": 1493 },
    "ja": { "language_name": "Japanese", "reviews": 404 },
    "fr": { "language_name": "French", "reviews": 203 },
    "it": { "language_name": "Italian", "reviews": 292 },
    "de": { "language_name": "German", "reviews": 166 },
    "pt": { "language_name": "Portuguese", "reviews": 1119 },
    "ru": { "language_name": "Russian", "reviews": 88 },
    "ko": { "language_name": "Korean", "reviews": 42 },
    ...
  },
  "review_keywords": [
    "happiest place on earth",
    "space mountain",
    "disney world",
    "indiana jones",
    "haunted mansion",
    "small world",
    "pirates of the caribbean",
    "fast pass",
    "magical place",
    "main street",
    "cast members",
    "popular rides",
    "jungle cruise",
    "california adventure",
    "wait times",
    "off season",
    "happy place",
    "star wars",
    "love disney",
    "fastpass system"
  ],
  "location": {
    "tripadvisor_entity_id": 103346,
    "name": "Disneyland Park",
    "link": "https://www.tripadvisor.com/Hotel_Review-d103346-Reviews-Disneyland_Park.html",
    "reviews": 0,
    "rating": null,
    "place_type": "hotel"
  }
}
```

</details>

## Error Handling

```python
response = requests.get(
    "https://tripadvisor-scraper-api.omkar.cloud/tripadvisor/reviews",
    params={"query": "Disneyland Park, California"},
    headers={"API-Key": "YOUR_API_KEY"}
)

if response.status_code == 200:
    data = response.json()
elif response.status_code == 401:
    # Invalid API key
    pass
elif response.status_code == 429:
    # Rate limit exceeded
    pass
```

## FAQs

### What data does the API return?

**Reviews** return title, full text, star rating, published date, trip type, travel date, reviewer profile (username, avatar, location, review count), review photos, and management responses. Also includes language breakdown and keyword distribution across all reviews.

**List endpoints** (hotels, restaurants, attractions) return name, rating, review count, ranking, price range, location, photos, award badges (Travelers' Choice, etc.), and category tags.

**Detail endpoints** return comprehensive property data — full description, contact info, hours, all photos, amenities, rating distribution (5-star breakdown), price levels, and booking links.

All in structured JSON. Ready to use in your app.

### How accurate is the data?

Data is pulled directly from TripAdvisor in real time. Ratings, review counts, pricing, and availability reflect what's on TripAdvisor right now. Not cached. Not stale.

### Can I search by URL, location name, or entity ID?

All three. Every endpoint that takes a `query` parameter accepts:
- **TripAdvisor URL**: `https://www.tripadvisor.com/Hotel_Review-g35805-d114581-Reviews-Swissotel_Chicago.html`
- **Location name**: `Swissotel Chicago`
- **Entity ID**: `114581`

Use whichever is most convenient. The API resolves all formats.

### What's the difference between List and Detail endpoints?

**List endpoints** (`/hotels/list`, `/restaurants/list`, `/attractions/list`) return paginated listings for a city or region — 30 results per page with summary data for each.

**Detail endpoints** (`/hotels/detail`, `/restaurants/detail`, `/attractions/detail`) return comprehensive data for a single property — full descriptions, all photos, amenities, rating breakdowns, hours, and more.

Use List to discover and browse. Use Detail to deep-dive into a specific property.

### What review filters are available?

The Reviews endpoint supports star rating (`rating_is=4,5`), date range (`since=2025-01-01`), traveler type (`business`, `couples`, `family`, `friends`, `solo`), visit month, keyword search within review text, language filter, and sort order. All filters are combinable.

### Do I need to handle proxies or CAPTCHAs?

No. The API handles all of that. You make a simple GET request and get clean JSON back. No proxy rotation, no CAPTCHA solving, no HTML parsing.

## Rate Limits

| Plan | Price | Requests/Month |
|------|-------|----------------|
| Free | $0 | 1,000 |
| Starter | $16 | 3,000 |
| Growth | $48 | 15,000 |
| Scale | $148 | 75,000 |

## Questions? We have answers.

Reach out anytime. We will solve your query within 1 working day.

[![Contact Us on WhatsApp about TripAdvisor Scraper](https://raw.githubusercontent.com/omkarcloud/assets/master/images/whatsapp-us.png)](https://api.whatsapp.com/send?phone=918178804274&text=I%20have%20a%20question%20about%20the%20TripAdvisor%20Scraper%20API.)

[![Contact Us on Email about TripAdvisor Scraper](https://raw.githubusercontent.com/omkarcloud/assets/master/images/ask-on-email.png)](mailto:happy.to.help@omkar.cloud?subject=TripAdvisor%20Scraper%20API%20Question)
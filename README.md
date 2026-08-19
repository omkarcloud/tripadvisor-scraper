<p align="center">
  <img src="https://raw.githubusercontent.com/omkarcloud/botasaurus/master/images/mascot.png" alt="tripadvisor scraper" />
</p>
<div align="center" style="margin-top: 0;">
  <h1>✨ TripAdvisor Scraper 🤖</h1>
  <p><strong>Scrape TripAdvisor hotels, restaurants, attractions, and cruises — with reviews, ratings, rankings, prices, full details, and each property's emails, phones, and social profiles. Clean JSON, no blocks, no proxies.</strong></p>
</div>
<em>
  <h5 align="center">(Programming Language - Python 3)</h5>
</em>
<p align="center">
  <a href="#">
    <img alt="tripadvisor-scraper forks" src="https://img.shields.io/github/forks/omkarcloud/tripadvisor-scraper?style=for-the-badge" />
  </a>
  <a href="#">
    <img alt="Repo stars" src="https://img.shields.io/github/stars/omkarcloud/tripadvisor-scraper?style=for-the-badge&color=yellow" />
  </a>
</p>
<p align="center">
  <img src="https://views.whatilearened.today/views/github/omkarcloud/tripadvisor-scraper.svg" width="80px" height="28px" alt="View" />
</p>

TripAdvisor Scraper turns TripAdvisor into clean JSON, pulled live — no blocks, no proxies to manage. Search hotels, restaurants, and attractions by name, list every property in a city with rankings and prices, pull full property details, browse cruises and sailing prices, and paginate every review — all via one API.

**New:** every hotel, restaurant, and attraction also comes with its **website contacts** — emails, phone numbers, social profiles, and the technologies it runs, crawled from the property's own website. TripAdvisor lists at most one phone and website per property; the contact crawl typically finds far more, each with source pages and an official/unofficial flag.

Reviews come back with rating, trip type, dates, language, owner responses, and reviewer profiles; listings carry ratings, review counts, award badges, rankings, prices, coordinates, and photos.

It works across **45+ locales and 145+ currencies** via `locale` and `currency` — so you get localized results and prices in the currency you need.

- **Rated Excellent — 4.6 based on 25 reviews** on [Trustpilot](https://www.trustpilot.com/review/omkar.cloud). Our open source work is sponsored by [1000+ devs on GitHub](https://github.com/sponsors/omkarcloud).

[![Try the TripAdvisor Scraper API in the live playground — free, no signup](https://img.shields.io/badge/%E2%96%B6%20Playground-Run%20a%20live%20request%2C%20free-brightgreen?style=for-the-badge)](https://www.omkar.cloud/tools/tripadvisor-scraper-api/playground?utm_source=github&utm_medium=cpc&utm_content=badge)

[![Free Plan: 200 requests per month](https://img.shields.io/badge/Free%20tier-200%20requests%2Fmonth-blue?style=for-the-badge)](#pricing)

The same scraper is also available on **Apify** and **RapidAPI**:

[![Run on Apify](https://img.shields.io/badge/Run%20on-Apify-blue)](https://apify.com/omkar-cloud/tripadvisor-scraper) [![Run on RapidAPI](https://img.shields.io/badge/Run%20on-RapidAPI-blue?logo=rapidapi)](https://rapidapi.com/Chetan11dev/api/tripadvisor-scraper)

## Example: A Hotel — With Its Website Contacts

One request to the hotel details API returns the full profile **plus the contacts found on the hotel's own website**:

```
GET https://tripadvisor-scraper-api.omkar.cloud/tripadvisor/hotels/detail?query=Swissotel Chicago
```

```json
{
  "tripadvisor_entity_id": 114581,
  "name": "Swissotel Chicago",
  "link": "https://www.tripadvisor.com/Hotel_Review-g35805-d114581-Reviews-Swissotel_Chicago-Chicago_Illinois.html",
  "rating": 4.3,
  "reviews": 6034,
  "hotel_class": 4,
  "ranking": { "current_rank": 30, "total": 205, "text": "#30 of 205 hotels in Chicago" },
  "website": "https://www.swissotel.com/hotels/chicago/",
  "website_contacts": {
    "domain": "swissotel.com",
    "emails": [
      { "value": "chicago@swissotel.com", "sources": ["https://www.swissotel.com/hotels/chicago/"], "is_likely_official": true }
    ],
    "phones": [
      { "value": "+13125650565", "sources": ["https://www.swissotel.com/hotels/chicago/"], "is_likely_official": true }
    ],
    "instagrams": [
      { "value": "https://www.instagram.com/swissotelchicago", "is_likely_official": true }
    ],
    "facebooks": [
      { "value": "https://www.facebook.com/SwissotelChicago", "is_likely_official": true }
    ],
    "technologies": [
      { "name": "Cloudflare", "categories": ["CDN"] },
      { "name": "Google Analytics", "categories": ["Analytics"] }
    ]
  },
  "phone": "+1 312-565-0565",
  "address": "323 East Wacker Drive, Chicago, IL 60601",
  "coordinates": { "latitude": 41.88671, "longitude": -87.61969 },
  "amenities": ["Pool", "Free Wifi", "Fitness Center", "Bar/Lounge", "Restaurant"]
}
```

*Trimmed for readability — the full response also has the rating distribution, AI review summary, review keywords, photo gallery, room tips, FAQs, nearby entities, and booking offers.*

The `website` and `phone` are what TripAdvisor itself lists. **`website_contacts` goes further:** we crawl the hotel's own website with our open-source **[Website Email Contact Scraper](https://github.com/omkarcloud/website-email-contact-scraper)** and return every email, phone number, social profile, and technology found on it — each with source pages and an official/unofficial flag. It's on all three detail endpoints (hotels, restaurants, attractions); set the crawl depth with `website_contacts_crawl_mode` (`homepage` default, `deep`, or `off`).

**[Run this exact request in the Playground — no signup, no key →](https://www.omkar.cloud/tools/tripadvisor-scraper-api/playground?utm_source=github&utm_medium=cpc&utm_content=example)**

The playground comes prefilled with this request and runs it against the live API in your browser. The JSON it returns is identical to what the API returns.

## Start Getting Data in Minutes

Python and Node.js integration examples are available for every endpoint in the playground, so you can get TripAdvisor data in minutes instead of days.

```python
import requests

# List every hotel in a city, ranked, with prices
response = requests.get(
    "https://tripadvisor-scraper-api.omkar.cloud/tripadvisor/hotels/list",
    params={"query": "New York City", "page": "1"},
    headers={"API-Key": "YOUR_API_KEY"},
)

print(response.json())
```

## API Reference

All endpoints are GET requests against `https://tripadvisor-scraper-api.omkar.cloud`, authenticated with the `API-Key` header, returning JSON.

Every endpoint takes a `locale` (default `en-US`, 45+ supported); the list endpoints also take a `currency` (default `USD`, 145+ supported). The three entity families — **Hotels**, **Restaurants**, **Attractions** — each follow the same `search → list → detail` shape; **Cruises** and **Reviews** round it out.

The `query` on search, list, detail, and reviews endpoints accepts a **location name**, a **TripAdvisor URL**, or an **entity ID** — use whichever you have.

### Location Reviews

▶ [Try it live in the Playground →](https://www.omkar.cloud/tools/tripadvisor-scraper-api/playground?utm_source=github&utm_medium=cpc&utm_content=endpoint-reviews)

```
GET https://tripadvisor-scraper-api.omkar.cloud/tripadvisor/reviews?query=126260
```

Paginate every review for any hotel, restaurant, attraction, or cruise — 20 per page — with filters.

| Parameter | Required | Default | Description |
|-----------|----------|---------|-------------|
| `query` | Yes | — | Location name, TripAdvisor URL, or entity ID. |
| `page` | No | `1` | Page number. |
| `sort_by` | No | `most_recent` | `most_recent`, `detailed_reviews`. |
| `rating_is` | No | — | Star ratings, comma-separated (e.g. `4,5`). |
| `since` | No | — | Only reviews on or after this date (`YYYY-MM-DD`). |
| `traveler_type` | No | — | `business`, `couples`, `family`, `friends`, `solo` (comma-separated). |
| `months_of_visit` | No | — | Months the traveler visited (comma-separated). |
| `keyword` | No | — | Keyword to match in review title or body. |
| `locale` | No | `en-US` | Localization code. |

<details>
<summary>Sample Response (click to expand)</summary>

```json
{
  "count": 6657,
  "per_page": 20,
  "current_page": 1,
  "total_pages": 333,
  "next": "https://tripadvisor-scraper-api.omkar.cloud/tripadvisor/reviews?query=126260&page=2",
  "previous": null,
  "results": [
    {
      "review_id": 1073681759,
      "review_link": "https://www.tripadvisor.com/ShowUserReviews-g60763-d126260-r1073681759-Lotte_New_York_Palace-New_York_City_New_York.html",
      "title": "Would not stay again",
      "text": "Items stolen from room, incidentals amount very high $600 only received $115 back...",
      "rating": 1,
      "subratings": [],
      "like_count": 0,
      "language": "en",
      "is_translated": false,
      "owner_response": null,
      "trip": { "trip_type": null, "stay_date": "2026-08-31" },
      "reviewer": {
        "reviewer_id": "D3AA4EBE6B09E7177A080FC1762FBE5D",
        "name": "whyteclair",
        "profile_link": "https://www.tripadvisor.com/Profile/whyteclair",
        "contribution_count": 6,
        "is_verified": false
      },
      "images": [],
      "created_at_date": "2026-08-17",
      "published_at_date": "2026-08-18"
    }
  ],
  "location": {
    "tripadvisor_entity_id": 126260,
    "name": "Lotte New York Palace",
    "link": "https://www.tripadvisor.com/Hotel_Review-d126260-Reviews-Lotte_New_York_Palace.html",
    "place_type": "hotel"
  }
}
```

</details>

---

### Hotels

```
GET /tripadvisor/hotels/search?query=new+york
GET /tripadvisor/hotels/list?query=New+York+City
GET /tripadvisor/hotels/detail?query=114581
```

- **Search** resolves a query into matching locations (cities and hotels), each with entity ID, coordinates, and cross-links to that place's hotels/restaurants/attractions. Takes `query` (required) and `locale`.
- **List** returns every hotel in a city, ranked, 30 per page — with rating, review count, price and price range, award badges, ranking, hotel class, style scores, address, coordinates, subratings, and a review snippet.
- **Detail** returns the full hotel profile. Takes `query` (required), `locale`, and **`website_contacts_crawl_mode`** (`homepage` default / `deep` / `off`) — which crawls the hotel's own website and adds `website_contacts` (emails, phones, social profiles, technologies) just below `website`. List also takes `page`, `check_in_date`, `check_out_date`, `rooms`, `adults`, `min_rating`, `is_5_star`, `awards`, and `currency`.

| List parameter | Required | Default | Description |
|-----------|----------|---------|-------------|
| `query` | Yes | — | City name, location URL, or entity ID. |
| `page` | No | `1` | Page number (30 hotels per page). |
| `check_in_date` / `check_out_date` | No | — | Stay dates (`YYYY-MM-DD`) for live prices. |
| `rooms` / `adults` | No | `1` / `2` | Occupancy for pricing. |
| `min_rating` | No | — | `2`, `3`, `4`, `5`. |
| `is_5_star` | No | — | `true` for 5-star hotels only. |
| `awards` | No | — | `travelers_choice`, `travelers_choice_best_of_the_best`. |
| `currency` | No | `USD` | Currency code. |
| `locale` | No | `en-US` | Localization code. |

<details>
<summary>Sample Response — Hotel List (click to expand)</summary>

```json
{
  "count": 1005,
  "per_page": 30,
  "current_page": 1,
  "total_pages": 34,
  "next": "https://tripadvisor-scraper-api.omkar.cloud/tripadvisor/hotels/list?query=60763&page=2",
  "previous": null,
  "results": [
    {
      "tripadvisor_entity_id": 23448880,
      "name": "Motto by Hilton New York City Chelsea",
      "link": "https://www.tripadvisor.com/Hotel_Review-g60763-d23448880-Reviews-Motto_by_Hilton_New_York_City_Chelsea-New_York_City_New_York.html",
      "description": "Modern NYC hotel with a central location and breathtaking views of landmarks...",
      "rating": 4.8,
      "reviews": 1758,
      "phone": "1 (855) 605-0316",
      "featured_image": "https://cdn.tripadvisor.com/media/photo-o/31/be/a9/38/exterior.jpg",
      "award": { "award_name": "Travelers Choice", "year": 2025, "award_type": "travelers_choice" },
      "ranking": { "current_rank": 25, "total": 770, "text": "#23 of 517 hotels in New York City" },
      "hotel_class": 3.5,
      "address": "113 West 24th Street, New York City, NY 10001",
      "coordinates": { "latitude": 40.74406, "longitude": -73.99294 },
      "price": 203,
      "price_range": { "min": 203, "max": 805 },
      "parent_location": { "tripadvisor_entity_id": 60763, "name": "New York City" },
      "subratings": {
        "location": 4.72, "cleanliness": 4.62, "service": 4.78, "value": 4.54,
        "sleep_quality": 4.88, "rooms": 4.9, "food": 4.68
      },
      "is_ad": false
    }
  ]
}
```

</details>

---

### Restaurants

```
GET /tripadvisor/restaurants/search?query=new+york
GET /tripadvisor/restaurants/list?query=New+York+City
GET /tripadvisor/restaurants/detail?query=Piccola+Cucina,+New+York
```

- **Search** resolves a query into matching locations. Takes `query` (required) and `locale`.
- **List** returns every restaurant in a city, 30 per page — with rating, review count, phone, menu link, cuisines, price range, opening hours, review snippets, reservation providers, and delivery flags. Takes `query` (required), `page`, `min_rating` (`3`/`4`/`5`), `establishment_types` (`restaurants`, `quick_bites`, `coffee_tea`, `bakeries`, `dessert`, `bars_pubs`, …), `meal_types` (`breakfast`, `brunch`, `lunch`, `dinner`), and `locale`.
- **Detail** returns the full restaurant profile. Takes `query` (required), `locale`, and **`website_contacts_crawl_mode`** (`homepage` default / `deep` / `off`) — which crawls the restaurant's own website and adds `website_contacts` (emails, phones, social profiles, technologies).

<details>
<summary>Sample Response — Restaurant List (click to expand)</summary>

```json
{
  "count": 10000,
  "per_page": 30,
  "current_page": 1,
  "total_pages": 334,
  "next": "https://tripadvisor-scraper-api.omkar.cloud/tripadvisor/restaurants/list?query=60763&page=2",
  "previous": null,
  "results": [
    {
      "tripadvisor_entity_id": 655719,
      "name": "Benjamin Steakhouse",
      "link": "https://www.tripadvisor.com/Restaurant_Review-g60763-d655719-Reviews-Benjamin_Steakhouse-New_York_City_New_York.html",
      "rating": 4.3,
      "reviews": 2546,
      "phone": "+1 212-297-9177",
      "menu_link": "https://benjaminsteakhouse.com/nyc/our-menus/",
      "award": { "award_name": "Travelers Choice", "year": 2025, "award_type": "travelers_choice" },
      "address": { "address": "52 East 41st Street, New York City, NY 10017", "country_code": "US", "postal_code": "10017" },
      "coordinates": { "latitude": 40.75174, "longitude": -73.97906 },
      "price_range": "$",
      "is_open_now": true,
      "cuisines": ["Steakhouse", "Seafood"],
      "establishment_types": [{ "tag_id": 10591, "name": "Restaurants" }],
      "has_reservation": true,
      "has_delivery": false
    }
  ]
}
```

</details>

---

### Attractions

```
GET /tripadvisor/attractions/search?query=new+york
GET /tripadvisor/attractions/list?query=New+York+City
GET /tripadvisor/attractions/detail?query=Central+Park,+New+York
```

- **Search** resolves a query into matching locations. Takes `query` (required) and `locale`.
- **List** returns every attraction in a city, 30 per page — with rating, review count, categories, award badges, description, neighborhood, ticket/tour links, and experiences count. Takes `query` (required), `page`, `good_for` (`good_for_kids`, `good_for_couples`, `free_entry`, `hidden_gems`, `adventurous`, …), `min_rating`, `awards`, `currency`, and `locale`.
- **Detail** returns the full attraction profile. Takes `query` (required), `locale`, and **`website_contacts_crawl_mode`** (`homepage` default / `deep` / `off`) — which crawls the attraction's own website and adds `website_contacts` (emails, phones, social profiles, technologies).

<details>
<summary>Sample Response — Attractions List (click to expand)</summary>

```json
{
  "count": 8073,
  "per_page": 30,
  "current_page": 1,
  "total_pages": 270,
  "next": "https://tripadvisor-scraper-api.omkar.cloud/tripadvisor/attractions/list?query=60763&page=2",
  "previous": null,
  "results": [
    {
      "tripadvisor_entity_id": 105127,
      "name": "Central Park",
      "description": "For more than 150 years, visitors have flocked to Central Park's 843 green acres...",
      "neighborhood": "Central Park",
      "link": "https://www.tripadvisor.com/Attraction_Review-g60763-d105127-Reviews-Central_Park-New_York_City_New_York.html",
      "rating": 4.7,
      "reviews": 134359,
      "categories": [
        { "id": 11160, "name": "Points of Interest & Landmarks" },
        { "id": 11092, "name": "Parks" }
      ],
      "award": { "award_name": "Travelers Choice Best of the Best", "year": "2025", "award_type": "travelers_choice_best_of_the_best" },
      "featured_image": "https://cdn.tripadvisor.com/media/photo-o/2f/c4/c8/4b/caption.jpg",
      "experiences": { "experiences_count": 144 }
    }
  ]
}
```

</details>

---

### Cruises

```
GET /tripadvisor/cruises                                  # 19 destinations, no params
GET /tripadvisor/cruises/list?destination_name=Caribbean
GET /tripadvisor/cruises/detail?query=Seabourn+Ovation
GET /tripadvisor/cruises/sailing-pricing?sailing_id=2014294
```

- **Cruise Destinations** lists all 19 cruise destinations with their entity IDs. No parameters.
- **Cruise List** returns cruises for a destination, 20 per page — each with ship (capacity, crew, amenities, rating, reasons to pick/skip), departure/arrival ports, day-by-day itinerary, and sailings with prices. Takes `destination_name` (required), `page`, `departure_date` (`YYYY-MM`), `min_price`/`max_price`, `cruise_length` (`3-5`, `6-9`, `10-14`, `15`), `cabin_type` (`inside`, `outside`, `balcony`, `suite`), `sort_by` (`popularity`, `departure_date`, `price`, `cruise_length`, `cruise_ship`), `currency`, and `locale`.
- **Cruise Details** returns the full ship profile — cabins, dining, activities, decks, itineraries, rating distribution, and initial reviews. Takes `query` (required) and `locale`.
- **Cruise Sailing Pricing** returns per-cabin-type prices from multiple vendors for a specific sailing. Takes `sailing_id` (required), `currency`, and `locale`.

<details>
<summary>Sample Response — Cruise Destinations (click to expand)</summary>

```json
{
  "count": 19,
  "results": [
    { "tripadvisor_entity_id": 147237, "name": "Caribbean" },
    { "tripadvisor_entity_id": 147414, "name": "Bahamas" },
    { "tripadvisor_entity_id": 28923, "name": "Alaska" },
    { "tripadvisor_entity_id": 14114078, "name": "Mediterranean" },
    { "tripadvisor_entity_id": 4, "name": "Europe" }
  ]
}
```

</details>

---

### Supported Locales

`da-DK`, `de-AT`, `de-CH`, `de-DE`, `en-AU`, `en-CA`, `en-GB`, `en-IE`, `en-IN`, `en-NZ`, `en-US`, `es-AR`, `es-CO`, `es-ES`, `es-MX`, `es-PE`, `fr-BE`, `fr-CA`, `fr-CH`, `fr-FR`, `it-IT`, `ja-JP`, `ko-KR`, `nl-BE`, `nl-NL`, `pt-BR`, `pt-PT`, `ru-RU`, `sv-SE`, `tr-TR`, `zh-CN`, `zh-TW`, and more — 45+ locales, plus 145+ currency codes on the list endpoints.

## Pricing

| Plan | Price | Requests/Month |
|------|-------|----------------|
| Free | $0 | 200 |
| Starter | $16 | 20,000 |
| Grow | $48 | 100,000 |
| Scale | $148 | 400,000 |

1 API call = 1 request

Free Plan Available — [create your API key →](https://www.omkar.cloud/auth/sign-up?redirect=/api-key&utm_source=github&utm_medium=cpc&utm_content=pricing-signup). No credit card for the free tier.

## FAQs

### Can I try the API before signing up?

Yes. The playground runs live requests in your browser — free, no account, no API key. [Try it in the Playground →](https://www.omkar.cloud/tools/tripadvisor-scraper-api/playground?utm_source=github&utm_medium=cpc&utm_content=faq)

### How does the API find property emails, phone numbers, and social profiles?

TripAdvisor lists at most one phone and website per property. We go further: on the hotel, restaurant, and attraction **detail** endpoints, the property's own website is crawled by our open-source **[Website Email Contact Scraper](https://github.com/omkarcloud/website-email-contact-scraper)**, and every email, phone number, social profile, and technology it finds comes back as `website_contacts`, each with the source pages and an `is_likely_official` flag. Control the crawl depth with `website_contacts_crawl_mode` (`homepage` default, `deep`, or `off`).

Want the same contact extraction for any website, free? **[Get the Website Email Contact Scraper on GitHub →](https://github.com/omkarcloud/website-email-contact-scraper)**

### How do I get every review for a place?

Call Location Reviews (`GET /tripadvisor/reviews?query=126260`) with a location name, TripAdvisor URL, or entity ID. It returns 20 reviews per page with a `next` link, and filters for `rating_is`, `since`, `traveler_type`, `months_of_visit`, `keyword`, and `sort_by`.

### How do I find hotels, restaurants, or attractions in a city?

Use the Search endpoint to resolve a place name into its entity ID, then pass that ID (or the city name) into the matching List endpoint. List returns every property ranked, 30 per page, with a `next` link to walk through all pages.

### Does it work for non-English regions and other currencies?

Yes. Pass `locale` (45+ supported, e.g. `en-GB`, `fr-FR`, `de-DE`, `ja-JP`, `pt-BR`) and, on list endpoints, `currency` (145+ codes). You'll get localized results and prices in the currency you choose.

### How fresh is the data?

Data is pulled from TripAdvisor in real time. Every API call fetches live data — not cached or stale results. Ratings, review counts, rankings, and prices reflect what's on TripAdvisor right now.

### Will I get blocked or need proxies?

No. We handle the scraping infrastructure — you call a normal REST API and never touch TripAdvisor directly, so there are no proxies, headless browsers, or CAPTCHAs on your side.

### Can I pass a URL instead of a name?

Yes. Search, list, detail, and reviews endpoints accept a location name, a full TripAdvisor URL, or an entity ID — use whichever you have.

## More Travel & Data Scrapers: Airbnb & Google Maps

- **[Airbnb Scraper API](https://github.com/omkarcloud/airbnb-scraper)** — the same clean JSON for Airbnb: search any location, list every home with live nightly prices, and pull full room details with amenities, house rules, and host profiles across 67 country sites. Cross-reference hotels against short-term rentals.

- **[Google Maps Scraper (3,100+ GitHub Stars)](https://github.com/omkarcloud/google-maps-scraper)** — need tens of thousands of leads? Type a niche and a city ("dentists in New York") and get every matching business as a ready-to-call lead list — name, address, phone, website, emails, rating, and reviews. The free tier alone pulls up to 100K leads a month.

- **[Website Email Contact Scraper](https://github.com/omkarcloud/website-email-contact-scraper)** — **Free and open source.** Point it at any website and get every email, phone number, and social profile on it, each with source pages and an official/unofficial flag.

## Support

Built by developers, for developers — when you reach out, you talk to the engineers who built the API, not a support script. Message us anytime and we'll solve your query within 1 working day.


[![Contact Us on WhatsApp about TripAdvisor Scraper](https://raw.githubusercontent.com/omkarcloud/assets/master/images/whatsapp-us.png)](https://api.whatsapp.com/send?phone=918178804274&text=I%20have%20a%20question%20about%20the%20TripAdvisor%20Scraper%20API.)

Email: [happy.to.help@omkar.cloud](mailto:happy.to.help@omkar.cloud?subject=TripAdvisor%20Scraper%20API%20Question)

[![Email Us about TripAdvisor Scraper](https://raw.githubusercontent.com/omkarcloud/assets/master/images/ask-on-email.png)](mailto:happy.to.help@omkar.cloud?subject=TripAdvisor%20Scraper%20API%20Question)

## Love It? Star It! ⭐

From one developer to another: If the TripAdvisor Scraper API saved you time, please [star the repo](https://github.com/omkarcloud/tripadvisor-scraper).

Here's why it matters: most developers judge a scraper by its stars before trying it. Your star helps the next developer — someone deciding whether the TripAdvisor data here is real and reliable — try it with confidence.

It takes only 1 second, and means the world to me.

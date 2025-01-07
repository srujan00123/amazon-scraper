import requests
from pprint import pprint
import json

# Structure payload.
payload = {
    "source": "amazon_search",
    "domain": "in",
    "query": "ryzen 9 9900x",
    "start_page": 1,
    "pages": 1,
    "parse": True,
    # "context": [
    #     {"key": "category_id", "value": 16391843031},
    #     {"key": "merchant_id", "value": "3AA17D2BRD4YMT0X"},
    # ],
}


response = requests.request(
    "POST",
    "https://realtime.oxylabs.io/v1/queries",
    auth=("srujan_3txSt", "Oxylab+=2000"),
    json=payload,
)

# Save JSON response to a file.
with open("response.json", "w") as file:
    json.dump(response.json(), file, indent=4)

print("Response saved to response.json")

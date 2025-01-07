import requests
from pprint import pprint
import dotenv
import os

# Load environment variables from .env file.
dotenv.load_dotenv()

# Get credentials from environment variables.
USER = os.getenv("USER_OXYLAB")
PASS = os.getenv("PASS_OXYLAB")
print(USER)
print(PASS)

# Structure payload.
payload = {
    "source": "amazon_pricing",
    "domain": "in",
    "query": "B0CGJDKLB8",
    "parse": True,
}


# Get response.
response = requests.request(
    "POST",
    "https://realtime.oxylabs.io/v1/queries",
    auth=(USER, PASS),
    json=payload,
)

# Print prettified response to stdout.
pprint(response.json())

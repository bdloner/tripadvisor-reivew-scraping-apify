import sys
import os
from dotenv import load_dotenv
from apify_client import ApifyClient
from integrate_db.db_insert import insert_into_database

# Load environment variables from .env file
load_dotenv()

# Define database connection parameters
APIFY_TOKEN = os.getenv('APIFY_TOKEN')

def main(url):
    # Initialize the ApifyClient with your API token
    client = ApifyClient(APIFY_TOKEN)

    # Prepare the Actor input
    run_input = {
        "lastReviewDate": "",
        "maxItemsPerQuery": 1,
        "reviewRatings": [
            "ALL_REVIEW_RATINGS"
        ],
        "reviewsLanguages": [
            "th",
            "ru",
            "en"
        ],
        "scrapeReviewerInfo": True,
        "startUrls": [
            {
                "url": url
            }
        ]
    }

    # Run the Actor and wait for it to finish
    run = client.actor("Hvp4YfFGyLM635Q2F").call(run_input=run_input)

    # Fetch and print Actor results from the run's dataset (if there are any)
    for item in client.dataset(run["defaultDatasetId"]).iterate_items():
        insert_into_database(item)

if __name__ == "__main__":
    # Check if the correct number of arguments is provided
    if len(sys.argv) != 2:
        print("Usage: python main.py <URL>")
        sys.exit(1)

    # Extract the URL from the command-line argument
    url = sys.argv[1]

    # Call the main function with the provided URL
    main(url)
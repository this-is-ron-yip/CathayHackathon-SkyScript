import requests
import os


GOOGLE_MAP_API_KEY = os.getenv("GOOGLE_MAP_API_KEY")

def getDestinations(query):

    # Define the API endpoint and parameters
    url = "https://maps.googleapis.com/maps/api/place/textsearch/json"
    params = {
        "query": query,
        "key": GOOGLE_MAP_API_KEY
    }

    # Make the GET request
    response = requests.get(url, params=params)
    # Check the response status and handle the output
    if not response.status_code == 200:
        print(f"Error: {response.status_code}")
        
    return response.json()


def DestinationRetreiverAgent(data):
    destinations = dict()
    for interest in data["interest"]:
        destinations[interest] = getDestinations(f"{interest} in {data["destination"]}")
    return destinations    

if __name__ == "__main__":
    data = {'destination': 'hong kong', 'interest': ['shopping', 'movie', 'eating'], 'length': 3}
    DestinationRetreiverAgent(data)

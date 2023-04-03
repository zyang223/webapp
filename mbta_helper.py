# # Your API KEYS (you need to use your own keys - very long random characters)
# from config import MAPBOX_TOKEN, MBTA_API_KEY


# Useful URLs (you need to add the appropriate parameters for your requests)
MAPBOX_BASE_URL = "https://api.mapbox.com/geocoding/v5/mapbox.places"
MBTA_BASE_URL = "https://api-v3.mbta.com/stops"


# A little bit of scaffolding if you want to use it
import urllib.request
import json
from pprint import pprint

def get_json(url: str) -> dict:
    """
    Given a properly formatted URL for a JSON web API request, return a Python JSON object containing the response to that request.

    Both get_lat_long() and get_nearest_station() might need to use this function."""

    MAPBOX_BASE_URL = "https://api.mapbox.com/geocoding/v5/mapbox.places"
    MAPBOX_TOKEN = "pk.eyJ1IjoienlhbmcwMTIiLCJhIjoiY2xmenljeGQ0MDBlczNmcXRrZHh0N3FjayJ9.hqGnA5P5s0lvMRp1Pm8IyA"
    query = 'Babson%20College'
    url=f'{MAPBOX_BASE_URL}/{query}.json?access_token={MAPBOX_TOKEN}&types=poi'
    print(url) # Try this URL in your browser first

    with urllib.request.urlopen(url) as f:
        response_text = f.read().decode('utf-8')
        response_data = json.loads(response_text)
        pprint(response_data)
        return response_data
    



def get_lat_long(place_name: str) -> tuple[str, str]:
    """
    Given a place name or address, return a (latitude, longitude) tuple with the coordinates of the given place.

    See https://docs.mapbox.com/api/search/geocoding/ for Mapbox Geocoding API URL formatting requirements.

    USing the similar code from get_json but changing the query to a place name and print them in a better format
    """
    MAPBOX_BASE_URL = "https://api.mapbox.com/geocoding/v5/mapbox.places"
    MAPBOX_TOKEN = "pk.eyJ1IjoienlhbmcwMTIiLCJhIjoiY2xmenljeGQ0MDBlczNmcXRrZHh0N3FjayJ9.hqGnA5P5s0lvMRp1Pm8IyA"
    query = place_name
    url=f'{MAPBOX_BASE_URL}/{query}.json?access_token={MAPBOX_TOKEN}&types=poi'
    print(url) # Try this URL in your browser first

    with urllib.request.urlopen(url) as f:
        response_text = f.read().decode('utf-8')
        response_data = json.loads(response_text)
    latitude=response_data["features"][0]["center"][1]
    longitude=response_data["features"][0]["center"][0]
    return latitude,longitude

place_name="Babson"
latitude, longitude = get_lat_long(place_name)
# print(f"The latitude and longitude of {place_name} are: {latitude}, {longitude}")


def get_nearest_station(latitude: str, longitude: str) -> tuple[str, bool]:
    """
    Given latitude and longitude strings, return a (station_name, wheelchair_accessible) tuple for the nearest MBTA station to the given coordinates.

    See https://api-v3.mbta.com/docs/swagger/index.html#/Stop/ApiWeb_StopController_index for URL formatting requirements for the 'GET /stops' API.
    """
    API="be09a127f60444dd989e786c5e2f4e39"
    MBTA_BASE_URL="https://api-v3.mbta.com/stops"
    url = f"{MBTA_BASE_URL}?include=wheelchair_boarding"
    with urllib.request.urlopen(url) as f:
        response_text = f.read().decode('utf-8')
        response_data = json.loads(response_text)
    pprint(response_data) 
    station_name = response_data["data"][0]["attributes"]["name"]
    wheelchair_accessible = response_data["data"][0]["attributes"]["wheelchair_boarding"] == 1
    return station_name, wheelchair_accessible

latitude="42.2981925"
longitude="-71.263598"
get_nearest_station(latitude,longitude)



def find_stop_near(place_name: str) -> tuple[str, bool]:
    """
    Given a place name or address, return the nearest MBTA stop and whether it is wheelchair accessible.

    This function might use all the functions above.
    """
    pass


def main():
    """
    You can test all the functions here
    """
    pass


if __name__ == '__main__':
    main()

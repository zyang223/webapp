# # Your API KEYS (you need to use your own keys - very long random characters)
# from config import MAPBOX_TOKEN, MBTA_API_KEY


# Useful URLs (you need to add the appropriate parameters for your requests)
MAPBOX_BASE_URL = "https://api.mapbox.com/geocoding/v5/mapbox.places"
MBTA_BASE_URL = "https://api-v3.mbta.com/stops"


# A little bit of scaffolding if you want to use it
import urllib.request
import json
from pprint import pprint
import urllib.parse

def get_json(url: str) -> dict:
    """
    Given a properly formatted URL for a JSON web API request, return a Python JSON object containing the response to that request.

    Both get_lat_long() and get_nearest_station() might need to use this function."""

    print(f"The Url you are accessing to is :{url}") # Try this URL in your browser first

    with urllib.request.urlopen(url) as f:
        response_text = f.read().decode('utf-8')
        response_data = json.loads(response_text)
        pprint(response_data)
        return response_data
    

def get_url(place_name: str) -> str:
    """
    Write a function that takes an address or place name as input and returns a properly encoded URL to make a Mapbox geocoding request.
    """
    MAPBOX_BASE_URL = "https://api.mapbox.com/geocoding/v5/mapbox.places"
    MAPBOX_TOKEN = "pk.eyJ1IjoienlhbmcwMTIiLCJhIjoiY2xmenljeGQ0MDBlczNmcXRrZHh0N3FjayJ9.hqGnA5P5s0lvMRp1Pm8IyA"
    possible_place_name=place_name
    url=f"{MAPBOX_BASE_URL}{possible_place_name}.json?access_token={MAPBOX_TOKEN}"
    return url


def get_lat_long(place_name: str) -> tuple[str, str]:
    """
    Given a place name or address, return a (latitude, longitude) tuple with the coordinates of the given place.

    See https://docs.mapbox.com/api/search/geocoding/ for Mapbox Geocoding API URL formatting requirements.

    USing the similar code from get_json but changing the query to a place name and print them in a better format
    """
    MAPBOX_BASE_URL = "https://api.mapbox.com/geocoding/v5/mapbox.places"
    MAPBOX_TOKEN = "pk.eyJ1IjoienlhbmcwMTIiLCJhIjoiY2xmenljeGQ0MDBlczNmcXRrZHh0N3FjayJ9.hqGnA5P5s0lvMRp1Pm8IyA"
    place_name=place_name.replace(" ","%20") # take out the space
    query = place_name
    url=f'{MAPBOX_BASE_URL}/{query}.json?access_token={MAPBOX_TOKEN}&types=poi'

    with urllib.request.urlopen(url) as f:
        response_text = f.read().decode('utf-8')
        response_data = json.loads(response_text)
    latitude=response_data["features"][0]["center"][1]
    longitude=response_data["features"][0]["center"][0]
    return latitude,longitude
#input area######################################################################



def get_nearest_station(latitude: str, longitude: str) -> tuple[str, bool]:
    """
    Given latitude and longitude strings, return a (station_name, wheelchair_accessible) tuple for the nearest MBTA station to the given coordinates.

    See https://api-v3.mbta.com/docs/swagger/index.html#/Stop/ApiWeb_StopController_index for URL formatting requirements for the 'GET /stops' API.
    """
    api_key="be09a127f60444dd989e786c5e2f4e39"
    MBTA_BASE_URL="https://api-v3.mbta.com/stops"
    url = f"{MBTA_BASE_URL}?sort=distance&filter[latitude]={latitude}&filter[longitude]={longitude}&api_key={api_key}"# found the url format from the url formatting requirement
    with urllib.request.urlopen(url) as f:
        response_text = f.read().decode('utf-8')
        response_data = json.loads(response_text)
    if len(response_data["data"]) >0:    # add an if statement to check if the station exist or not for a clear purpose
        station_name = response_data["data"][0]["attributes"]["name"] 
        wheelchair_accessible = response_data["data"][0]["attributes"]["wheelchair_boarding"] == 1
        return station_name, wheelchair_accessible
    else:
        print("Sorry, there is no MBTA station near the given coordinates.")

#Input Area################################


############################################


def find_stop_near(place_name: str) -> tuple[str, bool]:
    """
    Given a place name or address, return the nearest MBTA stop and whether it is wheelchair accessible.

    This function might use all the functions above.
    """
    place_name=place_name.replace(" ","%20") # take out the space
    latitude,longitude=get_lat_long(place_name)
    print(f"The target place name is{place_name}, latitude is{latitude},longitude={longitude}")
    station_name, wheelchair_accessible=get_nearest_station(latitude,longitude)
    if station_name:
        pass
    else:     
        print("Sorry, there is no MBTA station near the given coordinates.")
    return station_name, wheelchair_accessible




def main():

    MAPBOX_BASE_URL = "https://api.mapbox.com/geocoding/v5/mapbox.places"
    MAPBOX_TOKEN = "pk.eyJ1IjoienlhbmcwMTIiLCJhIjoiY2xmenljeGQ0MDBlczNmcXRrZHh0N3FjayJ9.hqGnA5P5s0lvMRp1Pm8IyA"
    query = 'Babson%20College'
    url=f'{MAPBOX_BASE_URL}/{query}.json?access_token={MAPBOX_TOKEN}&types=poi'
    # print(get_json(url))

    """ Get URL"""
    print(get_url("Cambridge"))
    ####################################################################################################
    """Get Longitude and Latitude"""
    place_name="Babson"
    latitude, longitude = get_lat_long(place_name)
    place_new_name = urllib.parse.unquote(place_name)#(return the space)
    print(f"The latitude and longitude of {place_new_name} are: {latitude}, {longitude}")
    #######################################################################################################
    """GET STATION AND WHEEL CHAIR"""
    latitude="42.3598"
    longitude="-71.0921"
    station_name, wheelchair_accessible = get_nearest_station(latitude,longitude)
    if wheelchair_accessible:
        print(f"The nearest station from the map is {station_name} and it is wheelchair accessible.")
    else:
        print(f"The nearest station from the map is {station_name} and it is not wheelchair accessible.")
    ################################################################################################################
    """USE PLACE NAME TO GET LON AND LAT, STATION AND WHEELCHAIR"""
    place_name="TD Garden"
    station_name,wheelchair_accessible=(find_stop_near(place_name))
    place_name=place_name.replace("%20", " ")# return the space
    if wheelchair_accessible:
        print(f"The nearest station from the map is {station_name} and it is wheelchair accessible.")
    else:
        print(f"The nearest station from the map is {station_name} and it is not wheelchair accessible.")


if __name__ == '__main__':
    main()

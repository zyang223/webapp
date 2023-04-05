import urllib.request
import json
import pprint

Api_key="756b1938810423b43e6ac1212d9d40fc"


def get_temp(city: str) -> float:
    """
    return the current temperature of a given city
    """
    city = city.replace(' ', '%20')
    url = f'https://api.openweathermap.org/data/2.5/weather?q={city},us&APPID={Api_key}&units=metric'
    print(url)

    with urllib.request.urlopen(url) as f:
        response_text = f.read().decode('utf-8')
        # print(response_text)
        response_data = json.loads(response_text)
    # pprint.pprint(response_data)
    temperature=response_data['main']['temp']
    return temperature


if __name__ == "__main__":
    print(get_temp('wellesley'))
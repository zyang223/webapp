from flask import Flask, render_template, request
from mbta_helper import*# import function wrote in the mbta_helper.py
from weather_helper import*
app = Flask(__name__)


@app.route('/welcome/')
def welcome_page():
    return render_template("welcome.html")

@app.route('/nearest/', methods=['GET']) # using the get method to do the MBTA Station
def nearest():
    address = request.args.get('address')
    latitude, longitude = get_lat_long(address)
    stop_name, wheelchair_accessible,description = get_nearest_station(latitude, longitude)
    if stop_name:
            return render_template("station_result.html", station_name=stop_name, address=address, wheelchair_accessible=wheelchair_accessible,description=description)
    else:
            return render_template("oops.html")


@app.get('/temp/') # using the post method to do the weather section
def temp_get():
    return render_template('weather-form.html')


@app.post('/temp/')
def temp_post():
    city_name = request.form['city']
    temperature = get_temp(city_name)
    summary, url = get_city_intro(city_name)
    return render_template('weather-result.html', city=city_name, temp=temperature, city_url=url, city_summary=summary)




if __name__ == '__main__':
    app.run(debug=True)

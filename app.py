from flask import Flask, render_template, request
from mbta_helper import*# import function wrote in the mbta_helper.py
app = Flask(__name__)


@app.route('/welcome/')
def welcome_page():
    return render_template("welcome.html")

@app.route('/nearest/', methods=['GET'])
def nearest():
    address = request.args.get('address')
    latitude, longitude = get_lat_long(address)
    if latitude and longitude:
        stop_name, wheelchair_accessible = get_nearest_station(latitude, longitude)
        if stop_name:
            return render_template("station_result.html", station_name=stop_name, address=address, wheelchair_accessible=wheelchair_accessible)
        else:
            return render_template("oops.html")


if __name__ == '__main__':
    app.run(debug=True)

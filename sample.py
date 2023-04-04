from flask import Flask, render_template, request
from weather_helper import get_temp 

app = Flask(__name__)


@app.get('/temp/')
def temp_get():
    return render_template('weather-form.html')


@app.post('/temp/')
def temp_post():
    city_name = request.form['city']
    temperature = get_temp(city_name)
    return render_template('weather-result.html', city=city_name, temp=temperature)


@app.route("/")
# if the website domain is www.abc.com, http://www.abc.com/ will trigger the function below, hello()
@app.route('/hello/')  # http://www.abc.com/hello/ will trigger the function
@app.route(
    '/hello/<name>'
)  # if the URL has the pattern /hello/<name>, it will trigger the function by passing the name to it.
def hello(name=None):
    if name:
        # return f'<h1>Hello, {name}!</h1> <p style="color: red">I am super excited to learn Flask.</p>'
        return render_template('index.html', username=name)
    return "Hello, world!"


# Create another route like '/square/<number>', so the web app will display the square of the number


@app.route('/square/')
@app.route('/square/<number>')
# @app.route('/square/<int:number>')
def square(number=None):
    if number:
        return str(float(number) ** 2)
    return "You need to provide a number."


if __name__ == "__main__":
    app.run(debug=True)
from flask import Flask, render_template, request
import requests


app = Flask(__name__)
app.config['DEBUG'] = True


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == "POST":
        city = request.form['city']
        country = request.form['country']
        api_key = "c57baf757ae0865afd737c0980bdca81"
        weather_url = requests.get(f'http://api.openweathermap.org/data/2.5/weather?q={city},{country}&appid={api_key}&units=metric')

        weather_data = weather_url.json()

        temp = round(weather_data['main']['temp'])
        humidity = weather_data['main']['humidity']
        wind_speed = weather_data['wind']['speed']
        return render_template("result.html", temp=temp, humidity=humidity, wind_speed=wind_speed, city=city)

    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)

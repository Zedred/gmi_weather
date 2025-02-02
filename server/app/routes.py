from flask import render_template
from app import flask_app

@flask_app.route('/')
@flask_app.route('/index')
def index():
    user = {'username': 'Charles'}
    data = [
        {'date_time':'2024-10-12 12:00pm EST', 'TempC':20, 'TempF':72},
        {'date_time':'2024-10-12 12:15pm EST', 'TempC':21, 'TempF':74},
        {'date_time':'2024-10-12 12:30pm EST', 'TempC':21, 'TempF':72}]
    return render_template('index.html', title='Home', user=user, weather_data=data)


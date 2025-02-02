from flask import render_template, flash, redirect
from app import flask_app
from app.forms import LoginForm

@flask_app.route('/')
@flask_app.route('/index')
def index():
    user = {'username': 'Charles'}
    data = [
        {'date_time':'2024-10-12 12:00pm EST', 'TempC':20, 'TempF':72},
        {'date_time':'2024-10-12 12:15pm EST', 'TempC':21, 'TempF':74},
        {'date_time':'2024-10-12 12:30pm EST', 'TempC':21, 'TempF':72}]
    return render_template('index.html', title='Home', user=user, weather_data=data)

@flask_app.route('/login', methods=['GET','POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash('Login request for user {}, remember_me{}'.format(
            form.username.data, form.remember_me.data))
    return redirect(url_for('index'))

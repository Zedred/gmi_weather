import sqlalchemy as sa
import sqlalchemy.orm as so
from app import flask_app, db
from app.models import User, WeatherStation, WeatherDataPoint

@flask_app.shell_context_processor
def make_shell_context():
    return {
            'sa': sa, 
            'so':so, 
            'db':db, 
            'User':User, 
            'WeatherStation': WeatherStation, 
            'WeatherDataPoint':WeatherDataPoint
        }
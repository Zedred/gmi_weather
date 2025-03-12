from typing import Optional
import sqlalchemy as sa
import sqlalchemy.orm as so
import datetime as dt
from app import db

class User(db.Model):
    id: so.Mapped[int] = so.mapped_column(primary_key=True)
    username: so.Mapped[str] = so.mapped_column(sa.String(64), index=True,
        unique=True)
    email: so.Mapped[str] = so.mapped_column(sa.String(120), index=True,
        unique=True)
    password_hash: so.Mapped[Optional[str]] = so.mapped_column(sa.String(256))

    def __repr__(self):
        return '<User {}'.format(self.username)

class WeatherStation(db.Model):
    id:   so.Mapped[int] = so.mapped_column(primary_key=True)
    name: so.Mapped[str] = so.mapped_column(sa.String(64), index=True, unique=True)
    city: so.Mapped[Optional[str]] = so.mapped_column(sa.String(64))
    elevation: so.Mapped[Optional[int]] =so.mapped_column()
    latitude: so.Mapped[Optional[str]] = so.mapped_column(sa.String(12))
    longitutde: so.Mapped[Optional[str]] = so.mapped_column(sa.String(12))
    data: so.WriteOnlyMapped['WeatherDataPoint'] = so.relationship(back_populates='station')
    
class WeatherDataPoint(db.Model):
    date_time: so.Mapped[dt.datetime] = so.mapped_column(primary_key=True, default=lambda: dt.datetime.now(dt.timezone.utc))
    station_id: so.Mapped[int] = so.mapped_column(sa.ForeignKey(WeatherStation.id), index=True)
    station: so.Mapped[WeatherStation] = so.relationship(back_populates='data')
    sunrise_time: so.Mapped[Optional[dt.time]] = so.mapped_column(sa.Time)
    sunset_time: so.Mapped[Optional[dt.time]] = so.mapped_column(sa.Time)
    temperature: so.Mapped[float] = so.mapped_column(sa.Float)
    humidity: so.Mapped[int] = so.mapped_column(sa.Integer)
    dew_point: so.Mapped[float] = so.mapped_column(sa.Float)
    wind_speed: so.Mapped[float] = so.mapped_column(sa.Float)
    wind_direction: so.Mapped[int] = so.mapped_column(sa.Integer)
    wind_chill: so.Mapped[float] = so.mapped_column(sa.Float)
    heat_index: so.Mapped[float] = so.mapped_column(sa.Float)
    thw_index: so.Mapped[float] = so.mapped_column(sa.Float)
    barometer: so.Mapped[float] = so.mapped_column(sa.Float)
    rain_rate: so.Mapped[float] = so.mapped_column(sa.Float)
    solar_radiation: so.Mapped[int] = so.mapped_column(sa.Integer)
    uv_index: so.Mapped[float] = so.mapped_column(sa.Float)
    
    def __repr__(self):
        return '{}, {}F'.format(self.date_time, self.temperature)
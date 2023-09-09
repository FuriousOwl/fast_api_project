# Модель данных для магазинов
from db.base import Base
from sqlalchemy import Column, Integer, String
from geoalchemy2 import Geometry


class Osm_point(Base):
    __tablename__ = 'planet_osm_point'

    osm_id = Column(Integer, primary_key=True)
    amenity = Column(String)
    building = Column(String)
    water = Column(String)
    highway = Column(String)
    shop = Column(String)
    way = Column(Geometry)


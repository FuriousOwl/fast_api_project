from geoalchemy2 import Geometry
from sqlalchemy import Column, Integer, String

from db.base import Base


class OsmPoint(Base):
    __tablename__ = 'planet_osm_point'
    osm_id = Column(Integer, primary_key=True)
    way = Column(Geometry)


class ShopPoint(OsmPoint):
    shop = Column(String)


class AmenityPoint(OsmPoint):
    amenity = Column(String)


class BuildingPoint(OsmPoint):
    building = Column(String)


class WaterPoint(OsmPoint):
    water = Column(String)


class HighwayPoint(OsmPoint):
    highway = Column(String)

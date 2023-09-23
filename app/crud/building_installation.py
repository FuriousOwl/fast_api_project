from geoalchemy2 import WKTElement
from geoalchemy2.functions import ST_Intersects

from core.constants import Messages
from models.Points import BuildingPoint, WaterPoint


def post_installation(session, building_location):

    building_geometry = WKTElement(building_location, srid=4326)

    query = session.query(BuildingPoint).filter(ST_Intersects(building_geometry, WaterPoint.way))
    result = query.all()
    if result:
        return Messages.BUILDING_INSTALLATION_NOT_ALLOWED
    else:
        return Messages.BUILDING_INSTALLATION_ALLOWED

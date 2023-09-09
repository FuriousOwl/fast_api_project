from models.shop import Osm_point
from db.base import get_session
from geoalchemy2 import WKTElement
from geoalchemy2.functions import ST_Intersects


def post_installation(building_location: str):
    session = get_session()

    building_geometry = WKTElement(building_location, srid=4326)

    query = session.query(Osm_point).filter(ST_Intersects(building_geometry, Osm_point.way))
    result = query.all()
    print(result)
    if result:
        return {"message": "Установка здания в данном месте невозможна, так как оно пересекается с другими объектами."}
    else:
        return {"message": "Установка здания в данном месте возможна."}


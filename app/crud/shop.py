# Модуль для работы с данными о магазинах
from models.shop import Osm_point
from db.base import get_session
from geoalchemy2.functions import ST_DWithin, ST_AsText


def get_points():
    session = get_session()
    subquery = (
        session.query(Osm_point.osm_id)
        .filter(
            ST_DWithin(Osm_point.way, Osm_point.way, 600)
            & (Osm_point.osm_id != Osm_point.osm_id)
        )
        .distinct()
    )

    query = (
        session.query(Osm_point.osm_id, Osm_point.shop, ST_AsText(Osm_point.way).label("way"))
        .filter(~Osm_point.osm_id.in_(subquery))
        .filter(Osm_point.shop.isnot(None))
    )

    result = query.limit(10).all()
    data = [{"osm_id": row.osm_id, "shop": row.shop, "way": row.way[6:-1].split()} for row in result]

    return data

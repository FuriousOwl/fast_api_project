# Модуль для работы с данными о университетах
from models.shop import Osm_point
from db.base import get_session
from geoalchemy2.functions import ST_Buffer, ST_AsText, ST_Intersects


def get_buffer():
    session = get_session()

    fuel_subquerty = (
        session.query(ST_AsText(ST_Buffer(Osm_point.way, 200, quad_segs=8)).label("fuel_buffer"))
        .filter(Osm_point.amenity == 'fuel')
        .subquery()
    )

    university_subquery = (
        session.query(Osm_point.amenity, ST_AsText(Osm_point.way).label('way'))
        .filter(Osm_point.amenity == 'university')
        .subquery()
    )

    query = (
        session.query(
            fuel_subquerty.c.fuel_buffer.label("fuel_buffer"),
            university_subquery.c.way.label("university_way"),
            ST_Intersects(fuel_subquerty.c.fuel_buffer, university_subquery.c.way).label('intersects')
        )
    )

    result = query.all()
    data = [{"fuel_buffer": row.fuel_buffer, "university_way": row.university_way, "intersects": row.intersects}
            for row in result]

    print(data)

    return data

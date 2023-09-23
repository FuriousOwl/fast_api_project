from geoalchemy2.functions import ST_AsText, ST_Buffer, ST_Intersects

from models.Points import AmenityPoint


def get_buffer(session):

    fuel_subquery = (
        session.query(ST_AsText(ST_Buffer(AmenityPoint.way, 200, quad_segs=8)).label("fuel_buffer"))
        .filter(AmenityPoint.amenity == 'fuel')
        .subquery()
    )

    university_subquery = (
        session.query(AmenityPoint.amenity, ST_AsText(AmenityPoint.way).label('way'))
        .filter(AmenityPoint.amenity == 'university')
        .subquery()
    )

    query = (
        session.query(
            fuel_subquery.c.fuel_buffer.label("fuel_buffer"),
            university_subquery.c.way.label("university_way"),
            ST_Intersects(fuel_subquery.c.fuel_buffer, university_subquery.c.way).label('intersects')
        )
    )

    result = query.all()
    data = [{"fuel_buffer": row.fuel_buffer, "university_way": row.university_way, "intersects": row.intersects}
            for row in result]
    return data

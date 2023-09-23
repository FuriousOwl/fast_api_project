from geoalchemy2.functions import ST_AsText, ST_DWithin

from models.Points import ShopPoint


def get_points(session):
    subquery = (
        session.query(ShopPoint.osm_id)
        .filter(
            ST_DWithin(ShopPoint.way, ShopPoint.way, 600)
            & (ShopPoint.osm_id != ShopPoint.osm_id)
        )
        .distinct()
    )

    query = (
        session.query(ShopPoint.osm_id, ShopPoint.shop, ST_AsText(ShopPoint.way).label("way"))
        .filter(~ShopPoint.osm_id.in_(subquery))
        .filter(ShopPoint.shop.isnot(None))
    )

    result = query.limit(10).all()
    data = [{"osm_id": row.osm_id, "shop": row.shop, "way": row.way[6:-1].split()} for row in result]

    return data

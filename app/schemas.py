from pydantic import BaseModel


class Osm_point_validation(BaseModel): #подумать над названием класса
    osm_id: int
    amenity: str | None = None
    shop: str | None
    way: list[str]


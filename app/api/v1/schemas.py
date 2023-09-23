from pydantic import BaseModel


class ShopPointSchema(BaseModel):
    osm_id: int
    shop: str | None
    way: list[str]


class UniversityProhibitedZoneSchema(BaseModel):
    fuel_buffer: str
    university_way: str
    intersects: bool


class BuildingLocationSchema(BaseModel):
    building_location: str


class BuildingInstallationResponseSchema(BaseModel):
    message: str

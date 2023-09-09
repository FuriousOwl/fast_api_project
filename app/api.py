from fastapi import APIRouter
from schemas import Osm_point_validation
from crud.shop import get_points
from crud.building_installation import post_installation
from crud.university import get_buffer

router = APIRouter()


@router.get('/get_shop_1/', response_model=list[Osm_point_validation])
def get_data_1():
    return get_points()


@router.get('/get_intersects_2/')
def get_data_2():
    return get_buffer()


@router.post('/post_building_installation/')
def post_building_installation(building_location: str):
    return post_installation(building_location)

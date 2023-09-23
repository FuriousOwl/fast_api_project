from fastapi import APIRouter, Depends, status
from fastapi.exceptions import HTTPException
from sqlalchemy.orm import Session

from api.v1.schemas import (BuildingInstallationResponseSchema,
                            BuildingLocationSchema, ShopPointSchema,
                            UniversityProhibitedZoneSchema)
from core.constants import Messages
from crud.building_installation import post_installation
from crud.shop import get_points
from crud.university import get_buffer
from db.base import get_session

router = APIRouter()


@router.get('/unique_shops/', response_model=list[ShopPointSchema])
def get_unique_shops(
        session: Session = Depends(get_session)
):
    shops = get_points(session)
    if not shops:
        raise HTTPException(status_code=status.HTTP_204_NO_CONTENT)
    return shops


@router.get('/university_prohibited_zone/', response_model=list[UniversityProhibitedZoneSchema])
def get_university_prohibited_zone(
        session: Session = Depends(get_session)
):
    university_zone = get_buffer(session)
    if not university_zone:
        raise HTTPException(status_code=status.HTTP_204_NO_CONTENT)
    return university_zone


@router.post('/check_building_installation/', response_model=BuildingInstallationResponseSchema)
def post_check_building_installation(building_location_data: BuildingLocationSchema,
                                     session: Session = Depends(get_session)):
    building_location = building_location_data.building_location
    result = post_installation(session, building_location)
    if result == Messages.BUILDING_INSTALLATION_NOT_ALLOWED:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=result)
    elif result == Messages.BUILDING_INSTALLATION_ALLOWED:
        return {"message": result}
    else:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=Messages.SERVER_ERROR)

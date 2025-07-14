from fastapi import APIRouter
from src.routers.starwars_router import starwars_router
from src.routers.user_router import user_router

router = APIRouter()

@router.get('/', include_in_schema=False)
async def root():
    return {"message": "The Star Wars API is running!"}

router.include_router(user_router)
router.include_router(starwars_router)
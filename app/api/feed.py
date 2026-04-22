from fastapi import APIRouter
from ..database import SessionLocal
from ..models import EventFeed

router = APIRouter()

@router.get("/feed")
def get_feed():
    db = SessionLocal()
    data = db.query(EventFeed).all()
    db.close()
    return data

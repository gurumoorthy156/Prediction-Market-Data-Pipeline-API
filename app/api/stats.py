from fastapi import APIRouter
from ..database import SessionLocal
from ..models import Market, EventFeed

router = APIRouter()

@router.get("/stats/summary")
def stats():
    db = SessionLocal()

    total_markets = db.query(Market).count()
    total_events = db.query(EventFeed).count()

    db.close()

    return {
        "total_markets": total_markets,
        "total_events": total_events
    }

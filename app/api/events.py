from fastapi import APIRouter
from ..services.ingestion import get_events, get_event_details

router = APIRouter()


@router.get("/events")
def events():
    return get_events()


@router.get("/events/{event_ticker}")
def event_details(event_ticker: str):
    return get_event_details(event_ticker)

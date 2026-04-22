from fastapi import APIRouter
from ..services.ingestion import get_series

router = APIRouter()


@router.get("/series/{series_ticker}")
def series(series_ticker: str):
    return get_series(series_ticker)

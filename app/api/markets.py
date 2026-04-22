from fastapi import APIRouter, Query
from ..services.ingestion import (
    get_markets,
    get_market_details,
    get_orderbook
)

router = APIRouter()


@router.get("/markets")
def markets(
    series_ticker: str = Query(None),
    event_ticker: str = Query(None),
    status: str = Query(None)
):
    return get_markets(series_ticker, event_ticker, status)


@router.get("/markets/{ticker}")
def market_details(ticker: str):
    return get_market_details(ticker)


@router.get("/markets/{ticker}/orderbook")
def orderbook(ticker: str):
    return get_orderbook(ticker)

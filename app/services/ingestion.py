import requests
from ..database import SessionLocal
from ..models import Market

BASE_URL = "https://api.elections.kalshi.com/trade-api/v2"

def fetch_markets():
    try:
        res = requests.get(f"{BASE_URL}/markets")
        data = res.json()
        return data.get("markets", [])
    except:
        return []


def save_markets(markets):
    db = SessionLocal()

    for m in markets:
        exists = db.query(Market).filter(Market.ticker == m["ticker"]).first()

        if not exists:
            market = Market(
                ticker=m["ticker"],
                title=m.get("title", ""),
                yes_bid=m.get("yes_bid", 0),
                last_price=m.get("last_price", 0),
                volume_24h=m.get("volume_24h", 0)
            )
            db.add(market)

    db.commit()
    db.close()


import requests

BASE_URL = "https://api.elections.kalshi.com/trade-api/v2"


def fetch_data(endpoint, params=None):
    try:
        url = f"{BASE_URL}{endpoint}"
        res = requests.get(url, params=params)
        
        if res.status_code == 200:
            return res.json()
        elif res.status_code == 429:
            print("Rate limited... retry later")
            return {}
        else:
            return {}
    except Exception as e:
        print("Error:", e)
        return {}


def get_markets(series_ticker=None, event_ticker=None, status=None):
    params = {}

    if series_ticker:
        params["series_ticker"] = series_ticker
    if event_ticker:
        params["event_ticker"] = event_ticker
    if status:
        params["status"] = status

    data = fetch_data("/markets", params)
    return data.get("markets", [])

def get_market_details(ticker):
    data = fetch_data(f"/markets/{ticker}")
    return data

def get_orderbook(ticker):
    data = fetch_data(f"/markets/{ticker}/orderbook")
    return data


def get_events():
    data = fetch_data("/events")
    return data.get("events", [])

def get_event_details(event_ticker):
    data = fetch_data(f"/events/{event_ticker}")
    return data

def get_trades():
    data = fetch_data("/trades")
    return data.get("trades", [])

def get_series(series_ticker):
    data = fetch_data(f"/series/{series_ticker}")
    return data

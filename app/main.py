from fastapi import FastAPI
from .database import Base, engine

from .api import markets, feed, stats
from .api import events, trades, series

from .services.scheduler import start_scheduler

app = FastAPI()

Base.metadata.create_all(bind=engine)

# Existing
app.include_router(markets.router, prefix="/api")
app.include_router(feed.router, prefix="/api")
app.include_router(stats.router, prefix="/api")

# NEW APIs
app.include_router(events.router, prefix="/api")
app.include_router(trades.router, prefix="/api")
app.include_router(series.router, prefix="/api")

start_scheduler()

@app.get("/")
def home():
    return {"message": "Nora Backend Running"}

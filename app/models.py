from sqlalchemy import Column, Integer, String, Float, DateTime
from .database import Base
import datetime

class Market(Base):
    __tablename__ = "markets"

    id = Column(Integer, primary_key=True)
    ticker = Column(String, unique=True)
    title = Column(String)
    yes_bid = Column(Float)
    last_price = Column(Float)
    volume_24h = Column(Float)
    timestamp = Column(DateTime, default=datetime.datetime.utcnow)


class EventFeed(Base):
    __tablename__ = "feed"

    id = Column(Integer, primary_key=True)
    type = Column(String)
    headline = Column(String)
    severity = Column(Integer)
    created_at = Column(DateTime, default=datetime.datetime.utcnow)

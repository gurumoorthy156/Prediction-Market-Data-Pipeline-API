from pydantic import BaseModel

class MarketSchema(BaseModel):
    ticker: str
    title: str
    yes_bid: float
    last_price: float
    volume_24h: float

    class Config:
        from_attributes = True


class FeedSchema(BaseModel):
    type: str
    headline: str
    severity: int

    class Config:
        from_attributes = True

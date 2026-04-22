from ..database import SessionLocal
from ..models import Market, EventFeed

def detect_changes():
    db = SessionLocal()

    markets = db.query(Market).all()

    for m in markets:

        # Price change
        if abs(m.yes_bid - m.last_price) > 0.05:
            db.add(EventFeed(
                type="price_change",
                headline=f"{m.title} price moved",
                severity=5
            ))

        # Low activity → still create event (for demo)
        elif m.volume_24h == 0:
            db.add(EventFeed(
                type="low_volume",
                headline=f"{m.title} has no trading activity",
                severity=2
            ))

    db.commit()
    db.close()

from ..database import SessionLocal
from ..models import Market, EventFeed

def detect_changes():
    db = SessionLocal()

    markets = db.query(Market).all()

    for m in markets:
        if m.yes_bid and m.last_price:
            if abs(m.yes_bid - m.last_price) > 0.1:
                event = EventFeed(
                    type="price_change",
                    headline=f"{m.title} price moved significantly",
                    severity=5
                )
                db.add(event)

    db.commit()
    db.close()

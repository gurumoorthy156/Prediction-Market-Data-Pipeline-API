from apscheduler.schedulers.background import BackgroundScheduler
from .ingestion import fetch_markets, save_markets
from .detection import detect_changes

def job():
    markets = fetch_markets()
    save_markets(markets)
    detect_changes()


def start_scheduler():
    scheduler = BackgroundScheduler()
    scheduler.add_job(job, "interval", minutes=30)
    scheduler.start()

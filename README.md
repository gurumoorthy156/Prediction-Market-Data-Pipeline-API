# Nora Backend Assessment – Prediction Market Data Pipeline & API

## 📌 Overview

This project is a backend service that ingests live prediction market data from the Kalshi API, processes it to detect meaningful changes, and exposes the data through REST APIs.

The system is designed to simulate a real-world data pipeline powering a mobile or web application.

---

## 🚀 Features

### 1. Data Ingestion

* Fetches market data from Kalshi public API
* Supports:

  * Markets
  * Events
  * Trades
  * Series
* Runs on a scheduled interval (every 30 minutes)
* Stores data in SQLite database

---

### 2. Change Detection

Detects important market events such as:

* Price movement (> 0.10 difference)
* Basic anomaly detection on pricing

Each detected event is stored as a feed item with:

* Event type
* Headline
* Severity score
* Timestamp

---

### 3. REST API

#### Markets

* `GET /api/markets` → List all markets (with filters)
* `GET /api/markets/{ticker}` → Market details
* `GET /api/markets/{ticker}/orderbook` → Order book data

#### Events

* `GET /api/events` → List events
* `GET /api/events/{event_ticker}` → Event details

#### Trades

* `GET /api/trades` → Recent trades

#### Series

* `GET /api/series/{series_ticker}` → Series info

#### Feed

* `GET /api/feed` → Detected events feed

#### Stats

* `GET /api/stats/summary` → Summary statistics

---

## 🧱 Tech Stack

* **Backend Framework**: FastAPI
* **Database**: SQLite
* **ORM**: SQLAlchemy
* **Scheduler**: APScheduler
* **HTTP Client**: Requests

---

## ⚙️ Setup Instructions

### 1. Clone the repository

```
git clone <your-repo-url>
cd nora-backend
```

### 2. Create virtual environment

```
python -m venv venv
venv\Scripts\activate   (Windows)
```

### 3. Install dependencies

```
pip install -r requirements.txt
```

### 4. Run the application

```
uvicorn app.main:app --reload 
```

---

## 🌐 API Documentation

Once the server is running, open:

👉 http://127.0.0.1:8000/docs

FastAPI provides interactive Swagger UI for testing all endpoints.


from fastapi import APIRouter
from ..services.ingestion import get_trades

router = APIRouter()


@router.get("/trades")
def trades():
    return get_trades()

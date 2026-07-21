import random
import string

from fastapi import APIRouter, Depends, HTTPException
from fastapi.responses import RedirectResponse
from sqlalchemy.orm import Session

from database import get_db
from models import URL
from schemas import URLCreate

router = APIRouter()


def generate_short_code(length: int = 6):
    return "".join(
        random.choices(string.ascii_letters + string.digits, k=length)
    )


@router.post("/shorten")
def shorten_url(url_create: URLCreate, db: Session = Depends(get_db)):

    short_code = generate_short_code()

    while db.query(URL).filter(URL.short_code == short_code).first():
        short_code = generate_short_code()

    new_url = URL(
        long_url=url_create.long_url,
        short_code=short_code,
    )

    db.add(new_url)
    db.commit()
    db.refresh(new_url)

    return {
        "id": new_url.id,
        "short_code": new_url.short_code,
        "long_url": new_url.long_url,
    }


@router.get("/{short_code}")
def redirect(short_code: str, db: Session = Depends(get_db)):

    url = db.query(URL).filter(URL.short_code == short_code).first()

    if not url:
        raise HTTPException(status_code=404, detail="URL not found")

    return RedirectResponse(url.long_url)


@router.get("/stats/{short_code}")
def stats(short_code: str, db: Session = Depends(get_db)):

    url = db.query(URL).filter(URL.short_code == short_code).first()

    if not url:
        raise HTTPException(status_code=404, detail="URL not found")

    return {
        "id": url.id,
        "long_url": url.long_url,
        "short_code": url.short_code,
        "created_at": url.created_at,
    }

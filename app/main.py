from typing import Annotated

from fastapi import FastAPI, Query
from sqlmodel import select
from contextlib import asynccontextmanager
from app.models import Event
from app.db import init_db, SessionDep


@asynccontextmanager
async def lifespan(app: FastAPI):
    init_db()
    yield


app = FastAPI(lifespan=lifespan)


@app.post("/event/")
def create_event(event: Event, session: SessionDep) -> Event:
    session.add(event)
    session.commit()
    session.refresh(event)
    return event


@app.get("/events/")
def read_events(
    session: SessionDep,
    limit: Annotated[int, Query(le=100)] = 100,
) -> list[Event]:
    events = session.exec(select(Event).limit(limit)).all()
    return list(events)

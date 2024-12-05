# Calendar Backend

## TODO

- [x] Set up local database with docker
  - [x] Set up db migrations
- [ ] Connect db to GET endpoint for all calender items
- [ ] Set up CD
- [ ] Set up authentication (Google OAuth)
- [ ] Create all endpoints needed
  - [ ] POST - create calendar item
  - [ ] GET - get calendar items for specific date
- [ ] Set up email reminders

## Setup

To start a local DB for the first time:
```
docker-compose up -d --build
```

To start to local FastAPI dev server:
```
pdm run start
```

View api docs at [http://localhost:8000/docs](http://localhost:8000/docs).

### DB Migrations

Define the table models in `/app/models.py`, then to generate a new revision run:
```
pdm run alembic revision --autogenerate -m "{short revision description}"
```

To upgrade or downgrade:
```
pdm run alembic upgrade head
pdm run alembic downgrade -1
```


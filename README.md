# Calendar Backend

## TODO

- [x] Set up local database with docker
  - [ ] Set up db migrations
- [ ] Connect db to GET endpoint for all calender items
- [ ] Set up CD
- [ ] Set up authentication (Google OAuth)
- [ ] Create all endpoints needed
  - [ ] POST - create calendar item
  - [ ] GET - get calendar items for specific date
- [ ] Set up email reminders

## Contributing

To start a local DB:
```
docker-compose up -d --build
```

To start to local FastAPI dev server:
```
pdm run start
```

View api docs at [http://localhost:8000/docs](http://localhost:8000/docs).


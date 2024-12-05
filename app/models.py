from sqlmodel import Field, SQLModel


class Event(SQLModel, table=True):
    id: int = Field(default=0, primary_key=True)
    name: str = Field(index=True)
    datetime: int = Field(default=0)
    duration: int = Field(default=0)

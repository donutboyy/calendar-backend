from sqlmodel import Field, SQLModel


class Event(SQLModel, table=True):
    id: int = Field(default=0, primary_key=True)
    name: str = Field(index=True)
    datetime: int = Field(default=0)
    duration: int = Field(default=0)

class User(SQLModel):
    id: int= Field(primary_key=True, index=True)
    email: str = Field(unique=True)

class UserInDB(User, table=True):
    hashed_password: str = Field()

class Token(SQLModel):
    access_token: str
    token_type: str

class TokenData(SQLModel):
    email: str | None = None

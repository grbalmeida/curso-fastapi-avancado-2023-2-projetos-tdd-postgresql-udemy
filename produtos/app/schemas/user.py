import re
from pydantic import field_validator
from app.schemas.base import CustomBaseModel

class User(CustomBaseModel):
    username: str
    password: str

    @field_validator('username')
    def validate_username(cls, value):
        if not re.match('^([a-z]|[A-Z]|-|_|@)+$', value):
            raise ValueError('Invalid username')

        return value
# Dados de usuário

# name: string
# age: integer
# email: string

# user = {
#     "name": "Homelander",
#     "age": 41,
#     "email": "homelander@gmail"
# }

# print(user)

from pydantic import BaseModel, validator

class User(BaseModel):
    name: str
    age: int
    email: str

    @validator('email')
    def validate_email(cls, value):
        if '@' not in value:
            raise ValueError('Invalid email')
        return value

def f(user: User):
    user.email = 'teste@gmail.com'
    pass

user = User(name='Homelander', age=41, email='homelander@gmail.com')
print(user)
print(user.model_dump())
print(user.model_dump_json())

# user2 = User(name='Homelander', age='seila', email='homelander@gmail.com')
# Input should be a valid integer, unable to parse string as an integer [type=int_parsing, input_value='seila', input_type=str]

user2 = User(name='Homelander', age=41, email='homelander.gmail.com')
print(user2)
# Value error, Invalid email [type=value_error, input_value='homelander.gmail.com', input_type=str]
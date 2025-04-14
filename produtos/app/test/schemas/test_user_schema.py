from datetime import datetime
import pytest
from app.schemas.user import User, TokenData

def test_user_schema():
    user = User(username='Diogo', password='pass#')

    assert user.model_dump() == {
        'username': 'Diogo',
        'password': 'pass#'
    }

def test_user_schema_invalid_username():
    with pytest.raises(ValueError):
        user = User(username='João', password='pass#')

    with pytest.raises(ValueError):
        user = User(username='Joao#', password='pass#')

def test_token_data():
    expires_at = datetime.now()
    token_data = TokenData(
        access_token='token qualquer',
        expires_at=expires_at
    )

    assert token_data.model_dump() == {
        'access_token': 'token qualquer',
        'expires_at': expires_at
    }
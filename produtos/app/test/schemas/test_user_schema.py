import pytest
from app.schemas.user import User

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
import pytest
from rest_framework.test import APIClient

from app.account import services


class BruceAlmighty:
    """ class example of the user for test """
    username = 'king_heaven'
    email = 'architect@heaven.com'
    first_name = 'Bruce'
    last_name = 'Almighty'
    password = 'believe_in_me'


@pytest.fixture
def user():
    user_dc = services.UserDataClass(
        first_name=BruceAlmighty.first_name,
        last_name=BruceAlmighty.last_name,
        username=BruceAlmighty.username,
        email=BruceAlmighty.email,
        password=BruceAlmighty.password
    )

    user = services.create_user(user_dc=user_dc)

    return user


@pytest.fixture
def client():
    return APIClient()

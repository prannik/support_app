import pytest
from conftest import BruceAlmighty


@pytest.mark.django_db
def test_signup(client):
    payload = dict(
        username=BruceAlmighty.username,
        first_name=BruceAlmighty.first_name,
        last_name=BruceAlmighty.last_name,
        email=BruceAlmighty.email,
        password=BruceAlmighty.password
    )

    response = client.post('/api/user/signup/', payload)
    assert response.status_code == 201

    data = response.data

    assert data['username'] == BruceAlmighty.username
    assert data['email'] == BruceAlmighty.email
    assert data['first_name'] == BruceAlmighty.first_name
    assert data['last_name'] == BruceAlmighty.last_name
    assert 'password' not in data


@pytest.mark.django_db
def test_login(user, client):
    response = client.post('/api/user/login/', dict(email=BruceAlmighty.email, password=BruceAlmighty.password))
    data = response.data

    assert response.status_code == 200
    assert data['username'] == BruceAlmighty.username
    assert data['email'] == BruceAlmighty.email


@pytest.mark.django_db
def test_login_fail(client):
    response = client.post('/api/user/login/', dict(email='shang_tsung@heaven.com', password='your_soul_is_mine'))

    assert response.status_code == 400

import pytest
from app import app

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_home(client):
    rv = client.get('/')
    assert b'Selamat datang di API DevSecOps!' in rv.data
    assert rv.status_code == 200
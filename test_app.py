import pytest
from app import app

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_home_page(client):
    """Test home page loads successfully"""
    response = client.get('/')
    assert response.status_code == 200
    assert b'Flask Docker App' in response.data

def test_api_hello(client):
    """Test API endpoint returns correct JSON"""
    response = client.get('/api/hello')
    assert response.status_code == 200
    data = response.get_json()
    assert data['message'] == 'Hello from Flask!'

def test_invalid_route(client):
    """Test 404 on invalid route"""
    response = client.get('/invalid')
    assert response.status_code == 404

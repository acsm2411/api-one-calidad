import pytest
from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_index_route():
    response = client.get('/infoUsers/Roslyn.Rempel')
    assert response.status_code == 200

def test_index_route_no_content():
    response = client.get('/infoUsers/test')
    assert response.status_code == 204
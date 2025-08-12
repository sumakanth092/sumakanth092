def test_basic():
    assert 1 + 1 == 2

def test_home_route():
    from app import app
    client = app.test_client()
    response = client.get("/")
    assert response.status_code == 200
    assert b"Hello, CI/CD World!" in response.data

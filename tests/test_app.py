from app import app

def test_get_students():
    client = app.test_client()
    response = client .get('/get_students')
    assert response.status_code ==200
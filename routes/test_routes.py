# Import and register blueprint routes
from app import app

def test_about_page():
    """Test the about page route"""
    with app.test_client() as client:
        response = client.get('/about')
        assert response.status_code == 200
        assert b'About TennisAI' in response.data
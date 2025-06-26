import pytest
import json
from app import app as flask_app

@pytest.fixture
def app():
    """Create and configure a new app instance for each test."""
    yield flask_app

@pytest.fixture
def client(app):
    """A test client for the app that resets the state for each test."""
    with app.test_client() as client:
        # Reset the database before each test
        client.post('/testing/reset')
        yield client


def test_get_all_items_initially_empty(client):
    """Test that GET /items returns an empty dictionary and a 200 status code."""
    response = client.get('/items')
    assert response.status_code == 200
    assert response.json == {}

def test_create_item(client):
    """Test POST /items to create a new item."""
    new_item_data = {'name': 'item1', 'description': 'A test item'}

    response = client.post('/items',
                           data=json.dumps(new_item_data),
                           content_type='application/json')

    assert response.status_code == 201
    response_data = response.json
    assert response_data['name'] == new_item_data['name']
    assert 'id' in response_data

    # Verify the item was added by checking the main /items list
    get_all_response = client.get('/items')
    assert get_all_response.status_code == 200
    assert str(response_data['id']) in get_all_response.json

def test_get_one_item(client):
    """Test GET /items/<id> for an existing item."""
    # First, create an item to retrieve
    new_item_data = {'name': 'item_to_get', 'description': 'Details'}
    post_response = client.post('/items', data=json.dumps(new_item_data), content_type='application/json')
    assert post_response.status_code == 201
    item_id = post_response.json['id']

    # Now, get the item by its ID
    get_response = client.get(f'/items/{item_id}')
    assert get_response.status_code == 200
    assert get_response.json['id'] == item_id
    assert get_response.json['name'] == 'item_to_get'

def test_get_nonexistent_item(client):
    """Test GET /items/<id> for a non-existent item."""
    response = client.get('/items/999') # Assumes ID 999 does not exist
    assert response.status_code == 404

def test_update_item(client):
    """Test PUT /items/<id> to update an item."""
    # First, create an item
    new_item_data = {'name': 'item_to_update', 'description': 'Original'}
    post_response = client.post('/items', data=json.dumps(new_item_data), content_type='application/json')
    item_id = post_response.json['id']

    # Now, update it
    update_data = {'name': 'updated_name', 'description': 'Updated description'}
    put_response = client.put(f'/items/{item_id}', data=json.dumps(update_data), content_type='application/json')
    assert put_response.status_code == 200
    assert put_response.json['name'] == 'updated_name'
    assert put_response.json['description'] == 'Updated description'

    # Verify the update with a GET
    get_response = client.get(f'/items/{item_id}')
    assert get_response.json['name'] == 'updated_name'

def test_update_nonexistent_item(client):
    """Test PUT /items/<id> for a non-existent item."""
    update_data = {'name': 'wont_work'}
    response = client.put('/items/999', data=json.dumps(update_data), content_type='application/json')
    assert response.status_code == 404

def test_delete_item(client):
    """Test DELETE /items/<id> to remove an item."""
    # Create an item
    post_response = client.post('/items', data=json.dumps({'name': 'item_to_delete'}), content_type='application/json')
    item_id = post_response.json['id']

    # Delete it
    delete_response = client.delete(f'/items/{item_id}')
    assert delete_response.status_code == 200
    assert delete_response.json['message'] == 'Item deleted'

    # Verify it's gone
    get_response = client.get(f'/items/{item_id}')
    assert get_response.status_code == 404

def test_delete_nonexistent_item(client):
    """Test DELETE /items/<id> for a non-existent item."""
    response = client.delete('/items/999')
    assert response.status_code == 404

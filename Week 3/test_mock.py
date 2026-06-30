from unittest.mock import patch
import requests

# Function to simulate database call
def get_user():
    return "Original User"

# Function to fetch data from API
def get_post():
    response = requests.get("https://jsonplaceholder.typicode.com/posts/1")
    return response.json()


# Mock Database Call
with patch("__main__.get_user", return_value="Mock User"):
    print("Database Call:", get_user())


# Mock HTTP Request
with patch("requests.get") as mock_get:

    mock_get.return_value.json.return_value = {
        "id": 1,
        "title": "Mock Post"
    }

    print("HTTP Request:", get_post())

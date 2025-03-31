import pytest
import requests

testcases = [
    ("http://localhost:8000/add/2/2", 4, "Addition of 2 and 2"),
    ("http://localhost:8000/subtract/2/2", 0, "Subtraction of 2 from 2"),
    ("http://localhost:8000/multiply/2/2", 4, "Multiplication of 2 and 2"),
]

@pytest.mark.parametrize("url, expected, description", testcases)
def test_api(url, expected, description):
    response = requests.get(url)
    result = response.json()["result"]
    assert result == expected, f"{description}. Expected {expected}, got {result}"
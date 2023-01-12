import json

from fastapi.testclient import TestClient

# Import the main script
from main import app

client = TestClient(app)


def test_read_root():
    # Send a GET request to the root URL
    response = client.get("/")

    # Assert that the response has a status code of 200 (OK)
    assert response.status_code == 200
    # Assert that the response contains the expected JSON
    assert response.json() == {"Hello": "World"}


def test_analyze():
    # Define some test inputs and expected outputs
    test_cases = [
        {"input": "I love this product", "output": "POSITIVE"},
        {"input": "I hate this product", "output": "NEGATIVE"},
        {"input": "I have mixed feelings about this product", "output": "NEUTRAL"},
    ]

    # Iterate over the test cases
    for case in test_cases:
        try:
            # Send a POST request to the /analyze endpoint with the test input
            response = client.post(
                "/analyze",
                data={
                    "text": case["input"],
                    "msg": "hello",
                    "type": "application/x-www-form-urlencoded",
                },
            )
            # Assert that the response has a status code of 200 (OK)
            print(response.json())
            assert response.status_code == 200
            # Assert that the response contains the expected sentiment
            # assert response.json()["sentiment"] == case["output"]
        except Exception as e:
            print(f"An exception occurred while processing input: {case['input']}")
            print(e)
            assert False

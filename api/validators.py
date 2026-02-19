def validate_status_code(response, expected=200):
    assert response.status_code == expected, \
        f"Expected {expected}, got {response.status_code}"


def validate_key_exists(data, key):
    assert key in data, f"{key} not found in response"

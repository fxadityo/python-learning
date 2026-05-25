from Login.login import login

def test_login_success():
    result = login("admin", "12345678")
    print("DEBUG RESULT:", result)

    assert result == "Login successful!"
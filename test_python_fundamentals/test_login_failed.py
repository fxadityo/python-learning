from login import login

def test_login_failed():
    result = login("admin", "WrongPassword")
    print("DEBUG RESULT:", result)

    assert result == "Login failed. Please check your credentials."
from login_multiple_success import login_multiple

def test_login_multiple_success():
    
    # Test case for successful login
    data = [
        {"username": "admin1", "password": "password1"}, # Password Benar
        {"username": "admin2", "password": "password2"}, # Password Benar
        {"username": "admin3", "password": "password3"}  # Password Benar
    ]

    results = login_multiple(data)
    

    # Cek satu per satu hasil login, kalau ada yang tidak True, langsung gagalkan test dan beritahu index akun yang bermasalah
    for i, result in enumerate(results):
        assert result == True, f"Login failed for user index {i}"
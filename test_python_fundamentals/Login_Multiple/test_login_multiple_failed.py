from login_multiple_failed import login_multiple

def test_login_multiple_failed():
    
    # Test case for failed login
    data = [
        {"username": "admin1", "password": "password2"}, # Password Salah
        {"username": "admin2", "password": "password5"}, # Password Salah
        {"username": "admin3", "password": "password6"}  # Password Salah
    ]

    results = login_multiple(data)
    

    # Cek satu per satu hasil login, kalau ada yang tidak True, langsung gagalkan test dan beritahu index akun yang bermasalah
    for i, result in enumerate(results):
        assert result == False, f"Login should have failed for user index {i}"
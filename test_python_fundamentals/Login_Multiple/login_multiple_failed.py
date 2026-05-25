def login_multiple(data):
    # Data akun yang valid
    valid_users = [    
        {"username": "admin1", "password": "password1"}, # Password Salah
        {"username": "admin2", "password": "password2"}, # Password Salah
        {"username": "admin3", "password": "password3"}  # Password Salah
    ]

    results = []
    for cred in data:
        is_valid = any(
            user["username"] == cred["username"] and user["password"] == cred["password"]
            for user in valid_users
        )
        results.append(is_valid)
    
    return results  # [False, False, False]
from login_multiple_failed import login_multiple

def test_login_multiple_failed():
    
    # Test case for failed login
    data = [
        {"username": "admin1", "password": "password2"}, # Password Salah
        {"username": "admin2", "password": "password5"}, # Password Salah
        {"username": "admin3", "password": "password6"}  # Password Salah
    ]

    print("\n========== MULAI TEST LOGIN GAGAL ==========")
    
    results = login_multiple(data)
    
    print(f"Hasil Semua Login: {results}")  # Output: [False, False, False]

    # Cek satu per satu hasil login, kalau ada yang tidak True, langsung gagalkan test dan beritahu index akun yang bermasalah
    for i, result in enumerate(results):
        username = data[i]["username"]
        print(f"Login untuk {username} {'berhasil' if result else 'gagal'}")
        password = data[i]["password"]
        print(f"Password yang digunakan: {password}") 

        assert result == False, f"Login should have failed for user index {i}"
        print(f"Login untuk {username} gagal karena password tidak sesuai.")

    print("\n========== SELESAI TEST LOGIN GAGAL ==========")
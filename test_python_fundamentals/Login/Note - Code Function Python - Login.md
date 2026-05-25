# 📒 Catatan Function Python — Login Single

---

## 📄 File: `login.py`

```python
def login(username, password):
    if username == "admin" and password == "12345678":
        return "Login successful!"
    else:
        return "Login failed. Please check your credentials."
```

| Function / Syntax | Kegunaan |
|---|---|
| `def login(username, password)` | Mendefinisikan fungsi `login` yang menerima 2 parameter: `username` dan `password` |
| `if username == "admin" and password == "12345678"` | Mengecek apakah username dan password sesuai secara bersamaan |
| `and` | Operator logika — kedua kondisi harus `True` agar blok `if` dijalankan |
| `return "Login successful!"` | Mengembalikan string sukses jika kredensial benar |
| `else` | Blok yang dijalankan jika kondisi `if` tidak terpenuhi |
| `return "Login failed. ..."` | Mengembalikan string gagal jika kredensial salah |

---

## 📄 File: `test_login_failed.py`

```python
from login import login

def test_login_failed():
    result = login("admin", "WrongPassword")
    print("DEBUG RESULT:", result)
    assert result == "Login failed. Please check your credentials."
```

| Function / Syntax | Kegunaan |
|---|---|
| `from login import login` | Mengambil fungsi `login` dari file `login.py` |
| `def test_login_failed()` | Mendefinisikan fungsi test gagal (dikenali pytest karena prefix `test_`) |
| `login("admin", "WrongPassword")` | Memanggil fungsi login dengan password yang salah |
| `result` | Variabel untuk menyimpan nilai kembalian dari fungsi `login` |
| `print("DEBUG RESULT:", result)` | Menampilkan hasil login ke terminal untuk keperluan debug |
| `assert result == "Login failed. ..."` | Memastikan result sesuai pesan gagal, jika tidak → test error |

---

## 📄 File: `test_login_success.py`

```python
from login import login

def test_login_success():
    result = login("admin", "12345678")
    print("DEBUG RESULT:", result)
    assert result == "Login successful!"
```

| Function / Syntax | Kegunaan |
|---|---|
| `from login import login` | Mengambil fungsi `login` dari file `login.py` |
| `def test_login_success()` | Mendefinisikan fungsi test sukses (dikenali pytest karena prefix `test_`) |
| `login("admin", "12345678")` | Memanggil fungsi login dengan kredensial yang benar |
| `result` | Variabel untuk menyimpan nilai kembalian dari fungsi `login` |
| `print("DEBUG RESULT:", result)` | Menampilkan hasil login ke terminal untuk keperluan debug |
| `assert result == "Login successful!"` | Memastikan result sesuai pesan sukses, jika tidak → test error |

---

## 🧠 Ringkasan Cepat Semua Function

| Function | Kegunaan Singkat |
|---|---|
| `def` | Mendefinisikan fungsi |
| `return` | Mengembalikan nilai dari fungsi |
| `if / else` | Percabangan kondisi |
| `and` | Kedua kondisi harus True |
| `print()` | Tampilkan output ke terminal |
| `assert` | Validasi kondisi, gagal → stop & error |
| `import` | Mengambil fungsi/modul dari file lain |
| `==` | Operator perbandingan, mengecek kesamaan nilai |

---

> 💡 **Tips Pytest:** Tambahkan flag `-s` agar `print()` muncul di terminal
> ```
> pytest nama_file.py -s
> pytest nama_file.py -s -v    (lebih detail)
> ```

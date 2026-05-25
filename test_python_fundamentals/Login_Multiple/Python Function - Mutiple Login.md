# 📒 Catatan Function Python — Login Multiple

---

## 📄 File: `login_multiple.py`

```python
def login_multiple(data):
    valid_users = [ ... ]
    results = []
    for cred in data:
        is_valid = any(
            user["username"] == cred["username"] and user["password"] == cred["password"]
            for user in valid_users
        )
        results.append(is_valid)
    return results
```

| Function / Syntax                      | Kegunaan                                                                                       |
| -------------------------------------- | ---------------------------------------------------------------------------------------------- |
| `def login_multiple(data)`             | Mendefinisikan fungsi bernama `login_multiple` yang menerima 1 parameter `data` (list of dict) |
| `valid_users = [...]`                  | Menyimpan daftar akun valid sebagai list of dictionary                                         |
| `results = []`                         | Membuat list kosong sebagai wadah hasil validasi login                                         |
| `for cred in data`                     | Looping tiap kredensial (username & password) dari input `data`                                |
| `any(...)`                             | Mengecek apakah **minimal 1 kondisi** dalam iterable bernilai `True`                           |
| `user["username"] == cred["username"]` | Membandingkan username input dengan username yang valid                                        |
| `results.append(is_valid)`             | Menambahkan hasil validasi (`True`/`False`) ke list `results`                                  |
| `return results`                       | Mengembalikan list hasil validasi ke pemanggil fungsi                                          |

---

## 📄 File: `test_login_multiple_failed.py`

```python
from login_multiple_failed import login_multiple

def test_login_multiple_failed():
    data = [ ... ]
    print("\n========== MULAI TEST LOGIN GAGAL ==========")
    results = login_multiple(data)
    print(f"Hasil Semua Login: {results}")
    for i, result in enumerate(results):
        username = data[i]["username"]
        print(f"Login untuk {username} {'berhasil' if result else 'gagal'}")
        password = data[i]["password"]
        print(f"Password yang digunakan: {password}")
        assert result == False, f"Login should have failed for user index {i}"
        print(f"Login untuk {username} gagal karena password tidak sesuai.")
    print("\n========== SELESAI TEST LOGIN GAGAL ==========")
```

| Function / Syntax                                | Kegunaan                                                                |
| ------------------------------------------------ | ----------------------------------------------------------------------- |
| `from ... import ...`                            | Mengambil fungsi `login_multiple` dari file `login_multiple_failed.py`  |
| `def test_login_multiple_failed()`               | Mendefinisikan fungsi test (dikenali pytest karena prefix `test_`)      |
| `print()`                                        | Menampilkan teks ke terminal (gunakan `pytest -s` agar muncul)          |
| `f"..."`                                         | F-string — menyisipkan variabel langsung di dalam string                |
| `login_multiple(data)`                           | Memanggil fungsi login dan menyimpan hasilnya ke `results`              |
| `for i, result in enumerate(results)`            | Looping hasil login sambil mendapatkan index (`i`) dan nilai (`result`) |
| `enumerate()`                                    | Menghasilkan pasangan index + nilai saat looping                        |
| `data[i]["username"]`                            | Mengakses username dari data berdasarkan index ke-`i`                   |
| `'berhasil' if result else 'gagal'`              | Ternary operator — pilih teks berdasarkan kondisi `True`/`False`        |
| `assert result == False`                         | Memastikan result adalah `False`, jika tidak → test gagal & error       |
| `f"Login should have failed for user index {i}"` | Pesan error yang tampil jika assert gagal                               |

---

## 📄 File: `test_login_multiple_success.py`

```python
from login_multiple_success import login_multiple

def test_login_multiple_success():
    data = [ ... ]
    results = login_multiple(data)
    for i, result in enumerate(results):
        assert result == True, f"Login failed for user index {i}"
```

| Function / Syntax                     | Kegunaan                                                                  |
| ------------------------------------- | ------------------------------------------------------------------------- |
| `from ... import ...`                 | Mengambil fungsi `login_multiple` dari file `login_multiple_success.py`   |
| `def test_login_multiple_success()`   | Mendefinisikan fungsi test sukses (dikenali pytest karena prefix `test_`) |
| `login_multiple(data)`                | Memanggil fungsi login dan menyimpan hasilnya ke `results`                |
| `for i, result in enumerate(results)` | Looping hasil login sambil mendapatkan index dan nilai                    |
| `assert result == True`               | Memastikan result adalah `True`, jika tidak → test gagal & error          |
| `f"Login failed for user index {i}"`  | Pesan error yang tampil jika assert gagal                                 |

---

## 🧠 Ringkasan Cepat Semua Function

| Function         | Kegunaan Singkat                         |
| ---------------- | ---------------------------------------- |
| `def`            | Mendefinisikan fungsi                    |
| `return`         | Mengembalikan nilai dari fungsi          |
| `print()`        | Tampilkan output ke terminal             |
| `append()`       | Tambah elemen ke akhir list              |
| `enumerate()`    | Loop dengan index otomatis               |
| `any()`          | True jika minimal 1 kondisi terpenuhi    |
| `assert`         | Validasi kondisi, gagal → stop & error   |
| `f"..."`         | F-string untuk sisipkan variabel ke teks |
| `for ... in ...` | Perulangan / looping                     |
| `import`         | Mengambil fungsi/modul dari file lain    |

---

> 💡 **Tips Pytest:** Tambahkan flag `-s` agar `print()` muncul di terminal
> ```
> pytest nama_file.py -s -v
> ```

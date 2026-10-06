"""Studi Kasus 3 - Sistem Keamanan Akun & Audit Log Login.

Menggunakan RegEx untuk validasi, class User dengan @property,
dan decorator (closure) untuk pencatatan audit trail otomatis.
"""

import re
from datetime import datetime
from functools import wraps

POLA_USERNAME = re.compile(r"^[A-Za-z0-9]{5,}$")  # alfanumerik, min 5 karakter
POLA_PASSWORD = re.compile(r"^(?=.*\d).{8,}$")  # min 8 karakter, ada angka


class User:
    """Model pengguna dengan username & password terenkapsulasi."""

    def __init__(self, username, password):
        self.username = username  # lewat setter -> tervalidasi
        self.password = password

    @property
    def username(self):
        return self._username

    @username.setter
    def username(self, nilai):
        if not POLA_USERNAME.fullmatch(nilai):
            raise ValueError(
                "Username minimal 5 karakter, hanya huruf dan angka (tanpa spasi/simbol)"
            )
        self._username = nilai

    @property
    def password(self):
        return "*" * len(self._password)  # password tidak pernah dibuka apa adanya

    @password.setter
    def password(self, nilai):
        if not POLA_PASSWORD.fullmatch(nilai):
            raise ValueError("Password minimal 8 karakter dan wajib memuat angka")
        self._password = nilai

    def cek_password(self, kandidat):
        return self._password == kandidat


def audit_log(fungsi):
    """Decorator: mencatat timestamp, username, dan status login."""

    @wraps(fungsi)
    def pembungkus(username, password, *args, **kwargs):
        waktu = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        try:
            hasil = fungsi(username, password, *args, **kwargs)
            status = "BERHASIL"
            alasan = ""
            return hasil
        except ValueError as err:
            status = "DITOLAK"
            alasan = f" | Alasan: {err}"
            return None
        finally:
            print(f"[{waktu}] User: {username!r:<14} | Status: {status}{alasan}")

    return pembungkus


@audit_log
def login(username, password):
    """Logika otentikasi murni (pencatatan ditangani decorator)."""
    pengguna = User(username, password)  # validasi regex terjadi di property
    return pengguna


def main():
    print("=== AUDIT LOG PERCOBAAN LOGIN ===\n")
    print("Skenario 1: username tidak sesuai aturan")
    login("ab", "rahasia123")
    login("user name!", "rahasia123")

    print("\nSkenario 2: password pendek / tanpa angka")
    login("mahasiswa01", "abc123")
    login("mahasiswa01", "passwordsaja")

    print("\nSkenario 3: login sukses")
    pengguna = login("mahasiswa01", "rahasia123")
    print(f"\nObjek User dibuat -> username={pengguna.username}, password={pengguna.password}")


if __name__ == "__main__":
    main()

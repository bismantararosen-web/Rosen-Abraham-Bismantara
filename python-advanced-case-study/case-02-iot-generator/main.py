"""Studi Kasus 2 - Streaming Data Sensor IoT Hemat Memori.

Data suhu diproduksi satu per satu oleh generator (yield) dan dikonsumsi
bertahap lewat next(), tanpa pernah disimpan dalam satu list besar.
"""

import random
import time

SUHU_MIN = 15.0
SUHU_MAX = 38.0
JUMLAH_BACAAN = 12


def sensor_suhu(jumlah=None, seed=42):
    """Generator suhu simulasi (15.0 - 38.0 C).

    Jika jumlah None, aliran bersifat tak terbatas seperti sensor sungguhan.
    """
    rng = random.Random(seed)
    n = 0
    while jumlah is None or n < jumlah:
        yield round(rng.uniform(SUHU_MIN, SUHU_MAX), 1)
        n += 1


def kategori_suhu(suhu):
    """Dingin < 20, Normal 20-30, Panas > 30."""
    if suhu < 20:
        return "Dingin"
    if suhu <= 30:
        return "Normal"
    return "Panas"


def main():
    aliran = sensor_suhu()  # generator tak terbatas, tidak memakai memori list
    print(f"Tipe aliran data : {type(aliran).__name__} (iterator, bukan list)")
    print(f"\n{'Bacaan':<8}{'Suhu (C)':>10}   Status")
    print("-" * 32)

    for nomor in range(1, JUMLAH_BACAAN + 1):
        suhu = next(aliran)  # data diminta satu per satu
        print(f"{nomor:<8}{suhu:>10.1f}   {kategori_suhu(suhu)}")
        time.sleep(0.05)  # simulasi jeda antar pembacaan sensor

    print("-" * 32)
    print(f"Selesai: {JUMLAH_BACAAN} bacaan diproses satu per satu tanpa menyimpan list.")


if __name__ == "__main__":
    main()

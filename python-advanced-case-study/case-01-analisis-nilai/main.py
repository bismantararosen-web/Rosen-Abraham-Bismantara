"""Studi Kasus 1 - Analisis Nilai Mahasiswa.

Menghitung nilai akhir, memfilter mahasiswa berprestasi, membuat ranking,
dan mengumumkan mahasiswa terbaik memakai list comprehension, lambda,
filtering, dan sorted().
"""

BOBOT_TUGAS = 0.30
BOBOT_UTS = 0.30
BOBOT_UAS = 0.40
BATAS_PRESTASI = 80

data_mahasiswa = [
    {"nama": "Aisyah", "nim": "230101", "tugas": 85, "uts": 80, "uas": 88},
    {"nama": "Budi", "nim": "230102", "tugas": 70, "uts": 65, "uas": 75},
    {"nama": "Cantika", "nim": "230103", "tugas": 90, "uts": 85, "uas": 92},
    {"nama": "Dimas", "nim": "230104", "tugas": 78, "uts": 82, "uas": 79},
    {"nama": "Eka", "nim": "230105", "tugas": 60, "uts": 70, "uas": 68},
]


def hitung_nilai_akhir(mhs):
    """Mengembalikan nilai akhir berbobot (dibulatkan 2 desimal)."""
    return round(
        mhs["tugas"] * BOBOT_TUGAS + mhs["uts"] * BOBOT_UTS + mhs["uas"] * BOBOT_UAS,
        2,
    )


def cetak_tabel(judul, daftar):
    print(f"\n{judul}")
    print("-" * 62)
    print(f"{'No':<4}{'NIM':<10}{'Nama':<12}{'Tugas':>6}{'UTS':>6}{'UAS':>6}{'Akhir':>9}")
    print("-" * 62)
    for i, m in enumerate(daftar, start=1):
        print(
            f"{i:<4}{m['nim']:<10}{m['nama']:<12}"
            f"{m['tugas']:>6}{m['uts']:>6}{m['uas']:>6}{m['nilai_akhir']:>9.2f}"
        )
    print("-" * 62)


def main():
    # 1. Hitung nilai akhir (list comprehension + dict unpacking)
    hasil = [{**m, "nilai_akhir": hitung_nilai_akhir(m)} for m in data_mahasiswa]
    cetak_tabel("1. NILAI AKHIR SELURUH MAHASISWA", hasil)

    # 2. Filter mahasiswa berprestasi (> 80) tanpa for bertingkat
    berprestasi = list(filter(lambda m: m["nilai_akhir"] > BATAS_PRESTASI, hasil))
    print(f"\n2. MAHASISWA BERPRESTASI (nilai akhir > {BATAS_PRESTASI})")
    print("   " + ", ".join(f"{m['nama']} ({m['nilai_akhir']:.2f})" for m in berprestasi))

    # 3. Ranking dari tertinggi ke terendah
    ranking = sorted(hasil, key=lambda m: m["nilai_akhir"], reverse=True)
    cetak_tabel("3. RANKING MAHASISWA (tertinggi -> terendah)", ranking)

    # 4. Mahasiswa terbaik
    terbaik = ranking[0]
    print("\n4. MAHASISWA TERBAIK")
    print(f"   Nama        : {terbaik['nama']}")
    print(f"   NIM         : {terbaik['nim']}")
    print(f"   Tugas       : {terbaik['tugas']}")
    print(f"   UTS         : {terbaik['uts']}")
    print(f"   UAS         : {terbaik['uas']}")
    print(f"   Nilai Akhir : {terbaik['nilai_akhir']:.2f}")


if __name__ == "__main__":
    main()

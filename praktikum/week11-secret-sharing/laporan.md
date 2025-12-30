# Laporan Praktikum Kriptografi
Minggu ke-: 11
Topik: Shamir’s Secret Sharing  
Nama: Faiz Al Mubarok  
NIM: [NIM Mahasiswa]  
Kelas: 5IKRB

---

## 1. Tujuan
( Tujuan dari praktikum ini adalah untuk memahami konsep Shamir’s Secret Sharing (SSS), mengimplementasikan pembagian rahasia ke beberapa bagian (shares), serta merekonstruksi kembali rahasia tersebut menggunakan jumlah share minimum sesuai nilai threshold. )

---

## 2. Dasar Teori
( Shamir’s Secret Sharing (SSS) adalah skema kriptografi yang digunakan untuk membagi sebuah rahasia menjadi beberapa bagian (shares), di mana rahasia asli hanya dapat direkonstruksi jika minimal sejumlah share tertentu (threshold k) digabungkan. Skema ini diperkenalkan oleh Adi Shamir pada tahun 1979.

Prinsip dasar SSS menggunakan polinomial berderajat (k−1) dalam aritmetika modular. Nilai rahasia disimpan sebagai konstanta polinomial, sedangkan share merupakan pasangan nilai (x, f(x)). Dengan menggunakan interpolasi Lagrange, rahasia dapat direkonstruksi kembali jika tersedia minimal k buah share yang valid.

Keamanan Shamir’s Secret Sharing terletak pada fakta bahwa kurang dari k share tidak memberikan informasi apa pun tentang rahasia. Hal ini menjadikan SSS sangat aman untuk manajemen kunci dan distribusi data sensitif. )
---

## 3. Alat dan Bahan
(- Python 3.x  
- Visual Studio Code  
- Git dan akun GitHub  
- Library secretsharing  )

---

## 4. Langkah Percobaan
(Tuliskan langkah yang dilakukan sesuai instruksi.  
Contoh format:
1. Membuat folder praktikum/week11-secret-sharing/ beserta subfolder src, screenshots, dan file laporan.md.
2. Menginstal library secretsharing menggunakan perintah pip install secretsharing.
3. Membuat file secret_sharing.py di dalam folder src.
4. Menuliskan kode program untuk membagi dan merekonstruksi rahasia.
5. Menjalankan program dengan perintah python secret_sharing.py.
6. Mengambil screenshot hasil pembagian dan rekonstruksi rahasia.
---

## 5. Source Code


```python
from secretsharing import SecretSharer

secret = "KRIPUPB2025"

secret_hex = secret.encode().hex()

shares = SecretSharer.split_secret(secret_hex, 3, 5)
print("Shares:", shares)

recovered_hex = SecretSharer.recover_secret(shares[:3])
recovered = bytes.fromhex(recovered_hex).decode()

print("Recovered secret:", recovered)

```
)

---


## 6. Hasil dan Pembahasan
![Hasil Eksekusi](screenshots/hasil.png)

---

## 7. Jawaban Pertanyaan
(Jawab pertanyaan diskusi yang diberikan pada modul.  
- Pertanyaan 1: Keuntungan utama Shamir Secret Sharing adalah peningkatan keamanan, karena rahasia tidak pernah disimpan atau dibagikan secara utuh. Jika satu atau beberapa share bocor, rahasia tetap aman selama jumlah share belum mencapai threshold.
- Pertanyaan 2: hreshold (k) menentukan jumlah minimum share yang dibutuhkan untuk merekonstruksi rahasia. Semakin besar nilai k, semakin tinggi tingkat keamanannya, tetapi juga mengurangi fleksibilitas dalam proses pemulihan rahasia.
-Pertanyaan 3: Shamir Secret Sharing banyak digunakan dalam manajemen kunci cryptocurrency, di mana kunci privat dompet dibagi ke beberapa pihak agar tidak ada satu pihak pun yang memegang kendali penuh.  
)
---

## 8. Kesimpulan
(Shamir’s Secret Sharing merupakan metode yang aman dan efektif untuk mendistribusikan rahasia.  )

---

## 9. Daftar Pustaka
(Cantumkan referensi yang digunakan.  
Contoh:  
- Shamir, A. (1979). How to Share a Secret. Communications of the ACM.
- Stinson, D. R. (2019). Cryptography: Theory and Practice.  )

---

## 10. Commit Log
(Tuliskan bukti commit Git yang relevan.  
Contoh:
```
commit abc12345
Author: Faiz Al Mubarok <huahuh3@gmail.com>
Date:   2025-12-30

    week2-cryptosystem: implementasi Caesar Cipher dan laporan )
```

# DevSecOps Pipeline - Flask API

## 1. Nama Aplikasi & Fungsinya
**FlaskUserAPI** adalah aplikasi REST API sederhana yang mengelola data pengguna. Aplikasi ini memiliki endpoint untuk menampilkan pesan selamat datang dan mencari pengguna berdasarkan username dari database SQLite.

## 2. Bahasa/Framework yang Digunakan
- **Bahasa:** Python 3.9
- **Framework:** Flask
- **Testing:** Pytest
- **SAST Tool:** Bandit

## 3. Cara Menjalankan Aplikasi
1. Clone repository ini: `git clone https://github.com/[username-anda]/devsecops-p5-[nim-anda].git`
2. Masuk ke direktori: `cd devsecops-p5`
3. Install dependensi: `pip install -r requirements.txt`
4. Inisialisasi database: `python models.py`
5. Jalankan aplikasi: `python app.py`

## 4. Overview Pipeline CI/CD (DevSecOps)
Pipeline diimplementasikan menggunakan **GitHub Actions** dengan dua job utama:
- **Build:** Menginstal dependensi dan menjalankan unit test menggunakan Pytest.
- **SAST Scan:** Bergantung pada job build, menggunakan tool **Bandit** untuk memindai kerentanan keamanan pada kode (seperti deteksi SQL Injection). Dilengkapi dengan skrip Quality Gate yang akan menggagalkan pipeline jika ditemukan kerentanan berisiko tinggi.
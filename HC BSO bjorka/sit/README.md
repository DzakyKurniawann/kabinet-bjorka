# SIT – Sistem Informasi Terintegrasi

Sistem Informasi Terintegrasi mahasiswa untuk kegiatan, iuran, rekrutmen, dan pengumpulan tugas.

---

## 🚀 Cara Menjalankan Backend & Frontend

### 1. Jalankan Langsung (Windows)
Cukup jalankan script runner berikut di terminal:
```bash
py run.py
```
atau double-click file **`start.bat`**.

Server otomatis menyajikan seluruh halaman web dan REST API di:
- **Localhost (Laptop ini):** `http://localhost:5000`
- **Jaringan LAN / Wi-Fi (Bisa diakses dari HP):** `http://<IP_KOMPUTER>:5000`

---

## 🌐 Cara Mempublikasikan (Online ke Internet / Public)

Ada 3 opsi mudah untuk mempublikasikan sistem ini ke publik:

### Opsi A: Menggunakan Cloudflare Tunnel (Gratis, Cepat, Tanpa Akun)
Jalankan di terminal:
```bash
npx untun@latest tunnel http://localhost:5000
```
atau jika punya `cloudflared`:
```bash
cloudflared tunnel --url http://localhost:5000
```
Kamu akan langsung mendapatkan URL publik HTTPS (contoh: `https://sit-demo.trycloudflare.com`).

### Opsi B: Menggunakan Ngrok (Gratis)
1. Unduh [ngrok](https://ngrok.com/) atau jalankan:
   ```bash
   ngrok http 5000
   ```
2. Bagikan URL HTTPS yang diberikan oleh ngrok kepada dosen atau teman.

### Opsi C: Deploy ke Cloud (Render / Railway / PythonAnywhere)
Proyek ini sudah dilengkapi file:
- `requirements.txt`
- `run.py`
- `backend/app.py`

Cukup hubungkan repository GitHub ini ke [Render.com](https://render.com) (Web Service gratis):
- **Build Command:** `pip install -r requirements.txt`
- **Start Command:** `python run.py`

---

## 🗄️ Fitur Penyimpanan Data (Backend & Database)

Sistem menggunakan database **SQLite** (`backend/sit.db`) yang otomatis dibuat dan diisi data awal saat server pertama kali dijalankan:

1. **Autentikasi Mahasiswa:**
   - Registrasi dan login dengan validasi NIM & Password.
   - Session tersimpan secara aman.
2. **Manajemen Kalender & Agenda (CRUD):**
   - Tambah, ubah, dan hapus event, tugas, iuran, dan rekrutmen melalui **Admin Console** (`/admin`).
   - Perubahan langsung tersimpan permanen di database dan muncul di **Kalender** (`/kalender`).
3. **Pengumpulan Tugas & Pembayaran Iuran (Upload File):**
   - Mahasiswa dapat mengunggah bukti transfer atau berkas tugas dalam format PDF.
   - File tersimpan di folder `uploads/` di server dan dapat dibuka langsung oleh admin.
4. **Verifikasi Admin:**
   - Admin dapat menerima/menolak bukti yang dikirim mahasiswa secara real-time.
5. **Profil Mahasiswa:**
   - Ubah nama, program studi, dan angkatan.
   - Unggah foto profil (tersimpan di server).

---

## 📂 Struktur Direktori

```
sit/
├── backend/
│   ├── app.py          # Server Flask & REST API
│   └── sit.db          # Database SQLite (dibuat otomatis)
├── css/
│   └── style.css       # Desain antarmuka
├── js/
│   ├── common.js       # Client API & helper sinkronisasi
│   ├── login.js        # Logika login & register
│   ├── kalender.js     # Logika kalender, filter, & upload tugas/iuran
│   ├── profil.js       # Logika profil mahasiswa & riwayat
│   └── admin.js        # Logika Admin Console & verifikasi
├── uploads/            # Direktori berkas PDF & foto yang diunggah
├── index.html          # Halaman Masuk / Register
├── kalender.html       # Halaman Kalender & Iuran
├── profil.html         # Halaman Profil Mahasiswa
├── admin.html          # Halaman Admin Console
├── run.py              # Script utama untuk menjalankan server
├── start.bat           # Launcher klik ganda untuk Windows
└── requirements.txt    # Dependensi Python
```


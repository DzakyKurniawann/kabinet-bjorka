# kabinet-bjorka
Membuat website informasi HIMA Informatika Unsoed

## 1. Deskripsi Permasalahan

* **Kelebihan Beban Informasi (*Information Overload*):** Pengandalan WhatsApp Group (WAG) sebagai media utama koordinasi menyebabkan informasi penting (seperti tenggat waktu tugas, pendaftaran panitia, dan instruksi iuran) sering kali tertumpuk dan tenggelam oleh ratusan pesan percakapan kasual setiap harinya.
* **Hambatan Komunikasi & Keterbatasan Platform:** Sifat komunikasi digital yang *asynchronous* serta keterbatasan aplikasi pesan instan (seperti risiko terhapusnya pesan atau anggota baru tidak bisa mengakses riwayat obrolan lama) memicu keterlambatan respons, ketimpangan informasi, dan kesalahan fatal dalam pelaksanaan kegiatan.
* **Infrastruktur Kampus yang Stagnan:** Situs web institusi/himpunan yang ada saat ini umumnya hanya memuat data profil formal yang minim serta jarang diperbarui, sehingga kurang memberikan fungsi praktis bagi operasional dan aktivitas harian mahasiswa.


## 2. Solusi yang Dikembangkan

* **Pusat Informasi Terintegrasi berbasis Web:** Mengembangkan portal web dinamis sebagai pusat kendali (*central hub*) aktivitas mahasiswa dengan menggeser paradigma komunikasi dari model *push* (didorong melalui grup obrolan) menjadi model *pull & centralized* (informasi disimpan secara persisten di web dan diakses saat dibutuhkan).
* **Modul dan Fitur Utama:**
* **Manajemen Acara & Kalender Terintegrasi:** Papan buletin digital interaktif yang dilengkapi jadwal dinamis, detail lokasi/waktu, serta dokumen pendukung (TOR, panduan lomba, tugas ospek).
* **Pusat Rekrutmen & Pengumpulan Tugas Terpadu:** Platform satu pintu untuk pendaftaran panitia/magang dan pengumpulan tugas beserta dasbor kelulusan/umpan balik bagi administrator.
* **Dasbor Transparansi Pembayaran via Integrasi Spreadsheet:** Display data *real-time* status pembayaran mahasiswa yang terhubung langsung dengan spreadsheet bendahara tanpa memberikan akses edit ke publik.
* **Otentikasi & Dasbor Personal:** Akses aman berbasis NIM/kredensial sah yang menampilkan rekap partisipasi, jadwal acara, dan status rekrutmen tiap pengguna.


## 3. Teknologi yang Digunakan

* **Antarmuka Pengguna (*Frontend*):** HTML, CSS, dan *framework* **Bootstrap (via CDN)** untuk merancang tampilan yang responsif di berbagai perangkat tanpa beban instalasi lokal.
* **Sisi Server (*Backend*):** Bahasa pemrograman **Python** menggunakan *framework* **Flask** yang ringan, *template engine* **Jinja2** untuk rendering halaman, serta basis data **MySQL** untuk penyimpanan data pengguna, acara, dan pendaftaran.
* **Integrasi Data Pembayaran:** **Google Sheets API** menggunakan *service account* (*read-only*) untuk membaca data spreadsheet bendahara dan memunculkannya pada dasbor web, dilengkapi sistem *caching* (penyimpanan sementara) untuk efisiensi API.
* **Manajemen Kode & Kolaborasi:** **GitHub** (fitur *branching*, *pull requests*, dan *issues*) untuk kolaborasi pengembangan paralel, serta penggunaan *environment variables* untuk mengamankan kredensial sensitif (*API keys*).
* **Penyebaran (*Deployment*):** Layanan *hosting* gratis berbasis Python yang memungkinkan portal diakses secara mandiri dan dapat dihubungkan langsung dari situs web himpunan yang sudah ada.

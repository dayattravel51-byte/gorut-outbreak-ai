# GORUT-OUTBREAK AI v45

## Perubahan utama
1. Halaman awal kembali menggunakan login.
2. Pilihan pengguna:
   - Surveilans Puskesmas dan Rumah Sakit
   - Surveilans Dinkes Kabupaten
   - Surveilans Dinkes Provinsi
   - Admin
3. Semua kategori pengguna memiliki akses operasional menu yang sama.
4. Pengguna selain Admin wajib mendaftar:
   - nama user
   - password
   - nomor WhatsApp
   - jenis pengguna
5. Setelah pendaftaran tersedia tombol WhatsApp Admin ke **082290150334** dengan pesan otomatis:
   > Izin Admin, saya mau login pada aplikasi Outbreak.
6. Status pengguna baru = MENUNGGU IZIN ADMIN.
7. Setelah Admin menjawab “silahkan”, Admin menandai akun sebagai DIIZINKAN pada menu Persetujuan Pengguna. Setelah itu pengguna dapat login.
8. Tidak ada pembayaran, subscription, atau masa akses 7 hari pada alur v45.
9. Kuesioner penyakit diintegrasikan langsung ke form Tambah/Edit Kasus.
10. Jawaban kuesioner disimpan pada `case.answers`.
11. Field epidemiologi inti dipetakan otomatis dari jawaban kuesioner jika tersedia: ID kasus, nama, umur, jenis kelamin, onset, status, outcome, alamat, desa, kecamatan, kabupaten, provinsi, puskesmas, latitude, longitude.
12. `case.answers` ikut dikirim pada sinkronisasi backend sebagai `questionnaire_response`.
13. Ditambahkan Audit Kuesioner v45.

## Audit statis v45
- 34 penyakit/sindrom pada Disease Library.
- 597 pertanyaan spesifik penyakit.
- 34/34 memiliki pertanyaan spesifik.
- Tidak ditemukan duplikasi label pertanyaan spesifik.
- Mesin integrasi jawaban ke `case.answers` aktif.

## Catatan penting
Audit struktural tidak berarti instrumen digital ini identik/verbatim dengan formulir resmi Kementerian Kesehatan. Sebelum digunakan sebagai instrumen resmi lapangan, setiap modul perlu divalidasi terhadap pedoman/formulir Kemenkes yang berlaku dan versi program terkait.

## Mode penyimpanan
Autentikasi v45 yang dibuat di browser menggunakan localStorage. Ini cocok untuk prototipe/instalasi lokal. Untuk deployment multi-perangkat/multi-user yang aman, autentikasi, persetujuan, dan data pengguna perlu ditegakkan di backend (misalnya Supabase/PostgreSQL) sehingga tidak dapat dimanipulasi dari browser.

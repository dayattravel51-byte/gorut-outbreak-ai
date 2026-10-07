# GORUT-OUTBREAK AI v8 — Backend Online

## 1. Tujuan
v8 mempertahankan mode offline-first v7 dan menambahkan fondasi backend PostgreSQL/Supabase.

## 2. Komponen
- Frontend: `index.html`
- Public survey: `public_survey.html`
- Database: `supabase-schema.sql`
- Konfigurasi browser: `backend-config.example.js`
- Disease/questionnaire engine: berada di frontend dan dapat dipindahkan ke tabel `diseases` + `questionnaires`.

## 3. Menyiapkan Supabase
1. Buat project Supabase.
2. Buka SQL Editor.
3. Jalankan `supabase-schema.sql`.
4. Aktifkan Email/Password Authentication jika ingin login email.
5. Buat user petugas/admin melalui Supabase Auth.
6. Salin URL project dan public anon/publishable key.
7. Salin `backend-config.example.js` menjadi `backend-config.js`, lalu isi nilai tersebut.
8. Ubah `enabled: true`.
9. Upload semua file frontend ke hosting HTTPS.

## 4. Keamanan
- Jangan menaruh `service_role` key di HTML/JavaScript.
- RLS harus tetap aktif.
- Untuk deployment Dinkes, tambahkan kebijakan admin kabupaten/provinsi/pusat menggunakan role pada `profiles`.
- Data by-name-by-address termasuk data sensitif; batasi akses, audit log, retensi, dan backup sesuai kebijakan instansi dan regulasi yang berlaku.

## 5. Public survey
`public_survey.html` dirancang untuk URL seperti:
`public_survey.html?survey=<public_token>`

Response masuk ke `survey_responses`; petugas dapat menghubungkannya ke kasus setelah verifikasi.

## 6. Offline → online
Alur target:
`Form lokal → IndexedDB → outbox → koneksi tersedia → upload → server ACK → outbox ditandai selesai`.

Jangan menghapus data lokal hanya karena browser kembali online. Hapus/arsipkan setelah ACK server diterima.

## 7. Master kuesioner
Versi v8 masih menandai instrumen sebagai **perlu validasi akhir**. Sebelum dipakai sebagai formulir resmi, setiap modul penyakit harus dibandingkan dengan pedoman/formulir Kemenkes yang berlaku pada tanggal penetapan, diberi nomor versi, tanggal validasi, dan penanggung jawab.

## 8. Roadmap v9
- Login Supabase nyata + RBAC admin kabupaten/provinsi/pusat.
- Sync engine dua arah dengan conflict handling.
- Public survey dinamis dari questionnaire schema.
- Statistical service: RR, OR, CI 95%, Fisher/chi-square, regresi logistik.
- GIS layer Puskesmas/desa dan cluster analysis.
- PDF laporan investigasi.
- AI epidemiologist melalui server-side API, tanpa API key di browser.

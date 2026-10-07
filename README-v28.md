# GORUT-OUTBREAK AI v28 — Production/SaaS Foundation

## Perubahan utama
- PE/KLB disease-aware: laporan memilih penyakit/sindrom sebelum template diterapkan.
- Tombol hapus per record utama: kasus, kontak, spesimen, kunjungan lapangan, alert, investigasi.
- Pilihan penyakit untuk analisis dan laporan.
- Registrasi Premium Rp30.000 / 7 hari, konfirmasi WhatsApp 082290150334.
- Admin tidak dibatasi masa akses.
- Fondasi subscription server-side melalui Supabase Auth/PostgreSQL.
- Registration request, subscription, audit log, secure activation function, dan access-status helper.
- LocalStorage tetap tersedia untuk mode offline/demo, tetapi tidak boleh dianggap sebagai enforcement keamanan produksi.

## Deployment produksi
1. Buat project Supabase.
2. Jalankan schema dasar lalu `supabase-schema-v28.sql` di SQL Editor.
3. Isi `backend-config.js` dengan URL project dan publishable/anon key.
4. Aktifkan Supabase Auth Email.
5. Buat akun admin, lalu set role profil menjadi `admin_kabupaten`/`admin_provinsi`/`admin_pusat` secara aman dari SQL Editor.
6. Untuk aktivasi pembayaran, admin memverifikasi transfer secara manual dan memanggil fungsi `activate_premium_7d(registration_id)` dari sesi admin.
7. Jangan pernah menaruh service-role key di frontend.
8. Gunakan HTTPS dan kebijakan backup database.

## Catatan pembayaran
Versi ini tidak mengklaim verifikasi transfer otomatis. Pembayaran Rp30.000 ke BNI 0599687726 a.n. Hidayat diverifikasi manual oleh admin. Otomatisasi payment gateway memerlukan provider dan kredensial resmi yang belum disediakan.

## Keamanan
Data kesehatan/epidemiologi dapat sensitif. Sebelum penggunaan operasional, lakukan uji RLS, backup/restore, audit akses, minimisasi PII, dan validasi instrumen program.

## File penting
- `index.html` — UI aplikasi
- `app.js` — frontend logic
- `supabase-schema.sql` — database + RLS + subscription functions
- `DEPLOYMENT-v28.md` — langkah deployment
- `backend-config.example.js` — contoh konfigurasi publik Supabase

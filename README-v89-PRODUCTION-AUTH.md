# GORUT OUTBREAK AI v89 — Production Authentication

v89 melanjutkan v88 dan memfokuskan aplikasi pada operasional surveilans.
Simulation Lab tidak menjadi bagian dari paket produksi.

## Fitur v89
- Supabase Auth email/password sebagai gerbang akses ketika backend diaktifkan.
- Profil pengguna otomatis dibuat dengan role `viewer` saat user Auth baru dibuat.
- Role operasional: `admin`, `surveilans`, `puskesmas`, `rumah_sakit`, `tgc`, `viewer`.
- Admin menetapkan role dan fasilitas melalui tabel `profiles`.
- RLS tetap menjadi lapisan keamanan utama; frontend tidak dipercaya untuk membatasi data.
- Mode lokal tetap tersedia ketika `backend-config.js` masih `enabled:false`.

## Aktivasi
1. Buat project Supabase.
2. Jalankan `supabase/001_initial_schema.sql` pada SQL Editor.
3. Jalankan migration public survey bila dibutuhkan.
4. Isi `backend-config.js` dengan URL project dan public anon/publishable key.
5. Ubah `enabled` menjadi `true`.
6. Buat akun operator melalui Supabase Auth.
7. Administrator mengisi `profiles.role` dan `profiles.facility_id`.
8. Uji RLS menggunakan akun dari setiap role sebelum memasukkan data nyata.

## Keamanan
- Jangan pernah menaruh `service_role` key di browser.
- Jangan menyimpan password sendiri di localStorage untuk mode produksi.
- Data kesehatan individu hanya boleh dimasukkan setelah kebijakan akses, retensi, backup, dan tata kelola internal Dinkes ditetapkan.

# GORUT OUTBREAK AI v91 — Command Center Integration

v91 menjadikan Supabase sebagai sumber data operasional saat backend aktif, sementara localStorage/IndexedDB tetap menjadi cache kerja offline.

## Perubahan
- Simulation Lab dihapus dari paket produksi.
- Setelah autentikasi berhasil, aplikasi mencoba memuat investigations, cases, contacts, specimens, field visits, dan alerts dari Supabase.
- Viewer tidak memuat data mentah; dashboard memakai `dashboard_counts()`.
- Sinkronisasi manual diikuti refresh data server.
- Saat perangkat kembali online, sinkronisasi dicoba otomatis.
- Investigasi dan alert membawa `facility_id` dari profil pengguna Puskesmas/RS.
- Normalisasi status kasus/outcome/contact agar sesuai enum Supabase.
- Tambahan SQL `003_v91_command_center.sql` untuk hardening dan ringkasan alert agregat.

## Urutan SQL Supabase
1. `001_initial_schema.sql`
2. `002_facility_rls_hardening.sql`
3. `003_v91_command_center.sql`

## Konfigurasi
Salin `backend-config.example.js` menjadi `backend-config.js`, lalu isi URL Supabase dan public anon/publishable key. Jangan pernah menaruh service-role key di browser.

## Uji sebelum data nyata
Buat akun uji untuk setiap role dan fasilitas. Pastikan:
- Puskesmas A tidak dapat membaca data Puskesmas B.
- RS A tidak dapat membaca data Puskesmas.
- TGC hanya melihat investigasi yang dimiliki/dibuatnya.
- Surveilans/Admin dapat melihat data kabupaten sesuai kebijakan.
- Viewer hanya memperoleh agregat dashboard.
- Insert investigasi/alert dari Puskesmas/RS otomatis membawa `facility_id`.

## Catatan privasi
Jangan memasukkan data pasien nyata sebelum RLS diuji dan master fasilitas resmi telah dimasukkan. Gunakan data uji anonim selama UAT.

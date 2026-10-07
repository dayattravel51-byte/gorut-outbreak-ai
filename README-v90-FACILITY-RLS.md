# GORUT OUTBREAK AI v90 — Facility-Based Access & RLS Hardening

v90 memperketat akses data operasional berdasarkan role, fasilitas, dan kepemilikan investigasi.

## Role
- `admin`: seluruh wilayah + administrasi pengguna/fasilitas.
- `surveilans`: seluruh data operasional kabupaten.
- `puskesmas`: hanya investigasi/data yang terhubung ke `facility_id` miliknya.
- `rumah_sakit`: hanya investigasi/data yang terhubung ke `facility_id` miliknya.
- `tgc`: investigasi yang dibuat/ditugaskan kepada akun tersebut.
- `viewer`: tidak mendapatkan raw operational records; gunakan agregat dashboard.

## Urutan instalasi
1. Jalankan `supabase/001_initial_schema.sql`.
2. Jalankan `supabase/002_facility_rls_hardening.sql`.
3. Isi `facilities` dengan master fasilitas resmi. Gunakan `FACILITY-MASTER-TEMPLATE.csv` sebagai format, jangan menebak nama/kode fasilitas.
4. Buat akun operator melalui Supabase Auth.
5. Isi `profiles.role` dan `profiles.facility_id` oleh admin.
6. Uji dengan akun terpisah untuk setiap role.

## Pengujian minimum
- Puskesmas A tidak dapat membaca investigasi Puskesmas B.
- Rumah Sakit A tidak dapat membaca investigasi Puskesmas.
- TGC hanya dapat membaca investigasi yang dibuat/ditugaskan kepadanya.
- Viewer tidak dapat membaca kasus/kontak/spesimen mentah.
- Admin dapat mengelola profiles dan fasilitas.
- Surveilans dapat melihat seluruh data operasional.

## Catatan keamanan
RLS adalah kontrol server-side. Jangan mengandalkan penyembunyian menu frontend sebagai keamanan. Jangan menaruh service-role key di browser. Sebelum data pasien nyata digunakan, tetapkan SOP akses, audit, retensi, backup, dan ekspor data.

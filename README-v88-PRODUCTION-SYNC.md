# GORUT OUTBREAK AI v88 — Production Sync Foundation

## Perubahan utama
-  dihapus dari aplikasi dan dokumentasi.
- UI operasional tetap dipertahankan: SKDR, PE/KLB, kasus, kontak, spesimen, kunjungan lapangan, GIS, analisis, laporan, dan admin.
- Sinkronisasi browser → Supabase diselaraskan dengan schema `supabase/001_initial_schema.sql`.
- `testBackend()` memeriksa tabel `profiles`, bukan tabel `diseases` yang tidak ada pada schema v87.
- Tidak ada service-role key di frontend.

## Urutan deployment
1. Buat project Supabase Free.
2. Jalankan `supabase/001_initial_schema.sql` di SQL Editor.
3. Isi `backend-config.js` dengan URL project dan public anon/publishable key.
4. Buat akun pengguna melalui Supabase Auth.
5. Isi `profiles` untuk menetapkan role dan fasilitas.
6. Uji login, RLS, `Uji Koneksi`, lalu `Sinkronisasi Sekarang`.
7. Publikasikan folder ke GitHub Pages.

## Catatan keamanan
Jangan memasukkan service-role key, password, OTP, atau credential pribadi ke repository. Data pasien hanya boleh diakses oleh pengguna yang memiliki kewenangan. Uji RLS dengan akun dari setiap role sebelum data nyata digunakan.

# Deployment GORUT-OUTBREAK AI v9

1. Buat project Supabase.
2. Jalankan `supabase-schema.sql` di SQL Editor.
3. Aktifkan Email/Password pada Authentication.
4. Buat akun petugas, lalu isi role pada tabel `profiles` sesuai kebutuhan.
5. Salin `backend-config.example.js` menjadi `backend-config.js` dan isi URL project serta anon/publishable key.
6. Host seluruh folder pada HTTPS (Vercel/Netlify/GitHub Pages/hosting instansi).
7. Buka aplikasi, login, pilih investigasi, lalu gunakan **Sinkronisasi Sekarang**.

Jangan memasukkan service_role key ke browser.

## Public survey
Dari investigasi pilih **Bagikan Kuesioner**. URL akan membawa `investigation` dan `disease` ke `public_survey.html`.

## Keamanan
Data by-name-by-address adalah data sensitif operasional. Gunakan HTTPS, RLS, akun individual, pembatasan role, audit log, backup, dan kebijakan retensi. Jangan membuka database langsung ke publik.

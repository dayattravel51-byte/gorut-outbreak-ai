# GORUT-OUTBREAK AI v30 — Production Release Candidate

v30 memfokuskan aplikasi pada alur SaaS produksi dan usability.

## Yang baru
- Production Admin Center: registrasi pending, aktivasi 7 hari, penolakan, pengguna, subscription, audit trail.
- Server-side access tetap authoritative melalui Supabase `my_access_status`.
- Admin unlimited/free; pengguna premium aktif selama 7 x 24 jam setelah aktivasi.
- Tombol Hapus pada record kasus, kontak, spesimen, kunjungan lapangan dan alert pada mode lokal.
- Login + registrasi premium tetap tersedia pada halaman awal.
- Informasi pembayaran: Rp30.000, BNI 0599687726 a.n. Hidayat, konfirmasi WhatsApp 082290150334.
- Verifikasi pembayaran tetap manual; tidak ada klaim integrasi mutasi bank otomatis.
- SQL tambahan v30 untuk `reject_registration()` dan `admin_subscription_summary`.

## Catatan keamanan
Untuk produksi, jalankan schema di Supabase, aktifkan Auth/Email confirmation sesuai kebijakan, gunakan HTTPS, dan uji RLS dengan akun biasa serta admin. Jangan menaruh service-role key di browser.

## Validasi
- `node --check app.js`
- `unzip -t` setelah packaging

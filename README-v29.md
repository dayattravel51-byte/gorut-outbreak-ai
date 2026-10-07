# GORUT-OUTBREAK AI v29 — Premium SaaS Foundation

## Fokus
v29 memperkuat fondasi produksi: subscription server-side, RLS admin/owner, premium access UX, countdown 7 hari, dan dashboard akses.

## Akses
- Premium: Rp30.000 / 7 hari setelah pembayaran diverifikasi admin.
- Konfirmasi WhatsApp: 082290150334.
- BNI: 0599687726 a.n. Hidayat.
- Admin: akses penuh dan gratis.

## Keamanan
Jika Supabase/backend diaktifkan, status akses authoritative berasal dari `my_access_status` dan `has_active_access()`. LocalStorage tidak menjadi sumber otoritas subscription.

RLS v29 menambahkan akses penuh untuk role admin pada data epidemiologi dan tetap mempertahankan scope owner untuk pengguna biasa.

## Mode offline
Mode offline/demo tetap tersedia untuk pelatihan. Jangan gunakan mode offline sebagai mekanisme subscription untuk layanan komersial.

## Deployment
1. Buat project Supabase.
2. Jalankan `supabase-schema-v28.sql` di SQL Editor.
3. Isi `backend-config.js` berdasarkan `backend-config.example.js`.
4. Buat user admin melalui Supabase Auth.
5. Set role admin pada `public.profiles`.
6. Uji RLS dengan akun pengguna biasa dan admin sebelum membuka layanan publik.
7. Deploy melalui HTTPS.

## Catatan pembayaran
Verifikasi transfer BNI pada v29 tetap manual. Tidak ada klaim integrasi mutasi rekening otomatis.

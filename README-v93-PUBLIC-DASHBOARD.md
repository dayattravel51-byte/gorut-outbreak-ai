# GORUT OUTBREAK AI v93 — Public Dashboard / KABAR SERGAP

v93 menambahkan lapisan publik yang terpisah dari data operasional internal.

## Komponen
- `public_dashboard.html` — dashboard publik agregat.
- `supabase/005_v93_public_dashboard.sql` — RPC agregat `public_dashboard_summary(days)`.
- Sidebar internal mendapat menu **KABAR SERGAP Publik**.

## Prinsip keamanan
Dashboard publik tidak melakukan query langsung ke tabel pasien/kasus. Data disediakan melalui RPC agregat dan tidak mengembalikan identitas individu.

Sebelum produksi:
1. Jalankan SQL 001 → 005 di Supabase.
2. Konfigurasikan `backend-config.js` dengan URL dan anon/publishable key.
3. Uji sebagai anon dan authenticated.
4. Pastikan tidak ada endpoint publik lain yang mengembalikan patient-level data.
5. Lakukan UAT sebelum memakai data kesehatan nyata.

## Alur arsitektur
`SKDR → Verifikasi → PE/KLB → Data agregat → KABAR SERGAP Publik`

Simulation Lab tetap dihapus dari produk.

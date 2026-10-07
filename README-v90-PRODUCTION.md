# GORUT OUTBREAK AI v90 — Production Foundation

v90 menghapus Simulation Lab dari produk operasional dan menambahkan facility-based access control serta RLS hardening.

### Fokus
- Authentication Supabase
- Role-based access
- Facility-based access
- Audit trail
- Offline/local queue tetap tersedia
- Dashboard agregat yang tidak mengekspos data individu kepada viewer

### Supabase
Jalankan berurutan:
1. `supabase/001_initial_schema.sql`
2. `supabase/002_facility_rls_hardening.sql`

Isi master fasilitas secara resmi melalui tabel `facilities`; gunakan template CSV sebagai struktur saja.

### Frontend
Isi `backend-config.js` dengan URL dan public anon/publishable key. Jangan pernah menggunakan service-role key di browser.

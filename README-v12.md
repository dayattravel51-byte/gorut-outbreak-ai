# GORUT-OUTBREAK AI v12

## Fokus
Mobile Field Investigation / TGC-Puskesmas: offline-first, GPS, catatan temuan, tindakan, foto lapangan, antrean sinkronisasi, dan ekspor CSV.

## Status
Prototype operasional untuk pengembangan. Jangan gunakan untuk registri kesehatan produksi sebelum validasi keamanan, privasi, RLS lintas-peran, manajemen media, backup, audit trail, dan uji lapangan.

## Data lapangan
Field visits tersimpan lokal pada mode offline. `syncStatus=pending` menjadi penanda untuk integrasi backend. Skema Supabase menambahkan tabel `field_visits`.

## Privasi
Foto dan koordinat adalah data sensitif secara operasional. Batasi akses, hindari menyimpan identitas pasien pada foto, dan terapkan kebijakan retensi/akses organisasi.

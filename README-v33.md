# GORUT-OUTBREAK AI v33 — Food Poisoning Edit & Data Quality Hardening

## Perbaikan utama
- Detail kasus keracunan pangan sekarang dapat **ditambah dan diedit** secara lengkap.
- Field waktu konsumsi, onset, masa inkubasi, gejala, sumber pangan, rawat inap, dan spesimen klinis dipertahankan saat edit.
- Validasi kualitas data laporan keracunan pangan:
  - sakit tidak boleh melebihi terpapar;
  - meninggal tidak boleh melebihi sakit;
  - Attack Rate tidak dihitung bila denominator terpapar belum tersedia/valid.
- Struktur laporan PE/KLB khusus keracunan pangan tetap dipertahankan.

## Validasi teknis
- `node --check app.js` berhasil.
- Seluruh file v32 dipertahankan; perubahan v33 bersifat incremental.

## Catatan produksi
Aplikasi masih memerlukan validasi lapangan terhadap instrumen program Kemenkes terbaru, pengujian backend/auth/RLS, dan uji penerimaan pengguna sebelum digunakan sebagai sistem produksi resmi.

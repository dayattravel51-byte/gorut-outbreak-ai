# GORUT-OUTBREAK AI v70 — Otomatisasi Desa → Puskesmas → Kecamatan

Basis: v69 Master Pembagian Desa per Puskesmas.

## Perubahan
- Desa/Kelurahan pada form Tambah/Edit Kasus menjadi pilihan dari master desa v69.
- Setelah desa dipilih, Kecamatan otomatis terisi.
- Puskesmas otomatis terisi pada field khusus dan disimpan ke data kasus sebagai `pkm`/`puskesmas`.
- Disimpan pula `wilayahKerja` dengan desa, puskesmas, kecamatan dan sumber master.
- Daftar Kasus tetap memakai kolom yang diusulkan: ID | Nama | Alamat | Desa/Kel. | Kecamatan | Umur | JK | Tanggal Onset | Gejala Utama | Status | Faktor Risiko (Kuesioner) | Outcome | Aksi.
- Tidak mengubah daftar 123 desa yang diberikan pengguna.

## Master wilayah
15 Puskesmas, 11 Kecamatan, 123 desa berdasarkan daftar 6 Oktober 2026.

## Catatan
Pemetaan otomatis ini adalah referensi wilayah kerja yang berasal dari master pengguna. Identifikasi RBI dari koordinat tetap dapat digunakan sebagai sumber administratif terpisah.

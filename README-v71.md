# GORUT-OUTBREAK AI v71 — Desa Acuan pada Tabel Isian Demografi

## Perubahan utama
- Kolom **Desa Acuan** pada Tabel Isian Demografi kini otomatis berisi seluruh daftar desa sesuai Master Pembagian Desa per Puskesmas yang diberikan pengguna.
- 15 Puskesmas, 11 Kecamatan, 123 desa.
- Daftar desa ditampilkan sebagai daftar multiline/read-only dan jumlah desa acuan ditampilkan per Puskesmas.
- Data Desa Acuan tidak perlu diketik ulang.
- Master desa tetap menjadi dasar pemetaan Desa → Puskesmas → Kecamatan pada Daftar Kasus.
- Data demografi (penduduk, laki-laki, perempuan, KK, luas, koordinat, catatan) tetap dapat diisi dan disimpan.

## Validasi
- app.js: `node --check` PASS
- daftar master desa terdeteksi: 15 Puskesmas / 123 desa

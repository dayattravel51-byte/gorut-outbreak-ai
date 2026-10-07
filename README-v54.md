# GORUT-OUTBREAK AI v54 — Advanced Outbreak Analysis

## Tambahan v54
- Mantel–Haenszel stratified analysis untuk OR/RR.
- Perbandingan crude vs adjusted dan skrining confounding berbasis perubahan estimasi.
- Multi-exposure screening dari variabel binary pada `case.answers`.
- Dose-response/kategori paparan untuk variabel numerik/ordinal sebagai analisis eksploratif.
- Narasi statistik otomatis untuk laporan PE/KLB.
- Ekspor hasil v54 ke JSON.
- Hasil v54 otomatis ditambahkan ke preview/HTML/TXT laporan PE/KLB bila analisis telah dijalankan.

## Catatan metodologis
Hasil adalah alat bantu analisis. Definisi operasional, reference category, coding binary, missing data, desain studi, confounding, effect modification, dan validitas data harus diverifikasi epidemiolog sebelum digunakan sebagai kesimpulan resmi. Ambang perubahan estimasi 10% adalah aturan skrining yang dapat diubah pengguna, bukan kriteria universal. Dose-response pada versi ini belum melakukan uji tren formal.

## Validasi paket
- `node --check app.js` harus lulus.
- ZIP diuji dengan `unzip -t`.

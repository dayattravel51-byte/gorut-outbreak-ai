# GORUT-OUTBREAK AI v24 — Research Studio

## Fokus
Research Studio mengubah modul penelitian menjadi alur kerja:

**Import → Preview → Cleaning/Recoding → Validation → Variable Dictionary → Analysis Pipeline → Statistical Analysis → Publication Tables → Research Report**

## Import data
Didukung:
- CSV
- TSV/TXT
- JSON array atau `{rows:[...]}` / `{data:[...]}`
- XLSX/XLS melalui SheetJS CDN saat koneksi internet tersedia

Dataset disimpan pada `localStorage` perangkat sebagai bagian dari `gorut-research-plan`.

## Cleaning
- missing-token normalization
- recoding dengan format `variabel | nilai_lama | nilai_baru`
- pemaksaan variabel numerik
- filter sederhana (`age>=18`, `sex=1`, dll.)
- pemeriksaan missing >20%
- pemeriksaan duplikasi penuh

## Analisis
Dataset penelitian menjadi sumber utama jika tersedia. Jika tidak, modul memakai data kasus investigasi aktif.

Desain yang didukung:
- Deskriptif/case series
- Cross-sectional
- Case-control
- Matched case-control
- Cohort
- Retrospective cohort outbreak
- Ecological
- Time-series
- Quasi-experimental

Mesin lanjutan v20–v23 tetap tersedia, termasuk 2×2, OR/RR/PR, Fisher, logistic regression, Mantel–Haenszel, matched/McNemar, person-time, Kaplan–Meier, robust Poisson, variable dictionary, DAG, dan publication tables.

## Catatan validitas
Output aplikasi adalah decision-support/statistical prototype. Sebelum tesis, disertasi, laporan resmi, atau publikasi:
1. cek coding dan definisi operasional;
2. cek desain sampling;
3. cek missing/outlier;
4. validasi estimasi dengan perangkat statistik independen (mis. R/Python/Stata/SPSS);
5. periksa asumsi model;
6. interpretasikan sesuai desain dan DAG;
7. jangan menyimpulkan kausalitas dari studi observasional tanpa dasar metodologis yang memadai.

## Arsitektur
`index.html` memuat UI; `app.js` memuat seluruh logic v19–v24. `index.html` secara eksplisit memuat `app.js`, sehingga Research Engine tidak lagi bergantung pada kode yang hanya tersimpan di arsip sumber.

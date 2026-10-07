# GORUT-OUTBREAK AI v35 — Priority Disease Instrument Pack

## Fokus
v35 melanjutkan v34 dengan pengayaan instrumen operasional untuk penyakit prioritas. Panel klinis-epidemiologi khusus tersedia pada input/edit kasus untuk:

- Campak
- DBD
- Malaria
- TB
- Difteri
- Pertusis
- AFP/Polio
- Rabies/GHPR
- Leptospirosis
- Avian Influenza
- Keracunan Pangan

## Alur
Instrumen penyakit → Investigasi → Input/Edit Kasus → Panel Prioritas → Kontak → Spesimen → Analisis → GIS → PE/KLB → Laporan.

## Penyimpanan
Data panel disimpan pada `case.priority` dengan penanda `_version: v35` dan `_disease`.

## Laporan
Laporan PE/KLB menampilkan agregasi Panel Klinis & Epidemiologi Prioritas pada bagian 3.6B. Untuk keracunan pangan, komponen khusus v32 tetap dipertahankan.

## Catatan validasi
Panel ini adalah adaptasi digital operasional, bukan klaim bahwa seluruh field merupakan reproduksi verbatim formulir resmi Kementerian Kesehatan. Sebelum digunakan sebagai instrumen resmi/program, validasikan terhadap pedoman, definisi kasus, formulir, dan versi regulasi yang berlaku.

## Validasi teknis
- `node --check app.js`: PASS
- ZIP integrity: PASS

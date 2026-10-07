# GORUT-OUTBREAK AI v23

## Research Data Management & Publication Engine

v23 melanjutkan Research Analysis Engine v22 dengan fokus pada manajemen variabel dan reproducible reporting.

### Fitur
- Variable dictionary: nama, label, tipe, peran (outcome/exposure/confounder/covariate).
- Variable discovery dari field kasus dan `answers.*`.
- Definisi operasional/coding dan catatan metodologi.
- DAG/kerangka analitik berbasis edge `penyebab → outcome`.
- Tabel karakteristik subjek otomatis (Table 1).
- Tabel kerangka analitik (Table 2).
- Ringkasan missing data.
- Integrasi tabel, DAG, dan catatan metodologi ke draft laporan penelitian.
- Ekspor draft laporan penelitian HTML.
- Ekspor research JSON v23.

### Alur yang disarankan
1. Tentukan desain penelitian.
2. Definisikan outcome, exposure, dan kovariat.
3. Isi variable dictionary dan coding.
4. Periksa data/missing.
5. Susun DAG atau kerangka konsep.
6. Jalankan analisis sesuai desain.
7. Generate publication tables.
8. Generate research report.
9. Validasi hasil terhadap data mentah dan perangkat statistik independen sebelum publikasi.

### Batasan
v23 tetap merupakan aplikasi web/client-side. Output statistik bukan pengganti review epidemiologis atau validasi dengan perangkat statistik tervalidasi. Definisi operasional dan instrumen penyakit harus diverifikasi terhadap sumber resmi yang berlaku sebelum digunakan sebagai dokumen resmi.

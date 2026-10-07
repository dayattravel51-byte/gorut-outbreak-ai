# GORUT-OUTBREAK AI v31

## Perbaikan Keracunan Pangan

Versi ini menyelesaikan modul **Keracunan Makanan/Keracunan Pangan** yang sebelumnya belum berfungsi penuh.

### Yang diperbaiki
- Pilihan `Keracunan Makanan` pada tipe investigasi sekarang otomatis mengaktifkan penyakit `Keracunan Pangan / Keracunan Makanan (KLB)`.
- Modul khusus investigasi pangan muncul otomatis.
- Data kejadian tersimpan dalam `foodInvestigation`.
- Kuesioner spesifik keracunan pangan tersedia.
- Form tambah kasus berubah menjadi form kasus keracunan pangan dan menyimpan `foodCase`.
- Pilihan penyakit analisis dan laporan otomatis mengenali `keracunan-pangan`.
- Template PE/KLB khusus keracunan pangan tersedia.

### Basis rujukan
Kemenkes menjelaskan bahwa PE KLB keracunan pangan dilakukan terhadap korban dan aspek terkait higiene sanitasi pangan; tujuannya antara lain mengetahui agen penyebab, gambaran epidemiologi, kelompok yang terancam, sumber/cara terjadinya keracunan, dan menentukan penanggulangan yang efektif.

Rujukan yang digunakan untuk pemetaan operasional:
- Kemenkes RI, pedoman Penyelidikan dan Penanggulangan KLB Penyakit Menular dan Keracunan Pangan.
- Kemenkes RI, Buku Pedoman Keracunan Alami dan Non Alami (2024).
- Pedoman pengawasan higiene sanitasi pangan berbasis risiko.

Template aplikasi adalah **pemetaan operasional**, bukan klaim salinan verbatim seluruh formulir resmi. Validasi akhir terhadap pedoman/formulir program yang berlaku tetap diperlukan sebelum digunakan sebagai dokumen resmi.

### Validasi teknis
- `node --check app.js`: PASS
- `unzip -t`: PASS

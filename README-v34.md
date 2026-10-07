# GORUT-OUTBREAK AI v34

## Disease-by-Disease Workflow Audit

v34 menambahkan modul **Audit Workflow Penyakit** untuk memeriksa konsistensi alur digital:

**Instrumen → Investigasi → Kasus → Kontak → Spesimen → Analisis → GIS → PE/KLB → Laporan**

### Fitur
- Audit seluruh disease library secara otomatis.
- Status PASS/WARN.
- Pemeriksaan pertanyaan spesifik per penyakit.
- Pemeriksaan ketersediaan template PE/KLB.
- Pemeriksaan keberadaan modul kasus, kontak, spesimen, analisis dan GIS.
- Ringkasan jumlah penyakit, PASS/WARN, investigasi, dan kasus.
- Filter berdasarkan kelompok penyakit dan status audit.
- Ekspor hasil audit sebagai JSON.

### Catatan penting
Audit ini adalah pemeriksaan arsitektur/fungsional aplikasi. Status PASS tidak berarti instrumen digital sudah identik atau telah disahkan sebagai formulir resmi Kementerian Kesehatan. Setiap instrumen tetap perlu validasi terhadap pedoman/formulir terbaru sebelum digunakan sebagai dokumen resmi.

## Validasi teknis
- `node --check app.js`: PASS
- ZIP integrity test: PASS

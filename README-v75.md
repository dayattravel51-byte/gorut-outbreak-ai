# GORUT-OUTBREAK AI — v75
## Dashboard Epidemiologi Desa & Early Warning

v75 dibangun langsung dari v74 dan menambahkan dashboard epidemiologi tingkat desa.

### Fitur
- Dashboard desa berdasarkan Master Desa/Puskesmas v69.
- Perbandingan kasus 28 hari terakhir dengan 28 hari sebelumnya.
- Tren kasus mingguan 8 minggu.
- Distribusi penyakit/sindrom 28 hari.
- IR 28 hari per 100.000 penduduk jika denominator desa valid.
- Sinyal operasional: PRIORITAS TINGGI, WASPADA, MONITOR, NORMAL.
- Ekspor CSV early warning desa.
- Indikator kualitas: cakupan pemetaan kasus dan validitas denominator.

### Catatan metodologis
Sinyal v75 adalah screening operasional internal, bukan definisi KLB, bukan diagnosis, dan bukan model prediksi tervalidasi. Sinyal menggunakan perbandingan 28 hari dengan 28 hari sebelumnya serta baseline mingguan operasional. Hasil harus diverifikasi dengan definisi kasus, kelengkapan tanggal onset, kualitas data, investigasi lapangan, dan kriteria KLB yang berlaku.

IR pada dashboard adalah **IR selama 28 hari**, bukan annualized incidence rate.

### Data
- Kasus aktif dari database aplikasi.
- Pemetaan Desa → Puskesmas → Kecamatan dari Master Desa v69.
- Denominator desa dari tabel demografi v72.

### Validasi
- app.js diperiksa dengan `node --check`.
- Paket final diperiksa dengan `unzip -t`.

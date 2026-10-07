# GORUT OUTBREAK AI v97 — Early Warning & Response Engine

v97 menambahkan screening prioritas operasional berbasis empat komponen transparan:
1. tren kasus 7 hari dibanding rerata mingguan pada 28 hari sebelumnya (35 poin),
2. incidence rate bila denominator penduduk tersedia (25 poin),
3. beban alert SKDR 7 hari (20 poin),
4. kematian pada 7 hari (20 poin).

Skor 0–100 dikategorikan Rendah, Sedang, Tinggi, atau Sangat Tinggi. Skor bukan model prediksi tervalidasi, bukan diagnosis, dan tidak menetapkan KLB/wabah otomatis. Hasil wajib diverifikasi dengan kualitas data, musim, definisi kasus, keterlambatan pelaporan, denominator, dan konteks lapangan.

Supabase: `008_v97_early_warning.sql` menyediakan RPC agregat `early_warning_summary()` tanpa data identitas pasien.

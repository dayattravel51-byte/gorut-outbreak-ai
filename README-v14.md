# GORUT-OUTBREAK AI v14

## Fokus
Statistical Engine + AI Epidemiologist berbasis data investigasi lokal.

## Fitur
- Tabel 2×2 otomatis dari kasus dan kontak.
- RR, OR, 95% CI berbasis log-ratio bila sel memungkinkan.
- Chi-square 1 df dan p-value pendekatan.
- Ekspor hasil analisis JSON.
- Draft AI Epidemiologist berbasis aturan dan ringkasan data lokal.
- Pemeriksaan kelengkapan onset, koordinat, kontak, spesimen, dan kunjungan lapangan.
- Tetap offline-first.

## Batasan
- Belum merupakan paket statistik tervalidasi untuk publikasi atau keputusan program.
- Sel nol dapat menghasilkan CI NA/undefined; analisis exact atau koreksi kontinuitas belum diimplementasikan.
- Regresi logistik multivariat belum menjadi engine produksi.
- AI v14 adalah rule-based draft; belum memanggil model AI server-side.
- Kesimpulan KLB tetap memerlukan verifikasi epidemiolog dan pedoman penyakit yang berlaku.

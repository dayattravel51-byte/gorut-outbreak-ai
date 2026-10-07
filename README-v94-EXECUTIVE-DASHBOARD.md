# GORUT OUTBREAK AI v94 — Executive Epidemiology Dashboard

v94 memperkuat KABAR SERGAP menjadi dashboard executive berbasis agregat: KPI, tren kasus mingguan, indikator early warning, intensitas kasus per kecamatan, penyakit/alert prioritas, dan command indicators.

## Keamanan
Dashboard publik memanggil RPC `public_executive_dashboard()` yang hanya mengembalikan agregat. Tidak ada nama, alamat, nomor telepon, kontak, atau rincian klinis individu.

## Supabase
Jalankan SQL berurutan: 001, 002, 003, 004, 005, lalu 006.

## Catatan epidemiologi
Visual wilayah pada v94 adalah indikator intensitas agregat per kecamatan, bukan choropleth boundary map. Peta choropleth administratif harus menggunakan layer batas wilayah resmi dan denominator populasi yang tervalidasi pada tahap GIS berikutnya.

# GORUT-OUTBREAK AI v49 — Demography + Puskesmas Map + Incidence Rate

v49 dibangun di atas paket GORUT-OUTBREAK AI v48.

## Perubahan utama
- Master Demografi Kabupaten Gorontalo Utara per tahun dan per wilayah kerja Puskesmas.
- Denominator: penduduk, laki-laki, perempuan, KK, koordinat referensi, sumber, tanggal update, catatan.
- Master awal memuat 15 wilayah Puskesmas dari atribut DBF `PETA PUSKESMAS GORUT ASLI`.
- Tambah tahun, simpan, ekspor CSV, impor CSV.
- Perhitungan Insiden Rate / 100.000 berdasarkan kasus yang sudah dipetakan ke Puskesmas dan denominator tahun terpilih.
- Dashboard peta kasus + indikator IR.
- Draft PE/KLB otomatis menambahkan bagian peta sebaran kasus dan tabel IR.
- Laporan PE/KLB memiliki pilihan tahun denominator demografi.
- RBI BIG digunakan sebagai referensi administrasi/fallback.

## Strategi peta
1. **Utama:** geometri wilayah kerja Puskesmas milik Dinkes/Gorontalo Utara, bila shapefile lengkap tersedia.
2. **Fallback/reference:** RBI/Batas Wilayah BIG.
3. Titik kasus tetap diplot berdasarkan koordinat yang tersimpan.

File peta yang diterima pada tahap ini hanya `.dbf` dan `.cpg`; geometri `.shp/.shx` belum tersedia. Aplikasi tidak membuat batas Puskesmas sintetis.

Untuk choropleth polygon wilayah kerja Puskesmas secara penuh, berikan minimal `.shp`, `.shx`, `.dbf`, dan sebaiknya `.prj`.

## RBI BIG
Service referensi:
`https://geoservices.big.go.id/rbi/rest/services/BATASWILAYAH/BATAS_WILAYAH/MapServer`

BIG menyediakan layanan batas administrasi; layanan terkait yang diperiksa menunjukkan data batas administrasi nasional edisi Juni 2026.

## Rumus
`IR = jumlah kasus / penduduk pertengahan tahun × 100.000`

IR harus dibaca bersama kualitas numerator, denominator, definisi kasus, kelengkapan pelaporan, dan perubahan wilayah kerja.

# GORUT-OUTBREAK AI v40

## Alamat Kasus + Batas Administrasi + RBI

v40 menambahkan alamat lengkap pada setiap record kasus dan integrasi spasial dengan layanan Badan Informasi Geospasial (BIG) untuk identifikasi wilayah administrasi dari koordinat.

### Field kasus baru
- Alamat lengkap
- Provinsi
- Kabupaten/Kota
- Kecamatan
- Desa/Kelurahan
- Latitude
- Longitude
- metadata sumber identifikasi wilayah

### Integrasi RBI/BIG
Layanan live yang digunakan:
- `https://geoservices.big.go.id/rbi/rest/services/BATASWILAYAH/BATAS_WILAYAH/MapServer`
- Layer provinsi: 12
- Layer kabupaten/kota: 13
- Layer kecamatan: 10
- Layer desa/kelurahan: 11

Saat koordinat tersedia, aplikasi melakukan spatial query ke layanan BIG dan menyimpan hasil administrasi pada `case.admin`. Peta Leaflet dapat menampilkan layer batas administrasi melalui Esri Leaflet.

### Catatan data
Data batas wilayah adalah data geospasial resmi yang dilayani BIG. Karena batas administrasi dapat mengalami pemutakhiran, aplikasi menggunakan koneksi live dan menyimpan timestamp sumber pada setiap hasil lookup. Untuk penggunaan resmi, lakukan verifikasi versi/tanggal data dan status batas sesuai kebutuhan daerah.

### Ekspor
Export CSV kasus v40 mencakup alamat, hierarki administrasi, koordinat, dan sumber identifikasi wilayah.

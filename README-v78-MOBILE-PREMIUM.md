# GORUT-OUTBREAK AI v78 — Compact Demography + Mobile Field Form

## Perubahan utama

### 1. Tabel Isian Demografi dibuat ringkas
- Kolom yang tampil pada tabel utama:
  - No.
  - Kecamatan
  - Puskesmas
  - Desa
  - Penduduk
  - Laki-laki
  - Perempuan
  - KK
  - Luas km²
  - Latitude
  - Longitude
- Kolom **Catatan** dan **Status Denominator** tidak lagi ditampilkan pada tabel.
- Validasi denominator tetap dihitung oleh sistem dari Penduduk, Laki-laki, dan Perempuan.
- Tidak ada horizontal scroll pada tabel utama.
- Tidak ada inner scroll pada tabel; halaman browser yang melakukan scrolling vertikal.
- Input angka diperbesar dan menggunakan font/tinggi input yang lebih mudah dibaca.
- Data lama v72/v77 tetap dibaca dari `gorut-demography-v72-village` agar kompatibel.

### 2. Formulir Lapangan Mobile
Ditambahkan formulir mobile-first pada menu **📱 Formulir Lapangan**.

Fitur:
- Investigasi aktif
- Jenis kegiatan lapangan
- Tanggal & waktu
- Petugas
- Desa/Kelurahan dari Master Desa
- Puskesmas dan Kecamatan otomatis dari Desa
- GPS latitude/longitude
- Alamat/lokasi detail
- Subjek/inisial/ID
- Keterkaitan kasus dan kontak
- Temuan utama
- Tindakan/intervensi
- Foto menggunakan kamera perangkat bila didukung
- Draft offline di localStorage
- Penyimpanan offline-first ke `db.fieldVisits`
- Status online/offline
- Antrean sinkronisasi tetap mengikuti mekanisme aplikasi yang sudah ada

## Prinsip penggunaan
Formulir mobile adalah alat pencatatan operasional lapangan. Status KLB tidak ditetapkan otomatis oleh aplikasi.

## Validasi v78
- `node --check app.js`: PASS
- HTML basic parse: PASS
- `unzip -t`: PASS / no errors detected
- SHA-256 paket: dibuat saat packaging final

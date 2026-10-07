# GORUT OUTBREAK AI v95 — GIS Epidemiology Engine

## Tujuan
Modul v95 menambahkan pemetaan epidemiologi berbasis **Incidence Rate (IR)** dengan denominator penduduk dan boundary GeoJSON yang diunggah oleh operator.

## Prinsip
- Choropleth digunakan untuk rate, bukan sekadar jumlah kasus.
- IR dihitung: `kasus / penduduk × 10.000`.
- Wilayah tanpa denominator tidak dianggap nol.
- Boundary tidak dibuat atau ditebak oleh sistem.
- GeoJSON resmi dapat diunggah melalui halaman **GIS Kasus**.
- Pencocokan awal boundary menggunakan atribut nama kecamatan/wilayah.
- Jika boundary belum tersedia, sistem menggunakan titik kasus berkoordinat sebagai fallback.

## GeoJSON
Gunakan `FeatureCollection` dan pastikan salah satu atribut nama feature berisi nama wilayah, misalnya `KECAMATAN`, `kecamatan`, `Kecamatan`, `NAME`, atau `nama`.

## Denominator
Data populasi desa berasal dari master demografi aplikasi (`gorut-demography-v72-village`) dan dijumlahkan ke kecamatan. Operator harus memastikan denominator sudah tervalidasi sebelum memakai IR untuk keputusan operasional.

## Klasifikasi default
- 0 = 0
- >0–<1 = Rendah
- 1–<3 = Sedang
- 3–<10 = Tinggi
- ≥10 = Sangat tinggi

Klasifikasi adalah tampilan operasional bawaan, bukan ambang KLB nasional. Ambang dapat disesuaikan sesuai penyakit dan konteks epidemiologis.

## Privasi
Peta publik tidak boleh menggunakan titik kasus individual. Modul v95 untuk dashboard operasional menggunakan agregasi wilayah; data identitas pasien tetap berada di Command Center/RLS.

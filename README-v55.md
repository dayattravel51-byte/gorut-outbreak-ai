# GORUT-OUTBREAK AI — v55 Automated PE/KLB Intelligence

v55 menambahkan lapisan **Automated PE/KLB Intelligence** di atas modul v52–v54.

## Fitur
- Ringkasan investigasi aktif: kasus, konfirmasi, probable, kematian, CFR.
- Sinyal temporal berdasarkan onset dan puncak kasus.
- Pemeriksaan kelengkapan onset, koordinat, spesimen, kontak, dan kunjungan lapangan.
- Skor kualitas data operasional 0–100 sebagai indikator kesiapan analisis, bukan skor mutu resmi.
- Prioritas tindak lanjut berbasis aturan.
- Narasi otomatis untuk draft bagian hasil/analisis PE/KLB.
- Mengikutsertakan hasil v52, v53, dan v54 dalam ekspor JSON bila sudah tersedia.
- Integrasi otomatis ke `reportHtml()` dan `reportText()` tanpa mengganti mesin laporan lama.

## Catatan metodologis
v55 tidak menetapkan KLB secara otomatis dan tidak menggantikan penilaian epidemiologis. Denominator IR/Attack Rate, definisi kasus, desain analisis, bias, confounding, dan validitas data tetap harus diverifikasi petugas.

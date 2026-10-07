# GORUT-OUTBREAK AI v85 — CLINICAL / EPIDEMIOLOGY WORKFLOW QA

Tanggal: 7 Oktober 2026
Basis: v84 Full Functional QA

## Fokus
Menambahkan pemeriksaan read-only terhadap alur end-to-end investigasi aktif: Investigasi → Kasus → Kontak → Spesimen → Kegiatan Lapangan → kesiapan Analisis/GIS → Laporan.

## Prinsip keselamatan epidemiologis
Modul QA hanya menilai kelengkapan dan keterhubungan data. Modul tidak menetapkan diagnosis dan tidak menetapkan KLB secara otomatis. Klasifikasi dan keputusan resmi tetap memerlukan verifikasi epidemiologis, definisi kasus, hasil laboratorium, pembandingan baseline, dan kewenangan program/kesehatan.

## Pemeriksaan
- Investigasi aktif
- Kasus terhubung
- Kontak dan keterkaitan kontak-kasus
- Spesimen dan keterkaitan spesimen-kasus
- Kegiatan lapangan dan tautan kasus/kontak
- Kelengkapan onset, status, dan koordinat kasus
- Keracunan pangan: denominator terpapar, sakit/meninggal, Attack Rate, dan sumber pangan
- Ekspor hasil QA sebagai JSON

Pemeriksaan bersifat read-only dan tidak memodifikasi data pengguna.

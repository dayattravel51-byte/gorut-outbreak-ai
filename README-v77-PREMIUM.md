# GORUT-OUTBREAK AI v77 — PREMIUM UI FINAL POLISH

Basis: v76 FINAL.

## Perubahan utama
1. Logo Kabupaten Gorontalo Utara dan logo Surveilans Epidemiologi hanya tampil pada halaman login. Dashboard/app shell menggunakan brand mark minimalis.
2. Sidebar dibuat scrollable dan lebih kompak agar menu Analisis, Penelitian, GIS, Disease Intelligence, Laporan, Audit, Admin, dan modul lain tetap dapat diakses.
3. Dashboard disederhanakan menjadi command center; kartu promosi demografi yang besar disembunyikan dari dashboard karena Demografi memiliki halaman/menu khusus.
4. Dashboard mendapatkan **Pusat Analisis & Pengambilan Keputusan** dengan shortcut langsung ke Analisis Epidemiologi, Research Studio, GIS, Demografi & IR, Disease Intelligence, Dashboard Administratif, Laporan PE/KLB, dan Audit Workflow.
5. Tabel Isian Demografi diperlebar dengan min-width kolom, input numerik lebih besar, sticky header, horizontal scrolling, dan keterbacaan yang lebih baik pada layar desktop maupun HP.
6. Fitur v73–v76 tetap dipertahankan: integritas kuesioner, backup/export, Google Sheets opsional, public survey, IR desa, dashboard epidemiologi desa, dan early warning.

## Validasi
- app.js: node --check PASS
- ZIP integrity: unzip -t PASS
- Logo app shell: tidak lagi menggunakan file logo resmi; logo resmi tetap tersedia untuk halaman login yang dirender oleh app.js.

## Catatan
Sinyal early warning tetap merupakan screening operasional dan bukan penetapan KLB otomatis.

# GORUT-OUTBREAK AI v21 — Advanced Biostatistics Engine

v21 memperkuat modul Research Analysis Engine dari v20 dengan analisis epidemiologi/biostatistik lanjutan yang berjalan di sisi aplikasi.

## Fitur baru

- Regresi logistik multivariat untuk outcome biner.
- Adjusted OR, 95% CI, dan p Wald.
- Ringkasan missing/tidak valid dan complete-case analysis.
- Perbandingan OR crude vs adjusted sebagai bantuan penilaian confounding.
- Mantel–Haenszel stratified analysis dan common OR.
- Matched case-control 1:1 dengan McNemar dan matched OR.
- Cohort dengan person-time: incidence rate dan incidence rate ratio (IRR) + 95% CI.
- Integrasi hasil analisis lanjutan ke draft laporan penelitian.
- Ekspor JSON versi v21.
- Variabel dapat berasal dari field kasus maupun `answers.*` dari kuesioner.

## Desain yang didukung

Deskriptif/case series, cross-sectional, case-control tidak berpasangan, matched case-control, cohort, retrospective cohort outbreak investigation, ecological, time-series/surveillance trend, dan quasi-experimental.

## Catatan metodologis penting

1. Pemilihan model harus mengikuti desain, sampling, struktur outcome, waktu pengamatan, dan pertanyaan penelitian.
2. Regresi logistik menghasilkan OR; pada desain tertentu OR tidak sama dengan RR/PR.
3. Untuk cohort dengan person-time, IRR dapat digunakan bila person-time dan event didefinisikan secara benar.
4. Matched analysis memerlukan pair/stratum ID yang valid.
5. Confounding tidak boleh ditentukan hanya dari p-value; gunakan rencana a priori, DAG, dan pengetahuan epidemiologis.
6. Missing data saat ini menggunakan complete-case analysis pada modul lanjutan; multiple imputation belum diimplementasikan.
7. Conditional logistic regression, Cox proportional hazards, Poisson robust/log-binomial, ITS/DiD, dan beberapa metode kompleks masih menjadi tahap pengembangan/validasi berikutnya.
8. Implementasi frontend ini adalah alat bantu analisis dan perlu divalidasi dengan perangkat statistik rujukan sebelum digunakan untuk publikasi ilmiah, tesis/disertasi final, atau keputusan resmi.
9. Kuesioner penyakit tetap harus divalidasi terhadap instrumen/pedoman Kementerian Kesehatan yang berlaku sebelum penggunaan resmi.

# GORUT-OUTBREAK AI v73 — Case & Questionnaire Data Integrity

## Perubahan utama
1. Setiap kasus memiliki Case ID.
2. Seluruh jawaban kuesioner tetap disimpan di `case.answers`.
3. Disimpan metadata versi instrumen dan jumlah jawaban.
4. Daftar Kasus tetap ringkas; tombol **📋 Kuesioner** membuka semua jawaban.
5. Tersedia ekspor Dataset Lengkap CSV dengan kolom jawaban dinamis.
6. Tersedia backup JSON untuk seluruh kasus investigasi aktif.
7. Draft pengisian kuesioner disimpan otomatis di perangkat dan dapat dipulihkan.
8. Sinkronisasi Google Sheets tersedia sebagai webhook opsional.
9. Kuesioner publik v73 mencoba membuat Case ID otomatis setelah respons diterima, selain menyimpan respons mentah.
10. Integrasi desa → Puskesmas → Kecamatan dari v70 dan demografi per desa dari v72 dipertahankan.

## Validasi
- `app.js`: `node --check` PASS
- `public_survey.html` script: `node --check` PASS
- Google Apps Script: file teks untuk deployment di Apps Script.

## Penting
Koneksi Google Sheets tidak aktif otomatis. Admin harus men-deploy `google-apps-script/Code.gs` dan memasukkan URL Web App pada aplikasi.

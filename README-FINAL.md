# GORUT-OUTBREAK AI — v76 FINAL

## Status
Finalisasi paket aplikasi setelah v75. v76 mempertahankan seluruh modul sebelumnya dan menambahkan lapisan akhir dashboard epidemiologi desa.

## Fitur final
- Dashboard investigasi/KLB dan pengelolaan kasus.
- Kuesioner internal dan public survey.
- Penyimpanan seluruh jawaban kuesioner pada `case.answers` / `questionnaire_response` sesuai alur masing-masing.
- Case ID dan draft autosave.
- Backup JSON/CSV dan opsi Google Sheets.
- Master 123 desa, 15 Puskesmas, 11 Kecamatan.
- Demografi 1 desa = 1 baris.
- IR tingkat desa berbasis denominator penduduk.
- Dashboard epidemiologi desa 28 hari vs 28 hari sebelumnya.
- Peta risiko epidemiologi desa menggunakan koordinat yang tersedia.
- Panel kualitas data.
- Early warning operasional; tidak menetapkan KLB otomatis.

## Prinsip interpretasi
Sinyal prioritas pada dashboard adalah screening operasional internal. Angka ambang tidak boleh dianggap sebagai definisi KLB, diagnosis, atau model prediksi tervalidasi. Semua sinyal harus diverifikasi dengan definisi kasus, kelengkapan data, investigasi lapangan, dan ketentuan KLB yang berlaku.

## Aktivasi public survey backend
File `supabase/v74_public_survey_trigger.sql` disediakan sebagai opsi penguatan backend. Sebelum menjalankan, tinjau schema, RLS, dan hak akses Supabase yang digunakan oleh instalasi.

## Google Sheets
Integrasi Google Sheets tetap opsional. Deploy `google-apps-script/Code.gs` sebagai Web App hanya jika organisasi mengizinkan penyimpanan data tersebut. Jangan menaruh API key atau kredensial sensitif di frontend.

## Data demografi
Aplikasi tidak melakukan pembagian otomatis populasi kabupaten/kecamatan ke desa. Setiap denominator desa harus diisi atau diimpor dari sumber resmi yang dipilih operator.

## Checklist sebelum produksi
1. Konfigurasi backend/Supabase dan RLS.
2. Jalankan trigger public survey setelah schema diverifikasi.
3. Isi denominator penduduk setiap desa.
4. Isi koordinat desa bila ingin menggunakan peta desa.
5. Uji satu investigasi penyakit menular.
6. Uji satu investigasi keracunan makanan.
7. Uji public survey online dan offline.
8. Uji ekspor CSV/JSON.
9. Uji Google Sheets jika diaktifkan.
10. Lakukan UAT oleh epidemiolog/surveilans sebelum digunakan untuk keputusan resmi.

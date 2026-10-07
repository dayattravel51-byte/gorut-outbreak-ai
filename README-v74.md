# GORUT-OUTBREAK AI — v74

## Fokus v74
**Village-level incidence rate (IR) + Public Survey Data Integrity**.

### 1. IR per Desa
Menu **Tabel Isian Demografi** sekarang memiliki analitik:
- Desa → Puskesmas → Kecamatan dari Master Desa v69.
- Kasus aktif dihitung per desa.
- IR = kasus / penduduk × 100.000.
- IR hanya dihitung bila denominator valid: penduduk > 0 dan laki-laki + perempuan = penduduk.
- Filter Kecamatan, Puskesmas, pencarian desa.
- Ekspor CSV IR desa.
- Jumlah kasus yang belum dapat dipetakan ke master desa ditampilkan.
- Sistem **tidak menetapkan KLB otomatis**.

### 2. Public Survey → Case
Public Survey v12 memakai `survey_responses.id` sebagai kunci idempoten untuk Case ID.
- Pengiriman ulang tidak membuat Case ID baru untuk response yang sama.
- Antrian offline akan mengirim ulang response lalu mencoba membuat/upsert kasus.
- Seluruh payload kuesioner disimpan pada `questionnaire_response`.
- Metadata menyimpan `survey_id` dan `response_id`.

### 3. Hardening backend yang direkomendasikan
File `supabase/v74_public_survey_trigger.sql` menyediakan trigger backend:

`survey_responses INSERT → cases UPSERT`

Dengan ini pembuatan kasus tidak bergantung pada kemampuan browser publik untuk INSERT langsung ke tabel `cases`, dan retry menjadi idempoten berdasarkan `survey_responses.id`.

**Penting:** jalankan SQL hanya setelah meninjau schema/RLS Supabase yang digunakan oleh instalasi Anda. File ini mengasumsikan kolom `cases` dan `public_surveys` sesuai struktur aplikasi v74.

### 4. Urutan pengujian
1. Isi 1 desa dengan denominator valid.
2. Buat beberapa kasus pada desa tersebut.
3. Buka Tabel Isian Demografi → kartu **IR KASUS PER DESA**.
4. Pastikan jumlah kasus dan IR sesuai rumus.
5. Buat Public Survey dan kirim satu response.
6. Pastikan `survey_responses` terisi dan satu Case ID terbentuk.
7. Kirim ulang/refresh dan pastikan tidak terjadi duplikasi kasus.
8. Uji mode offline kemudian kembali online.

## Validasi paket
- `app.js` diperiksa dengan `node --check`.
- JavaScript `public_survey.html` diekstrak dan diperiksa dengan `node --check`.
- ZIP diperiksa dengan `unzip -t`.

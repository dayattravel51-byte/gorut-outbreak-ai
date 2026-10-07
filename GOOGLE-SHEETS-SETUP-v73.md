# GORUT-OUTBREAK AI v73 — Google Sheets Backup

## Prinsip
Google Sheets adalah **backup/warehouse opsional**, bukan database utama aplikasi. Aplikasi tetap menyimpan data kasus dan seluruh jawaban kuesioner di `case.answers`.

## Cara menyiapkan
1. Buat Google Spreadsheet khusus data surveilans.
2. Buka **Extensions → Apps Script**.
3. Hapus kode contoh lalu salin isi `google-apps-script/Code.gs`.
4. Save.
5. **Deploy → New deployment → Web app**.
6. Execute as: **Me**.
7. Who has access: **Anyone with the link** (sesuaikan kebijakan organisasi; untuk data kesehatan gunakan kebijakan akses yang disetujui instansi).
8. Salin URL `/exec`.
9. Di GORUT-OUTBREAK AI → **Daftar Kasus** → **Google Sheets — sinkronisasi opsional** → tempel URL → Simpan URL.
10. Klik **Kirim Kasus Aktif ke Sheet**.

## Sheet yang dibuat otomatis
- `CASE_MASTER`: satu baris per kasus, termasuk JSON jawaban lengkap.
- `QUESTIONNAIRE_RESPONSES`: satu baris per jawaban kuesioner.
- `SYNC_LOG`: catatan sinkronisasi.

## Catatan keamanan
- Data kesehatan adalah data sensitif. Gunakan Spreadsheet/Google Workspace yang dikelola instansi dan batasi akses sesuai kewenangan.
- Jangan mengaktifkan endpoint publik untuk data sensitif tanpa persetujuan kebijakan/keamanan organisasi.
- Versi v73 menggunakan webhook Google Apps Script opsional. Jika URL belum diisi, tidak ada pengiriman data ke Google.
- `no-cors` pada browser berarti aplikasi tidak dapat memverifikasi respons HTTP dari Google. Karena itu status `sheet-queued` berarti permintaan telah dikirim, bukan bukti absolut bahwa Google berhasil menyimpan data. Periksa `SYNC_LOG`.

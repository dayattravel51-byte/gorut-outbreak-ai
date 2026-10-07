# GORUT-OUTBREAK AI — v63

## Perubahan utama
- Struktur Daftar Kasus final: ID, Nama, Alamat, Desa/Kel., Kecamatan, Umur, JK, Tanggal Onset, Gejala Utama, Status, Faktor Risiko (Kuesioner), Outcome, Aksi.
- Tidak ada kolom Outcome ganda.
- Faktor Risiko tetap bersumber dari jawaban kuesioner dan dapat dibuka detailnya.
- v62 Automated IR dipertahankan.
- v63 Epidemiological Ranking & Alert: ranking Puskesmas dan Kecamatan berdasarkan sinyal IR, jumlah kasus, tren 28 hari, dan kelengkapan denominator.
- Status Prioritas Tinggi/Sedang/Monitor adalah sinyal operasional, bukan penetapan KLB.
- Kasus yang belum terpetakan tidak dipaksakan masuk ranking.
- Tersedia ekspor CSV ranking & alert.

## Validasi
- `node --check app.js`: PASS
- `unzip -t`: PASS

# GORUT-OUTBREAK AI v32

## Finalisasi fungsional

Perbaikan v32 berfokus pada audit alur kerja dan penyelesaian field yang sebelumnya hanya tampil tetapi belum konsisten dipersistenkan.

### Keracunan Pangan
- Investigasi bertipe `Keracunan Makanan` otomatis memilih disease `keracunan-pangan`.
- Panel investigasi menyimpan event, lokasi, waktu konsumsi, denominator terpapar, sakit, meninggal, pangan dicurigai, penjamah, air, penyimpanan, dan hipotesis.
- Kasus keracunan pangan menyimpan detail pangan, waktu konsumsi, onset, masa inkubasi, gejala, sumber pangan, rawat inap, dan spesimen klinis.
- Laporan PE/KLB menambahkan komponen khusus keracunan pangan dan attack rate bila denominator tersedia.

### Record management
Tombol hapus/konfirmasi tersedia untuk kasus, kontak, spesimen, alert, kunjungan lapangan, dan investigasi. Menghapus kasus juga membersihkan kontak dan spesimen yang merujuk pada kasus tersebut.

### Catatan metodologis
Template PE/KLB adalah template operasional yang dipetakan ke penyakit dan perlu diverifikasi terhadap pedoman/formulir Kemenkes yang berlaku sebelum diterbitkan sebagai dokumen resmi. Angka yang tidak tersedia tidak diimputasi secara otomatis.

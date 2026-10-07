# GORUT-OUTBREAK AI v80 — Demography & Field Lapangan Premium

## Perbaikan
- Tabel demografi benar-benar tanpa horizontal scrollbar/overflow container.
- Kolom Catatan dan Status Denominator tidak ditampilkan pada tabel input.
- Lebar kolom Laki-laki, Perempuan, KK, dan Luas km² dioptimalkan agar angka mudah dibaca.
- Latitude/Longitude tetap dipertahankan untuk GIS.
- Validasi Penduduk = Laki-laki + Perempuan tetap dihitung oleh sistem.
- Halaman Field Lapangan kini hanya menampilkan satu formulir utama; formulir legacy/duplikat disembunyikan.
- Formulir lapangan mempertahankan GPS, desa→Puskesmas→Kecamatan, foto, draft, offline-first, dan sinkronisasi antrean.

## Catatan
Data Catatan/Status Denominator lama tidak dihapus dari penyimpanan agar kompatibilitas data tetap terjaga; keduanya hanya tidak ditampilkan sebagai kolom input utama.

## v80 final UX adjustment
- Removed visible horizontal scrollbar/scroll container from the demographic entry table.
- Number-input spinner arrows are hidden while retaining numeric keyboard behavior.
- Legacy desktop Field Lapangan cards are hidden so the page presents one unified field form only.

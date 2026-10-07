# GORUT-OUTBREAK AI v19 — Risk Assessment & Early Warning

## Fokus
v19 menambahkan modul **Risk Assessment & Early Warning** di atas Command Center v18. Modul ini merupakan **screening operasional yang transparan**, bukan definisi KLB, bukan diagnosis, dan bukan model prediksi tervalidasi.

## Indikator screening
Skor dihitung dari data investigasi aktif yang tersedia:
- tendensi temporal (perbandingan jendela waktu terakhir dengan periode sebelumnya bila tanggal onset memadai);
- konsentrasi spasial menurut desa/village/kecamatan yang tercatat;
- sinyal laboratorium dari hasil positif yang tersedia;
- keparahan/outcome melalui kematian dan CFR;
- transmisi/kontak berdasarkan kontak sakit/konfirmasi dan kontak yang ditautkan ke kasus;
- sinyal alert SKDR terverifikasi pada data lokal.

Skor maksimum 11 dan level tampilan: Rendah, Perlu perhatian, atau Tinggi. Threshold ini adalah threshold screening internal aplikasi dan **bukan ambang resmi Kemenkes**.

## Kualitas data
Dashboard terpisah menampilkan kelengkapan onset, koordinat, status kasus, hasil laboratorium, kontak, dan kunjungan lapangan. Kesenjangan data tidak disamakan dengan rendahnya risiko.

## Lingkungan & iklim
v19 tidak mengasumsikan pengaruh curah hujan, suhu, sanitasi, kepadatan, atau paparan lingkungan tanpa data aktual. Variabel tersebut disiapkan sebagai perluasan berikutnya.

## Ekspor
Hasil screening dapat diekspor sebagai JSON dengan versi algoritme, indikator, skor, level, kelengkapan, dan timestamp.

## Prinsip penggunaan
Hasil screening harus ditinjau epidemiolog. Sistem tidak menetapkan KLB, diagnosis, sumber penularan, atau prediksi otomatis berdasarkan skor ini.

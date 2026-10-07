# GORUT-OUTBREAK AI — Field Mobile v79

## Tujuan
Aplikasi **GORUT Field Mobile** adalah PWA formulir lapangan yang dibuat khusus untuk smartphone petugas surveilans/epidemiologi Kabupaten Gorontalo Utara.

## Fitur
- Tampilan portrait-first untuk HP.
- Form kunjungan lapangan satu kolom dengan tombol besar.
- Master wilayah resmi 123 desa, 15 Puskesmas, 11 Kecamatan yang digunakan pada aplikasi.
- Kecamatan → Puskesmas → Desa otomatis berjenjang.
- GPS perangkat dengan tampilan akurasi.
- Kamera HP untuk foto lapangan.
- Penyimpanan offline/local-first menggunakan localStorage.
- Draft formulir.
- Data tersimpan, hapus, bagikan ringkasan.
- Ekspor JSON dan CSV; impor JSON.
- PWA/service worker untuk cache dan penggunaan saat koneksi buruk.
- Kompatibel dengan `gorut-v8` jika `mobile.html` dan aplikasi utama dijalankan pada origin yang sama: kunjungan mobile akan dijembatani ke `db.fieldVisits` aplikasi utama.
- Tidak menetapkan KLB/diagnosis secara otomatis.

## Cara menggunakan di HP
1. Upload `mobile.html`, `mobile-manifest.json`, `mobile-sw.js`, dan dua file icon ke hosting HTTPS.
2. Buka `https://DOMAIN/mobile.html` melalui Chrome/Edge/Safari di HP.
3. Izinkan akses lokasi saat diminta.
4. Pilih **Add to Home Screen / Tambahkan ke Layar Utama** agar tampil seperti aplikasi.
5. Atur nama petugas di menu Pengaturan.
6. Isi kunjungan lapangan. Data dapat disimpan walaupun offline.

### Catatan penting GPS/kamera
GPS dan PWA memerlukan konteks yang aman (HTTPS atau localhost). Jangan mengandalkan `file://` untuk penggunaan produksi.

## Integrasi dengan aplikasi utama
Jika `mobile.html` berada pada **origin/domain yang sama** dengan GORUT-OUTBREAK AI, aplikasi menggunakan key `gorut-v8` dan menambahkan kunjungan ke `fieldVisits` aplikasi utama melalui localStorage.

Jika mobile app berada pada domain/subdomain berbeda, gunakan Ekspor JSON/CSV untuk pemindahan data sampai sinkronisasi backend dikonfigurasi.

## Privasi
Formulir dapat memuat data sensitif. Gunakan kunci layar/PIN perangkat, batasi akses file ekspor, dan hapus data lokal setelah proses pemindahan/retensi sesuai kebijakan organisasi.

## Batasan
- Paket ini belum mengklaim sinkronisasi cloud otomatis.
- Status `pending` berarti data masih lokal/belum dikonfirmasi tersimpan pada backend.
- Foto disimpan sebagai data lokal dan dapat meningkatkan penggunaan penyimpanan perangkat.
- Instrumen lapangan harus divalidasi terhadap formulir/pedoman program yang berlaku sebelum digunakan sebagai instrumen resmi.

## Versi
**v79 Field Mobile — 7 Oktober 2026**

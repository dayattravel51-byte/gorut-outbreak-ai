# GORUT-OUTBREAK AI v36

## Disease-Specific Intelligence & Automated PE/KLB Support

Fitur baru: modul Disease Intelligence menghitung sinyal prioritas berdasarkan data kasus yang tersimpan, mencakup volume kasus, konfirmasi, kematian/CFR, kasus 7 hari terakhir, dan karakteristik penyakit prioritas.

### Prinsip keselamatan epidemiologis
- Skor adalah sinyal pendukung investigasi, bukan penetapan KLB.
- Sistem tidak menggantikan definisi kasus, baseline, verifikasi lapangan, pemeriksaan laboratorium, atau kewenangan program.
- CFR hanya dihitung dari data kasus yang tersedia di aplikasi dan tidak boleh dianggap sebagai estimasi populasi tanpa denominator yang sesuai.

### Prioritas
- TINGGI: skor 7–10
- PERHATIAN: skor 4–6
- RENDAH: skor 0–3

### Validasi teknis
- `node --check app.js`
- Uji integritas ZIP

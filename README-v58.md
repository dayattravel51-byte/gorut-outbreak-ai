# GORUT-OUTBREAK AI v58 — Case Risk Factor Presentation

## Fokus v58
Perapihan modul **Daftar Kasus**, khususnya kolom **Faktor Risiko (dari kuesioner)**.

### Perubahan
- Kolom Faktor Risiko tidak lagi menampilkan seluruh jawaban sebagai paragraf panjang.
- Faktor risiko ditampilkan dalam bentuk chip/row ringkas.
- Maksimal 3 faktor ditampilkan langsung pada line listing.
- Jika lebih dari 3 faktor, tersedia indikator **+n lainnya**.
- Tombol **Lihat detail** menampilkan seluruh faktor risiko yang teridentifikasi, dikelompokkan menurut kategori kuesioner.
- Sumber data tetap `case.answers`; tidak ada penghapusan atau pemindahan jawaban kuesioner.
- Pencarian Daftar Kasus juga dapat menemukan kasus berdasarkan faktor risiko.
- Export CSV sekarang menyertakan kolom **Faktor Risiko (dari kuesioner)**.
- Tabel Daftar Kasus diberi horizontal scroll agar tetap rapi pada layar desktop yang lebih kecil.
- Login wajib dan kebijakan tanpa pembayaran dari v57 tetap dipertahankan.
- Logo PAEI tetap menggunakan sumber sementara dari tautan pengguna sampai file logo dapat diunggah/dibundel secara lokal.

## Catatan metodologis
Identifikasi faktor risiko pada kolom ini merupakan **screening/presentasi jawaban kuesioner berbasis aturan**, bukan bukti hubungan kausal dan bukan hasil analisis statistik. Interpretasi epidemiologis tetap mengikuti desain studi, definisi variabel, kualitas data, dan analisis yang sesuai.

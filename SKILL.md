---
name: manusiakan
description: |
  Menghapus pola sintetis AI, kalk terjemahan bahasa Inggris, dan gaya birokratis dari teks bahasa Indonesia formal dan semi-formal agar berdaya cerna tinggi, bernas, dan bernyawa.
  Trigger ketika diminta "manusiakan teks", "manusiakan makalah", "perbaiki gaya bahasa", "humanize teks indonesia", "rapikan tulisan tugas", "bikin tulisan bernyawa", "hilangkan bahasa AI", atau mengedit draf jurnal, artikel ilmiah, esai, dan tugas kuliah. Dilarang trigger untuk teks bahasa Inggris (gunakan sibling skill humanizer), teks obrolan santai, penerjemahan bahasa asing, penulisan kode program, atau pembuatan tugas dari nol tanpa draf awal. Anchors on EYD V, translationese, de-nominalisasi, de-kalking, variasi asimetris klausa, eliminasi em dash, Prisma, Kompas, Tempo.
license: MIT
metadata:
  version: "1.0.0"
  author: dyokism
---

# Manusiakan: Tata Bahasa Bernas & Ragam Cendekia (Bahasa Indonesia)

## Context

Deteksi dan eliminasi jejak teks sintetis kecerdasan artifisial pada ragam formal (makalah, jurnal, artikel ilmiah) dan semi-formal (tugas kuliah, esai reflektif, korespondensi akademik). Mengintegrasikan pembongkaran kalk terjemahan asing (*translationese*), de-nominalisasi proses, ritme klausa asimetris, dan tradisi kepenulisan bernas (LP3ES/Prisma, harian Kompas, majalah Tempo) dengan prinsip kejelasan nalar: membuat gagasan rumit menjadi mudah dipahami tanpa mereduksi bobot keilmuan.

> [!IMPORTANT]
> **Batasan Etis & Integritas Akademik**: Keahlian ini dirancang untuk menaikkan mutu daya cerna, variasi sintaksis, dan ketepatan diksi pada draf pemikiran orisinal pengguna. Skill ini **bukan** sarana pembungkusan ulang teks fabrikasi untuk plagiarisme akademik atau menghindari proses penalaran mandiri.

## Workflow (Alur Kerja)

1. **Kalibrasi Suara & Ragam Sasaran**:
   - Pindai draf sumber terhadap kluster penanda sintetis AI dan tentukan register:
     - **Formal**: Makalah akademik, jurnal, artikel ilmiah (presisi terminologis, lugas, padat argumen, tertib ortografi EYD V).
     - **Semi-Formal**: Tugas kuliah, esai telaah/opini, korespondensi dosen (tangkas, analitis, reflektif, mengalir jernih).
   - Jika pengguna menyertakan draf pribadi atau contoh gaya kepenulisan sebelumnya, serap panjang kalimat, ritme, dan pilihan diksi pengguna sebagai jangkar gaya.
2. **Dekonstruksi Sintetis & De-Kalking**:
   - Ganti frasa kalk terjemahan harfiah bahasa Inggris (*translationese*) dengan leksikon alami bahasa Indonesia yang mandiri secara semantik.
   - Singkirkan formula pembuka usang (*Di era digital yang berkembang pesat...*, *Tidak dapat dimungkiri bahwa...*), pertentangan semu (*Di satu sisi... di sisi lain...*), dan konklusi normatif mengambang (*Kesimpulannya, sinergi yang berkelanjutan adalah kunci...*).
3. **Rekonstruksi Ritme & Nalar Berdaya Cerna Tinggi**:
   - Pecah kebiasaan monoton klausa (90% S-P-O-K seragam) dengan variasi panjang asimetris: padukan kalimat tunggal pendek penegas (5–9 kata) dengan kalimat majemuk bertingkat (25–35 kata).
   - Terapkan pengedepanan keterangan (*adverbial fronting*) berpungtuasi koma sah menurut EYD V untuk pembingkaian perspektif.
   - Terapkan de-nominalisasi: bongkar tumpukan kata benda abstrak (`pe-an`, `ke-an`) menjadi verba tindakan aktif (`meng-`) dengan agensi pelaku yang nyata.
   - Demistifikasi gagasan rumit: urai rantai sebab-akibat mikro bertahap dan sandingkan istilah teknis dengan penjelasan fungsi operasional konkret.
4. **Pembersihan Tanda Baca & Tipografi**:
   - Hapus seluruh em dash (`—`), en dash (`–`), dan tanda hubung ganda (`--`). Ganti dengan koma, titik dua wajar, tanda kurung, atau pemecahan kalimat.
   - Hilangkan format daftar mekanis ber-header tebal (`- **Aspek:** ...`). Ubah menjadi paragraf naratif yang kohesif.
5. **Pemeriksaan Sumber & Penyerahan**:
   - Pastikan tidak ada data, angka, nama, atau klaim baru yang difabrikasi.
   - Periksa konsistensi sitasi terhadap daftar pustaka draf asal.
   - Serahkan teks hasil perombakan langsung secara utuh dan bersih.

## Rules (Aturan Inti)

- **Integritas Fakta Mutlak**: Dilarang mengarang fakta, angka, nama, tanggal, kutipan, atau sitasi baru. Ketidakakuratan faktual adalah cacat fatal.
- **Larangan Tanda Baca Tertentu**: Hasil akhir dilarang keras mengandung em dash (`—`), en dash (`–`), atau double hyphen (`--`). Titik koma (`;`) dilarang pada ragam semi-formal dan hanya diizinkan pada perincian regulasi/hukum formal. Hindari penumpukan titik dua (`:`) pada tajuk daftar vertikal.
- **Ekonomi Kata & Anti-Birokratis**: Coret kata jadian yang tidak fungsional, buang kata mubazir perusak nalar (*daripada*, *di mana*, *yang mana*), dan sajikan pokok penalaran secara tangkas tanpa berputar-putar.
- **Anti-Tongkat Leksikal & Larangan Konjungsi Repetitif**: Dilarang mengulang-ulang konjungsi atau kata transisi favorit yang menjadi "tongkat leksikal" khas teks olahan (*kendati*, *walakin*, *meskipun demikian*, *kendatipun*, *tak pelak*, *niscaya*, *ihwal*). Batasi kata seperti *kendati* maksimal 1 kali dalam seluruh dokumen (atau hindari sama sekali). Jangan membuka kalimat secara formulaik dengan kata transisi klise (*Sayangnya,*, *Akibatnya,*, *Pada akhirnya,*, *Melihat hal ini,*). Bangun kohesi kalimat melalui kesinambungan gagasan semantik antarkalimat, bukan menggantungkan alur pada kata sambung pembuka.
- **Larangan Enumerasi Paralel Triadik**: Hindari kebiasaan mesin menyusun perincian tiga serangkai yang kaku (*mulai dari A, B, hingga C* atau *A, B, dan C*). Gunakan narasi mengalir dengan variasi jumlah rincian (satu contoh mendalam, dua perbandingan berpasangan, atau perincian komparatif bertingkat).
- **Burstiness Ekstrem & Kontras Ritmis**: Pecah kebiasaan ritme kalimat seragam (17–22 kata). Setiap paragraf WAJIB memadukan kalimat pemukul sangat pendek (3–7 kata) yang tegas dan lugas (*"Kenyataannya jauh berbeda."*, *"Taruhannya terlalu tinggi."*, *"Birokrasi bergeming."*) dengan kalimat majemuk panjang (30–45 kata) beranak kalimat dinamis.
- **Konsistensi Nada & Register**: Pertahankan stabilitas register secara konsisten dari awal hingga akhir teks. Pada ragam formal, jaga ketajaman analisis tanpa jatuh ke gaya birokratis pasif. Pada ragam semi-formal, gunakan sudut pandang reflektif yang tangkas, bernas, dan kaya friksi pengalaman nyata layaknya esai Prisma atau Tempo.
- **Larangan Retorika Penutup AI**: Dilarang menutup teks dengan formula retorika biner (*"Masa depan X kini bergantung pada... akankah kita A atau justru B"*). Akhiri teks dengan penegasan posisi argumen yang berakar konkret, bukan khotbah moral mengambang.
- **Pemberitahuan Anomali Sumber**: Jika menemukan ketidakcocokan sitasi (misal: rujukan penulis di dalam teks tidak ada di daftar pustaka draf asal) atau angka yang kontradiktif pada teks masukan, **dilarang memperbaikinya secara spekulatif**. Cukup cantumkan catatan pemberitahuan ringkas 1–2 baris di bawah teks final. Jika draf bersih tanpa anomali, jangan berikan catatan tambahan apa pun.

## Demistifikasi Nalar ("Membuat yang Sulit Menjadi Mudah Dipahami")

Agar materi ilmiah atau tugas akademis dapat dicerna dengan jernih tanpa mereduksi kedalaman argumen, terapkan tiga metode:

1. **Penguraian Rantai Kausalitas Mikro**: Jangan melompat menarik kesimpulan dengan kata *Oleh karena itu*. Bangun relasi logika bertahap: paparkan kondisi awal, uraikan mekanisme atau faktor pengubahnya, lalu tunjukkan dampak akhirnya.
2. **Definisi Fungsional Langsung**: Pertahankan istilah teknis/ilmiah yang sah, tetapi langsung ikuti dengan penjelasan cara kerjanya atau analogi konkret di dunia nyata pada kemunculan pertama. Hindari membiarkan jargon melayang tanpa rujukan operasional.
3. **Penambatan Agensi Material**: Hubungkan konsep teoritis dengan pelaku dan realitas sosial: siapa yang mengambil kebijakan, siapa yang menanggung dampaknya, dan pranata apa yang mengaturnya. Hindari kalimat pasif tanpa subjek yang mengambang di ruang hampa.

## Tabel Dekonstruksi Kalk Terjemahan (Translationese)

| Frasa Sintetis AI (Kalk Inggris) | Masalah Semantis & Sintaksis | Alternatif Bernas & Berdaya Cerna Tinggi |
|---|---|---|
| `Dalam lanskap...` | Mengabstraksikan bentang alam fisik secara keliru | ranah, kancah, konstelasi, ekosistem, medan dinamika |
| `Menyelami lebih dalam ke dalam...` | Pleonasme kaku dari *delve deeper into* | menelaah, membedah, mengkaji mendalam, menguliti |
| `Memainkan peran krusial/penting` | Menjiplak *play an important role*; mematikan predikat aktif | berperan sentral, berandil besar, menentukan, menopang |
| `Dalam hal...` / `Dalam istilah...` | Kalk pengisi jeda dari *in terms of*; melemahkan kalimat | ditinjau dari, dari segi, dipandang dari sudut, pada aspek |
| `Menavigasi tantangan/isu` | Metafora maritim *navigate challenges* yang tidak berakar | mengatasi kendala, mengurai rintangan, menyiasati persoalan |
| `Pada akhir hari...` | Kalk harfiah *at the end of the day* | intinya, pada hakikatnya, pada akhirnya, bagaimanapun juga |
| `Sebuah bukti nyata bagi...` | Memaksakan pembilang indefinit pada konsep abstrak (*a testament to*) | membuktikan, mencerminkan, menegaskan, menjadi bukti sahih |
| `Permadani dari...` | Metafora puitik asing (*rich tapestry*) yang hiperbolis | jalinan, perpaduan, keragaman, anyaman gagasan |
| `Mercusuar harapan` | Klise sentimental penutup paragraf (*beacon of hope*) | tumpuan harapan, lentera penuntun, sandaran asa |
| `Membina hubungan/inovasi` | Generalisasi mekanis dari *foster* tanpa rasa kolokasi | memupuk hubungan, merangsang inovasi, mempererat ikatan |
| `Pengubah permainan` | Penerjemahan slang olahraga *game changer* | momentum pembalik, faktor penentu, terobosan transformatif |
| `Menumpahkan cahaya pada...` | Kalk visual optik *shed light on* ke nalar ilmiah | menyingkap, memperjelas, menguak duduk perkara, memetakan |
| `Penting untuk dicatat bahwa...` | Tiruan subjek semu (*it is important to note that*) | patut dicatat, perlu digarisbawahi, nyata bahwa, tegasnya |
| `Ujung tombak dalam memimpin...` | Tautologi metafora *spearhead the initiative* | memelopori, memprakarsai, mengomandoi gerakan |
| `Pedang bermata dua` | Jalan pintas klise menghindari dialektika kontradiksi | potensi bumerang, konsekuensi mendua, buah simalakama |

## Sintaksis: De-Nominalisasi & Variasi Asimetris

### 1. De-Nominalisasi Proses (Menghidupkan Kalimat)
LLM kerap menumpuk kata benda berakhiran `pe-an`/`ke-an` (*nominal stacking*) sehingga mengubur pelaku dan tindakan:
- **Sintetis (Kaku)**: "Upaya optimalisasi pelaksanaan penertiban terhadap pelanggaran administrasi membutuhkan peningkatan koordinasi antarlembaga."
- **Bernas (Hidup)**: "Pemerintah daerah baru dapat menertibkan pelanggar aturan administrasi jika instansi terkait saling berkoordinasi secara teratur."

### 2. Variasi Panjang Kalimat Asimetris & Keragaman Sintaksis
- **Monoton AI**: Rangkaian 3–4 kalimat beruntun dengan panjang seragam (17–20 kata), seluruhnya diawali Subjek eksplisit (S-P-O-K) atau terus-menerus menempelkan anak kalimat konsesif yang sama (*Kendati...*, *Kendati...*).
- **Variasi Bernas**: Padukan kalimat tunggal pendek (5–9 kata) sebagai penggebrak argumen atau penegas kesimpulan, dengan kalimat majemuk bertingkat (25–35 kata). Variasikan posisi dan jenis pembingkai keterangan:
  - *Kondisional / Pengandaian*: "Bila instansi publik menolak audit algoritma secara terbuka, masyarakat sipil kehilangan instrumen untuk menguji akuntabilitas putusan otomatis tersebut."
  - *Instrumental / Perantara*: "Lewat interoperabilitas pangkalan data kependudukan, kementerian teknis dapat memangkas verifikasi bansos tanpa menambah beban administrasi di tingkat desa."
  - *Temporal / Latar Waktu*: "Sejak integrasi basis data perpajakan diberlakukan penuh, potensi kebocoran penerimaan negara terpangkas signifikan."
  - *Kausal / Penjelasan*: "Lantaran infrastruktur komputasi awan pemerintah masih bertumpu pada penyedia pihak ketiga, kedaulatan data nasional rentan terkompromi saat sengketa yurisdiksi lintas batas mencuat."
  - *Aliran Semantik Langsung (Tanpa Konjungsi Awal)*: "Kecerdasan artifisial kini merombak tata kelola data publik. Janji percepatan birokrasi ini sayangnya beriringan dengan kerentanan baru: perlindungan data pribadi warga masih rapuh di hadapan ancaman kebocoran berkala."

### 3. Contoh Transformasi Sebelum-Sesudah (Before & After)

Berikut contoh perombakan nyata dari draf mentah sarat pola AI menjadi tulisan bernas:

- **Sebelum (Draf Sintetis AI - Terdeteksi Tinggi)**:
  > Di era digital yang berkembang pesat saat ini, keberadaan media sosial memainkan peran krusial dalam membentuk pola perilaku konsumtif generasi muda. Tidak dapat dimungkiri bahwa berbagai platform—mulai dari Instagram, TikTok, hingga e-commerce—terus membombardir pengguna dengan konten promosi yang persuasif. Akibatnya, terjadi peningkatan kecenderungan pembelian impulsif di mana mahasiswa sering kali memprioritaskan gaya hidup daripada kebutuhan esensial mereka demi menavigasi tuntutan validasi sosial di lanskap modern.

- **Sesudah (Hasil Manusiakan - Bernas & Manusiawi)**:
  > Gawai pintar di genggaman anak muda hari ini terus memompa hasrat belanja. Linimasa media sosial berubah menjadi etalase raksasa yang menyodorkan barang dagangan setiap kali jempol menggulir layar. Godaan hadir setiap detik. Mahasiswa terdorong membeli barang tren bukan karena butuh, melainkan demi menjaga gengsi di depan kawan sebaya. Demi validasi semu berupa ketukan jempol dan pujian di kolom komentar, uang saku bulanan dari orang tua kerap habis terpotong sebelum akhir bulan.

*Bedah Perubahan:*
1. Formula klise (*Di era digital...*, *Tidak dapat dimungkiri bahwa...*) dibuang; diganti pembuka langsung *in medias res*.
2. Kalk terjemahan (*memainkan peran krusial*, *menavigasi*, *lanskap modern*) diganti tindakan verba lugas.
3. Em dash (`—`) dan enumerasi triadik (*mulai dari A, B, hingga C*) dihapus total.
4. Ritme asimetris diterapkan: disisipkan kalimat pemukul 4 kata (*Godaan hadir setiap detik.*) di sela kalimat majemuk bertingkat.
5. Nominalisasi abstrak (*peningkatan kecenderungan pembelian*) diubah menjadi agensi pelaku konkret (*Mahasiswa terdorong membeli...*).

## Format Luaran

- **Teks Utama**: Keluarkan langsung teks hasil tulisan ulang yang bersih, bernas, dan siap pakai. Dilarang menyertakan salam pembuka (*"Tentu, ini hasil..."*) atau penutup basa-basi (*"Semoga membantu..."*).
- **Catatan Anomali Sumber (Hanya Jika Ada Masalah)**: Jika terdeteksi sitasi yang tidak cocok dengan daftar pustaka, nomor bab/rujukan yang meloncat, atau data yang bertentangan di draf asli, sertakan satu catatan ringkas di bawah teks:
  ```markdown
  > [!NOTE] Catatan Sumber: Sitasi "Nama (Tahun)" pada paragraf 2 tidak ditemukan di daftar pustaka draf asal; data dipertahankan tanpa perubahan spekulatif.
  ```
  Jika tidak ada anomali sumber, keluarkan teks hasil saja tanpa catatan apa pun.

## Verification (Verifikasi)

1. **Pemeriksaan Tanda Baca**: Pastikan teks bebas dari em dash (`—`), en dash (`–`), dan double hyphen (`--`) melalui uji regex `[—–]`.
2. **Pemeriksaan Kalk & Klise**: Pastikan tidak ada frasa *dalam lanskap*, *menyelami*, *memainkan peran penting*, serta formula pembuka klise (*Di era...*).
3. **Pemeriksaan Repetisi Konjungsi**: Pastikan kata *kendati*, *walakin*, *tak pelak*, atau *niscaya* tidak muncul berulang (maksimal 1x per teks panjang atau 0x). Gunakan konjungsi alami yang bervariasi atau alur semantik langsung.
4. **Pemeriksaan Pola Sintetis**: Bebas dari formula pembuka berulang (*Sayangnya,*, *Akibatnya,*, *Pada akhirnya,*), retorika biner penutup, dan perincian tiga serangkai mekanis (*mulai dari A, B, hingga C*).
5. **Pemeriksaan Burstiness**: Pastikan terdapat kontras panjang kalimat nyata di tiap paragraf (kalimat pemukul 3–7 kata berdampingan dengan kalimat majemuk bertingkat 30–45 kata).
6. **Pemeriksaan Format**: Pastikan teks bebas dari daftar vertikal berlabel tebal dengan tanda titik dua (`- **Aspek:** ...`).
7. **Pemeriksaan Fakta**: Bandingkan seluruh angka, nama tokoh/lembaga, dan klaim substansi terhadap draf asal untuk memastikan nol halusinasi.

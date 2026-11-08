# Manusiakan

[![Lisensi MIT](https://img.shields.io/badge/license-MIT-blue.svg)](LICENSE)
[![Versi](https://img.shields.io/badge/version-1.0.0-green.svg)](CHANGELOG.md)

**Manusiakan** merombak draf tulisan yang kaku dan sarat jejak sintetis AI menjadi tulisan cendekia yang bernas, jernih, dan bernyawa. Gagasan pokok tetap utuh tanpa rekayasa fakta.

Skill ini bekerja pada ragam formal (makalah, jurnal, artikel ilmiah) maupun semi-formal (esai telaah, tugas kuliah, korespondensi akademik). Pondasinya bertumpu pada tertib ortografi EYD V, pembongkaran kalk terjemahan asing (*translationese*), serta tradisi kepenulisan lugas khas LP3ES/Prisma, Kompas, dan Tempo.

## Contoh Transformasi (Sebelum & Sesudah)

**Sebelum (Draf Sintetis AI):**
> Di era digital yang berkembang pesat saat ini, keberadaan media sosial memainkan peran krusial dalam membentuk pola perilaku konsumtif generasi muda. Tidak dapat dimungkiri bahwa berbagai platform—mulai dari Instagram, TikTok, hingga e-commerce—terus membombardir pengguna dengan konten promosi yang persuasif. Akibatnya, terjadi peningkatan kecenderungan pembelian impulsif di mana mahasiswa sering kali memprioritaskan gaya hidup daripada kebutuhan esensial mereka demi menavigasi tuntutan validasi sosial di lanskap modern.

**Sesudah (Hasil Manusiakan):**
> Gawai pintar di genggaman anak muda hari ini terus memompa hasrat belanja. Linimasa media sosial berubah menjadi etalase raksasa yang menyodorkan barang dagangan setiap kali jempol menggulir layar. Godaan hadir setiap detik. Mahasiswa terdorong membeli barang tren bukan karena butuh, melainkan demi menjaga gengsi di depan kawan sebaya. Demi validasi semu berupa ketukan jempol dan pujian di kolom komentar, uang saku bulanan dari orang tua kerap habis terpotong sebelum akhir bulan.

## Hasil Uji Empiris & Benchmark

Uji banding terkontrol pada naskah bertema *Dampak Media Sosial terhadap Gaya Hidup dan Pola Konsumtif Generasi Z* melalui detektor ZeroGPT membuktikan ketajaman pendekatan ini:

| Kondisi | Berkas Sampel | Panjang Teks | Skor ZeroGPT | Status Deteksi |
| :--- | :--- | :--- | :--- | :--- |
| **Draf Mentah (Raw AI ChatGPT)** | [`raw_ai_mentah.md`](benchmark/samples/raw_ai_mentah.md) | 11.783 karakter | **94% AI** | 58 kalimat terblok (*AI GPT*) |
| **Hasil Polesan (`manusiakan`)** | [`humanized_hasil.md`](benchmark/samples/humanized_hasil.md) | 6.751 karakter | **0% AI** | 0 kalimat terdeteksi (*Human Written*) |

> **Skor deteksi turun dari 94% ke 0%**. Bukti tangkapan layar serta draf uji ragam formal dan semi-formal tersimpan rapi di direktori [benchmark/](benchmark/README.md).

## Lima Prinsip Inti

1. **Bongkar Pembuka Klise**: Tanggalkan basa-basi usang (*Di era modern...*, *Tidak dapat dimungkiri bahwa...*). Masuk langsung ke pokok persoalan sejak kalimat pertama (*in medias res*).
2. **Kikis Kalk Terjemahan Harfiah**: Singkirkan struktur gramatika bahasa Inggris mentah (*memainkan peran kunci*, *dalam lanskap*, *menavigasi*, *menyelami*). Gunakan padanan leksikal bahasa Indonesia yang wajar dan berakar.
3. **Urai Nominalisasi, Hadirkan Pelaku**: Pecah tumpukan kata benda abstrak `pe-an`/`ke-an` menjadi kata kerja aktif `meng-`. Tunjukkan siapa yang memikul tindakan agar kalimat tidak melayang di ruang hampa.
4. **Pecah Monotoni Ritme**: Jangan biarkan panjang kalimat seragam (17–22 kata). Setiap alinea memadukan kalimat pemukul pendek (3–7 kata) dengan kalimat majemuk bertingkat (30–45 kata) yang beranak-kalimat dinamis.
5. **Tertibkan Tipografi**: Buang seluruh tanda pisah em dash (`—`), en dash (`–`), tanda hubung ganda (`--`), serta daftar poin mekanis berlabel tebal.

## Tabel Dekonstruksi Kalk Terjemahan

| Frasa Sintetis AI (Kalk Inggris) | Masalah Semantis & Sintaksis | Alternatif Bernas & Berdaya Cerna Tinggi |
|---|---|---|
| `Dalam lanskap...` | Mengabstraksikan bentang alam fisik secara keliru | ranah, kancah, konstelasi, ekosistem, medan dinamika |
| `Menyelami lebih dalam ke dalam...` | Pleonasme kaku dari *delve deeper into* | menelaah, membedah, mengkaji mendalam, menguliti |
| `Memainkan peran krusial/penting` | Menjiplak *play an important role*; mematikan predikat aktif | berperan sentral, berandil besar, menentukan, menopang |
| `Dalam hal...` / `Dalam istilah...` | Kalk pengisi jeda dari *in terms of*; melemahkan kalimat | ditinjau dari, dari segi, dipandang dari sudut, pada aspek |
| `Menavigasi tantangan/isu` | Metafora maritim *navigate challenges* yang tidak berakar | mengatasi kendala, mengurai rintangan, menyiasati persoalan |
| `Pada akhir hari...` | Kalk harfiah *at the end of the day* yang tidak lazim | pada akhirnya, bagaimanapun juga, intinya |
| `Memberikan wawasan tentang...` | Jiplakan kaku dari *provide insights into* | menerangkan, menyingkap, memperjelas, memetakan |
| `Merupakan bukti dari...` | Terjemahan mentah *is a testament to* | membuktikan, menegaskan, mencerminkan, menandai |
| `Penting untuk dicatat bahwa...` | Pengisi jeda buatan dari *it is important to note* | buang frasa ini; langsung nyatakan gagasan pokok |
| `Berada di garis depan...` | Kalk militer *at the forefront of* yang dipaksakan | memelopori, memimpin, menginisiasi, berada di garda depan |
| `Memiliki dampak pada...` | Struktur pasif nominal dari *have an impact on* | berdampak pada, mempengaruhi, mengguncang, menekan |
| `Menyoroti kebutuhan akan...` | Kalk mekanis dari *highlight the need for* | mendesak perlunya, menuntut adanya, menunjukkan urgensi |

## Cara Pemasangan

Setelah terpasang, panggil skill melalui perintah `/manusiakan`, *"manusiakan naskah ini"*, atau *"perbaiki gaya bahasa draf berikut"*.

### Claude Code

Pasang lewat marketplace plugin Claude Code:
```bash
/plugin marketplace add dyokism/manusiakan
/plugin install manusiakan@manusiakan
```

Atau pasang melalui pengelola paket skills:
```bash
npx skills add dyokism/manusiakan --global --agent claude-code
```

### Google Antigravity

Klon repositori ke folder skills Antigravity lokal:
```bash
git clone https://github.com/dyokism/manusiakan.git ~/.gemini/config/skills/manusiakan
```

### Claude Desktop & Claude.ai (Web)

1. Buka halaman [Releases](https://github.com/dyokism/manusiakan/releases).
2. Unduh paket `manusiakan.skill`.
3. Unggah ke Claude lewat menu **Settings → Capabilities / Skills**.

### Agen Lainnya (Codex, OpenCode, dsb.)

```bash
npx skills add dyokism/manusiakan --global --agent '*'
```

## Batasan Etis & Integritas Akademik

Manusiakan menajamkan daya cerna, variasi sintaksis, dan ketepatan diksi pemikiran orisinal penulis.

> [!IMPORTANT]
> Keahlian ini **bukan** sarana penyamaran teks fabrikasi demi plagiarisme atau jalan pintas menghindari penalaran mandiri. Sitasi rujukan, data numerik, nama tokoh, dan pokok argumen dari draf asal wajib dipertahankan seutuhnya tanpa fabrikasi spekulatif.

## Lisensi

Didistribusikan di bawah lisensi terbuka [MIT License](LICENSE). Hak Cipta (c) 2026 dyokism.

---
name: manusiakan
description: |
  Membersihkan dan menghapus tanda-tanda teks sintetis AI dari tulisan bahasa Indonesia secara presisi tanpa merombak gaya orisinal penulis. Trigger ketika diminta "manusiakan teks", "manusiakan draf", "hilangkan bahasa AI", "bersihkan pola AI", "remove AI writing", "rapikan gaya AI", atau mengoreksi teks yang terindikasi buatan ChatGPT/Claude/Gemini. Dilarang trigger untuk teks bahasa Inggris (gunakan sibling skill humanizer), penulisan esai dari nol, perombakan gaya sastra/kreatif non-AI, atau penulisan kode program. Anchors on tanda AI, kalk terjemahan, em dash, inflation words, negative parallelism, Wikipedia AI Cleanup, WP:AISIGNS.
license: MIT
metadata:
  version: "2.0.1"
  author: dyokism
---

# Manusiakan: Eliminasi Pola Teks AI (Bahasa Indonesia)

## Context

Pembersihan tanda-tanda teks sintetis kecerdasan buatan (LLM) pada tulisan bahasa Indonesia berbasis pedoman komunitas Wikipedia (WP:AISIGNS) dan inspirasi blader/humanizer. Berprinsip bedah terukur (surgical): mengidentifikasi dan mengeliminasi klise, inflasi kosakata, dan cacat struktural khas AI tanpa memaksakan perubahan gaya orisinal, ritme artifisial, atau kosakata berat yang membebani daya cerna pembaca.

## Workflow

1. **Pindai & Identifikasi (Pass 1 - Audit)**:
   - Pindai draf terhadap 4 kategori penanda AI:
     - **Kata & Frasa Inflasi**: Frasa klise dan kalk terjemahan harfiah (*dalam lanskap*, *menyelami*, *memainkan peran krusial*).
     - **Retorika Struktural**: Pembuka formulaik (*Di era digital saat ini...*, *Tidak dapat dimungkiri bahwa...*), pertentangan semu (*Bukan hanya X, melainkan Y*), enumerasi triadik mekanis (*A, B, dan C* yang dipaksakan), serta penutup khotbah/retorika biner.
     - **Tipografi & Format**: Em dash (`—`) berulang, format daftar tebal mekanis (`**Kategori:** ...`), dan bullet point artifisial pengganti paragraf naratif.
     - **Artefak Chatbot**: Pembuka obrolan (*Tentu, berikut draf...*), penutup sopan (*Semoga bermanfaat!*), atau disclaimer model bahasa.
2. **Bedah Terukur & De-AI (Pass 2 - Refactor)**:
   - Terapkan intervensi moderat: ganti frasa bermasalah langsung pada tempatnya. Tulis ulang satu kalimat utuh hanya jika pola AI menyatu erat dengan struktur sintaksis kalimat tersebut.
   - Pertahankan register, suara, alur penalaran, dan ragam kosakata asli pengguna tanpa memaksakan burstiness, ritme asimetris, atau jargon berat.
   - Ganti em dash (`—`) dan en dash (`–`) dengan koma, tanda kurung, titik dua wajar, atau pemecahan kalimat sederhana.
   - Jika draf sudah alami dengan minim tanda AI, pertahankan teks aslinya dan hindari perombakan berlebih.
3. **Verifikasi & Format Luaran (Pass 3 - Finalisasi)**:
   - Jaga integritas fakta secara mutlak: dilarang menambah, mengubah, atau menghapus angka, data, nama, atau sitasi faktual.
   - Sajikan teks hasil revisi secara utuh, bersih, dan langsung siap pakai tanpa catatan pembersihan, kecuali pengguna eksplisit memintanya.

## Tabel Panduan Frasa & Kalk Terjemahan AI

| Frasa Sintetis AI | Masalah Semantis / Retoris | Pengganti Alami / Solusi |
|---|---|---|
| `Dalam lanskap...` | Abstraksi bentang alam klise (*in the landscape of*) | di bidang, dalam ranah, pada situasi, di lingkungan |
| `Menyelami lebih dalam...` | Kalk kaku dari *delve deeper* | menelaah, mengkaji, membahas, mendalami |
| `Memainkan peran krusial/penting` | Kalk pasif dari *play a crucial role* | berperan penting, berpengaruh besar, menentukan |
| `Sebuah bukti nyata bagi...` | Kalk indefinit dari *a testament to* | bukti nyata, mencerminkan, menunjukkan |
| `Menavigasi tantangan/isu` | Metafora maritim asing (*navigate challenges*) | menghadapi kendala, mengatasi persoalan, menyiasati |
| `Permadani dari...` / `Mercusuar...` | Metafora puitik AI (*rich tapestry*, *beacon*) | keragaman, jalinan gagasan, tumpuan, pedoman |
| `Penting untuk dicatat bahwa...` | Tiruan subjek semu (*it is important to note that*) | perlu dicatat bahwa, patut diingat, (atau hapus frasa) |
| `Tidak dapat dimungkiri bahwa...` | Pengisi jeda pembuka kalimat klise | sesungguhnya, nyatanya, (atau langsung ke inti argumen) |
| `Bukan hanya X, tetapi juga Y` | Formula dikotomi kaku (*Not only X, but Y*) | sebut langsung kedua poin secara sejajar atau fokus ke klaim utama tanpa kontras semu |
| `Di era [teknologi/digital] yang...` | Klise pembuka generik AI (*In today's era...*) | langsung masuk ke topik atau konteks spesifik |

## Rules

- **Integritas Fakta Mutlak**: Dilarang mengarang, mengubah, atau menghilangkan angka, data, fakta, nama tokoh/lembaga, dan sitasi dari draf asal.
- **Anti-Overengineering**: Dilarang memaksakan kosakata arkais/berat, ritme asimetris paksa, burstiness buatan, atau de-nominalisasi kaku yang justru mengaburkan pemahaman pembaca. Prioritas utama adalah kejelasan alami.
- **Larangan Em Dash**: Hasil akhir dilarang memuat em dash (`—`), en dash (`–`), atau double hyphen (`--`).
- **Penanganan Teks Bersih**: Jika teks masukan sudah bagus dan minim tanda AI, jangan mencari-cari kesalahan; pertahankan draf asli.

## Format Luaran

Keluarkan langsung teks hasil tanpa pengantar obrolan, salam penutup, atau catatan pembersihan. Hasil akhir harus 100% teks bersih yang siap langsung disalin dan digunakan.

Jika dan hanya jika pengguna secara eksplisit meminta penjelasan atau catatan perubahan (misal: "jelaskan apa yang diubah"), berikan poin ringkas di akhir teks:

Catatan Perubahan:
- [Pola yang diperbaiki/dihapus, misal: pembuka klise, kalk terjemahan, em dash]

## Verification

1. **Pemeriksaan Tanda Baca**: Pastikan teks bersih dari karakter `[—–]`.
2. **Pemeriksaan Frasa AI**: Pastikan tidak ada frasa klise/kalk yang tertinggal (*dalam lanskap*, *menyelami*, *memainkan peran krusial*, dll.).
3. **Pemeriksaan Integritas Fakta**: Bandingkan seluruh klaim faktual, angka, dan sitasi terhadap draf asal.

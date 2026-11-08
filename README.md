# Manusiakan

[![Lisensi MIT](https://img.shields.io/badge/license-MIT-blue.svg)](LICENSE)
[![Versi](https://img.shields.io/badge/version-2.0.0-green.svg)](CHANGELOG.md)

Pernah baca draf tulisan yang langsung kebongkar kalau itu buatan AI? Kalimat pembuka klise *"Di era digital saat ini..."*, frasa terjemahan kaku kayak *"memainkan peran krusial"*, atau taburan em dash (`—`) di mana-mana.

**Manusiakan** hadir buat membersihkan semua penyakit teks sintetis itu secara presisi (surgical). Filosofinya sederhana: **fokus kenyamanan baca manusia, bukan ngibulin detektor**.

Kami nggak merombak suara aslimu atau memaksakan kosakata berat layaknya sastra lama. Frasa yang bermasalah diperbaiki langsung pada tempatnya, alur argumenmu tetap utuh, dan fakta tidak diutak-atik sama sekali.

## Contoh Transformasi (Sebelum & Sesudah)

Biar kelihatan bedanya, intip contoh bedah terukur di bawah ini:

**Sebelum (Draf Sintetis AI):**
> Di era digital yang berkembang pesat saat ini, keberadaan media sosial memainkan peran krusial dalam membentuk pola perilaku konsumtif generasi muda. Tidak dapat dimungkiri bahwa berbagai platform—mulai dari Instagram, TikTok, hingga e-commerce—terus membombardir pengguna dengan konten promosi yang persuasif. Akibatnya, terjadi peningkatan kecenderungan pembelian impulsif di mana mahasiswa sering kali memprioritaskan gaya hidup daripada kebutuhan esensial mereka demi menavigasi tuntutan validasi sosial di lanskap modern.

**Sesudah (Hasil Bedah Presisi `manusiakan`):**
> Keberadaan media sosial sangat memengaruhi pola perilaku konsumtif generasi muda. Berbagai platform seperti Instagram, TikTok, dan e-commerce terus membombardir pengguna dengan konten promosi yang persuasif. Akibatnya, tren pembelian impulsif meningkat; mahasiswa kerap memprioritaskan gaya hidup dibanding kebutuhan pokok demi memenuhi validasi sosial di lingkungannya.

> [!NOTE] Catatan Pembersihan AI:
> - Memangkas pembuka klise (*Di era digital...*, *Tidak dapat dimungkiri bahwa...*).
> - Mengikis kalk terjemahan asing (*memainkan peran krusial* → *sangat memengaruhi*, *menavigasi* → *memenuhi*, *lanskap* → *lingkungan*).
> - Menghapus em dash (`—`) dan menyederhanakan sambungan antarkalimat.

## Empat Kluster yang Dibersihkan

Manusiakan bekerja lewat audit 3-pass (Audit, Refactor, Finalisasi) yang menyasar 4 kluster utama penanda AI berbasis standar [WP:AISIGNS](https://en.wikipedia.org/wiki/Wikipedia:Signs_of_AI_writing):

1. **Kata & Frasa Inflasi**: Frasa klise dan kalk terjemahan harfiah bahasa Inggris (*dalam lanskap*, *menyelami*, *memainkan peran krusial*).
2. **Retorika Struktural Formulaik**: Pembuka generik (*Di era modern...*, *Tidak dapat dimungkiri bahwa...*), pertentangan semu (*Bukan hanya X, melainkan juga Y*), serta enumerasi triadik (*A, B, dan C*) yang dipaksakan.
3. **Tipografi & Format Khas Mesin**: Tanda pisah em dash (`—`) berulang, format daftar tebal vertikal (`**Kategori:** ...`), dan bullet points mekanis pengganti alur narasi.
4. **Artefak Chatbot**: Sisa pembuka obrolan (*Tentu, berikut draf...*), penutup basa-basi, atau disclaimer khas LLM.

## Tabel Panduan Cepat Kalk Terjemahan

Berikut beberapa kalk terjemahan bahasa Inggris yang paling sering lolos di draf AI dan padanan wajarnya:

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
| `Bukan hanya X, tetapi juga Y` | Formula dikotomi kaku (*Not only X, but Y*) | sebut langsung kedua poin sejajar tanpa kontras semu |
| `Di era [teknologi/digital] yang...` | Klise pembuka generik AI (*In today's era...*) | langsung masuk ke topik atau konteks spesifik |

## Cara Pasang & Pemakaian

Panggil skill dengan perintah `/manusiakan`, *"manusiakan naskah ini"*, atau *"hilangkan gaya bahasa AI di draf berikut"*.

### Claude Code

Pasang langsung lewat marketplace plugin Claude Code:
```bash
/plugin marketplace add dyokism/manusiakan
/plugin install manusiakan@manusiakan
```

Atau pasang via skills CLI:
```bash
npx skills add dyokism/manusiakan --global --agent claude-code
```

### Google Antigravity

Klon langsung ke direktori skills Antigravity lokalmu:
```bash
git clone https://github.com/dyokism/manusiakan.git ~/.gemini/config/skills/manusiakan
```

### Claude Desktop & Claude.ai (Web)

1. Buka halaman [Releases](https://github.com/dyokism/manusiakan/releases).
2. Unduh bundle `manusiakan.skill`.
3. Buka menu **Settings → Capabilities / Skills**, lalu unggah arsipnya.

### Agen Lainnya (Codex, OpenCode, Cursor, dsb.)

```bash
npx skills add dyokism/manusiakan --global --agent '*'
```

## Integritas Fakta & Etika

Manusiakan dirancang untuk memoles draf pemikiran aslimu agar jernih dan nyaman dibaca.

> [!IMPORTANT]
> Skill ini bukan sarana fabrikasi data demi plagiarisme. Nomor, nama tokoh, rujukan sitasi, dan klaim data dari naskah asal wajib dipertahankan seutuhnya tanpa spekulasi halusinasi.

## Lisensi

Dirilis di bawah lisensi terbuka [MIT License](LICENSE). Hak Cipta (c) 2026 dyokism.

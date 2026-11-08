# Changelog

## 2.0.1

- **Format Luaran Murni Tanpa Catatan Default**: Menghapus blok catatan `[!NOTE]` otomatis di akhir luaran agar teks hasil revisi 100% bersih, rapi, dan siap langsung disalin tanpa artefak tag teknis.
- **Catatan Berbasis Permintaan**: Catatan perubahan kini disajikan dengan format teks sederhana (`Catatan Perubahan:`) hanya saat diminta secara eksplisit oleh pengguna.

## 2.0.0

Perombakan total paradigma Manusiakan dari orientasi *ZeroGPT bypass* menuju *Surgical AI Removal* berbasis pedoman komunitas Wikipedia (WP:AISIGNS) dan inspirasi `blader/humanizer`.

- **Bedah Presisi Tanpa Merusak Suara Penulis**: Mengganti frasa bermasalah tepat pada tempatnya, menjaga alur penalaran dan register asli tanpa memaksakan perubahan gaya atau diksi berat.
- **Workflow 3-Pass Terstruktur**: Menerapkan alur audit (Pass 1), refactor terukur (Pass 2), dan finalisasi fakta tanpa halusinasi (Pass 3).
- **Penghapusan Aturan Berlebih**: Mengeliminasi paksaan *burstiness* ekstrem (rasio 3–7 kata vs 30–45 kata), de-nominalisasi kaku, dan pemaksaan gaya editorial tertentu (Prisma/Kompas/Tempo).
- **Format Luaran Transparan**: Teks hasil revisi disajikan langsung disertai blok catatan pembersihan ringkas di akhir.
- **Pembersihan Draf Alami**: Jika teks masukan sudah wajar dan minim pola AI, draf dipertahankan seutuhnya tanpa mencari-cari kesalahan.
- **Pembersihan Repositori**: Menghapus direktori `benchmark/` untuk mengakhiri ketergantungan semu pada skor detektor AI matematis.

## 1.0.0

Rilis perdana Manusiakan: standar kepenulisan agen cerdas untuk merombak teks sintetis AI menjadi bahasa Indonesia bernas, tajam, dan cendekia.

- **Dekonstruksi Kalk Terjemahan (*Translationese*)**: Mengeliminasi pinjaman struktur bahasa Inggris mentah (*dalam lanskap*, *menyelami*, *memainkan peran krusial*, *dalam hal*, *pada akhir hari*) dan menggantinya dengan leksikon alami bahasa Indonesia.
- **De-Nominalisasi & Agensi Aktif**: Membongkar tumpukan kata benda abstrak berimbuhan `pe-an`/`ke-an` menjadi verba tindakan aktif (`meng-`) yang memiliki pelaku konkret.
- **Ritme Asimetris (*Burstiness*)**: Menghilangkan irama kalimat yang monoton (17–22 kata) dengan memadukan kalimat pemukul pendek (3–7 kata) dan kalimat majemuk bertingkat (30–45 kata).
- **Pembersihan Tipografi & Format Mekanis**: Larangan mutlak tanda pisah em dash (`—`), en dash (`–`), dan tanda hubung ganda (`--`). Menghilangkan format daftar vertikal berlabel tebal (`- **Aspek:** ...`) menjadi narasi mengalir.
- **Anti-Tongkat Leksikal**: Membatasi kata transisi favorit sintetis (*kendati*, *walakin*, *tak pelak*, *niscaya*) serta membuang formula pembuka usang (*Di era digital...*, *Tidak dapat dimungkiri bahwa...*).
- **Integritas Fakta & Nol Halusinasi**: Aturan ketat melarang fabrikasi data, klaim, atau nama baru, disertai format pemberitahuan anomali sitasi sumber secara transparan.
- **Integrasi Multi-Platform**: Mendukung instalasi via Claude Plugin Marketplace, `npx skills`, Google Antigravity, dan paket `.skill` untuk Claude Desktop/Web.

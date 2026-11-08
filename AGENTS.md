# Panduan Agen (AGENTS.md)

Dokumen ini memandu agen cerdas (AI agents) dan kontributor dalam mengubah repositori **Manusiakan** tanpa merusak integritas paket, prompt, maupun sinkronisasi versi.

## Isi & Filosofi Repositori

Manusiakan adalah *agent skill* mandiri yang ditulis dalam Markdown. Sumber kebenaran tunggal (*single source of truth*) yang dibaca oleh agen adalah `SKILL.md`. Repositori ini tidak memiliki proses kompilasi (*no build step*).

Jaga portabilitas skill ini agar tetap netral dan dapat berjalan di Claude Code, Google Antigravity, OpenCode, Codex, maupun agen LLM lainnya.

## Berkas Kunci

- `SKILL.md`: Sumber kebenaran tunggal prompt dan metadata. Berisi prinsip bedah terukur (*surgical de-AI*) berbasis WP:AISIGNS, alur 3-pass (Audit, Refactor, Finalisasi), tabel kalk terjemahan AI, dan aturan anti-overengineering.
- `README.md`: Dokumentasi publik dalam Bahasa Indonesia bergaya kasual komunitas, showcase transformasi sebelum & sesudah, tabel frasa cepat, dan panduan instalasi multi-agen.
- `CHANGELOG.md`: Catatan rilis terstruktur dengan versi terbaru di bagian teratas.
- `.claude-plugin/plugin.json`: Manifest plugin Claude Code yang menunjuk ke `./` (root `SKILL.md`).
- `.claude-plugin/marketplace.json`: Manifest marketplace agar repositori dapat dipasang via `/plugin marketplace add`.
- `scripts/validate-package.py`: Skrip mandiri tanpa dependensi eksternal untuk memvalidasi sinkronisasi versi, format YAML, dan kuota kata.
- `.github/workflows/validate.yml`: Workflow CI untuk memeriksa integritas paket pada setiap *pull request* dan *push* ke `main`.
- `.github/workflows/release.yml`: Workflow rilis otomatis yang mengemas arsip bundle `manusiakan.skill` saat tag versi di-push.

## Aturan Perubahan

1. **Sinkronisasi Versi**: Versi yang sama (SemVer 3 bagian, misal `2.0.1`) **wajib** identik di:
   - `SKILL.md` (di bawah `metadata.version`).
   - `CHANGELOG.md` (tajuk tingkat dua pertama: `## 2.0.1`).
   - `.claude-plugin/plugin.json` (field `"version"`).
2. **Sinkronisasi Deskripsi**: Kalimat pertama deskripsi pada `SKILL.md` harus sama persis dengan field `description` pada `.claude-plugin/plugin.json` dan entri plugin di `.claude-plugin/marketplace.json`.
3. **Batas Kata (*Word Budget*)**: Setiap kata di `SKILL.md` dibaca oleh model pada tiap pemanggilan. Jaga agar ukuran `SKILL.md` tetap berada di bawah **5.500 kata** (skrip validasi akan menolak jika melebihi batas ini).
4. **Nol Halusinasi & Preservasi Fakta**: Jangan pernah menambahkan aturan yang melonggarkan verifikasi fakta, data numerik, nama tokoh/lembaga, atau kutipan draf asal.
5. **Kaidah Bahasa**: Gunakan Bahasa Indonesia yang lugas, bernas, dan tertib ortografi EYD V pada seluruh dokumentasi maupun instruksi prompt. Hindari gaya penulisan birokratis pasif dan kata mubazir.

## Alur Kerja Pembaruan Versi (Version Update Workflow)

Saat menyiapkan rilis atau pembaruan versi baru (misalnya dari `2.0.0` ke `2.0.1` atau `2.1.0`), ikuti prosedur berurutan berikut:

### 1. Perbarui Nomor Versi & Catatan
1. Naikkan versi pada [SKILL.md](SKILL.md):
   ```yaml
   metadata:
     version: "X.Y.Z"
   ```
2. Tambahkan entri rilis baru di paling atas [CHANGELOG.md](CHANGELOG.md):
   ```markdown
   ## X.Y.Z

   - Ringkasan pembaruan pola atau perbaikan.
   ```
3. Perbarui `"version": "X.Y.Z"` pada [.claude-plugin/plugin.json](.claude-plugin/plugin.json).
4. Perbarui badge versi pada [README.md](README.md):
   ```markdown
   [![Versi](https://img.shields.io/badge/version-X.Y.Z-green.svg)](CHANGELOG.md)
   ```

### 2. Validasi Lokal
Jalankan skrip validasi paket sebelum melakukan commit:
```bash
python3 scripts/validate-package.py
```
Pastikan keluaran mencatat status valid: `Manusiakan package vX.Y.Z is valid (... words)`.

### 3. Buat Tag & Publikasikan Rilis
Setelah perubahan di-commit ke branch `main`:
```bash
# 1. Buat git tag baru sesuai versi
git tag vX.Y.Z

# 2. Push branch dan tag ke repositori GitHub remote
git push origin main
git push origin vX.Y.Z
```
Setelah tag `vX.Y.Z` terdorong ke GitHub, GitHub Actions di `.github/workflows/release.yml` akan berjalan otomatis untuk:
- Mengemas berkas `manusiakan.skill` (arsip ZIP berisi `SKILL.md` dan `LICENSE`).
- Membuat GitHub Release resmi `vX.Y.Z` dengan catatan rilis terlampir.

# 9Router Setup — Catatan Workflow

Tanggal: 2026-11-18 · Versi 9router: 0.5.119 · Endpoint: `http://localhost:20128/v1`

## Provider

| Provider | Status | Catatan |
|---|---|---|
| `openrouter` | Aktif | API key terhubung. Model free yang lolos uji: `baidu/ernie-5.5-flash-preview:free`, `nvidia/nemotron-3.5-lightning:free`, `nvidia/nemotron-3.5-super-vl:free`, `particle-ai/particle-1:free`, `dots-studio/dots-3-note-preview:free`. |
| `xiaomi-mimo` (`mimo`) | Dinonaktifkan | Saldo habis (402). Sesuai permintaan, Mimo di-skip: koneksi dinonaktifkan dan combo `mimo-coding` dihapus. |
| `sp` (Sumopod, OpenAI-compatible) | Aktif | Node custom diberi kredensial dari `AI_SUMAPOD_RDEV`. ~55 model tersedia, antara lain `sp/deepseek-v4-pro`, `sp/claude-sonnet-5-5`, `sp/glm-5.3`, `sp/gemini/gemini-3.8-flash`, `sp/gpt-5.6-sol`, `sp/hy4-flash`. |
| `thb` (TokenHarbor, OpenAI-compatible) | Aktif | Node `openai-compatible-chat-62b40173-985f-4839-96d8-44ae14644270`, base URL `https://tokenharbor.ai/v1`. Model `:free` lolos uji: `thb/deepseek-v4.1-flash:free`, `thb/deepseek-v4-flash:free`, `thb/mimo-v2.6-flash:free`, `thb/mimo-v2.5:free`. Varian berbayar masih 402. |
| `pecutopus` (PecutOpus, OpenAI-compatible) | Aktif | Node `openai-compatible-chat-pecutopus`, base URL `https://api.pecutopus.web.id/v1`, connection `pecutopus-connection`. ~20 model, tidak ada yang `:free`. Flash yang lolos uji: `pecutopus/pecut/deepseek-v4.1-flash`, `glm-5.3-flash`, `deepseek-v4.1-flash-ultrafast`, `qwen3.8-flash`, `gemini-3.1-flash-lite`, `mimo-v2.6-flash`, `glm-5.3`. |
| `oc` (OpenCode Free) | Sebagian aktif | `oc/big-pickle` jalan. `oc/deepseek-v4.1-flash-free` kena free-usage limit; model `muse-spark-*` sedang unavailable. |

Perbaikan yang dilakukan: dependency `wreq-js` sudah terpasang di `~/.9router/runtime` tetapi server lama berjalan tanpa `NODE_PATH` ke sana. Server di-restart sehingga `oc/*` bisa diakses.

## Combos (strategy: `fallback`)

Combo harus dibuat dengan `kind: "llm"` agar tampil di halaman **Combo & Vision Adapter** di dashboard. Jika dibuat via API dengan `kind: "model"`, datanya tersimpan dan dipakai routing, tetapi UI menyembunyikannya.

Prinsip urutan: **free → pecutopus → sumopod**. Model mahal (Claude Opus/Sonnet, GPT-6) sengaja tidak dijadikan andalan. `free-coding` dan `thb-free` sengaja murni free.

- **free-coding** — 4 model `:free` THB → `oc/big-pickle` → 2 model free OpenRouter
- **thb-free** — `thb/deepseek-v4.1-flash:free` → `thb/deepseek-v4-flash:free` → `thb/mimo-v2.6-flash:free` → `thb/mimo-v2.5:free` → `oc/big-pickle`
- **daily-coding** — free (THB, OC, OpenRouter) → `pecutopus/pecut/deepseek-v4.1-flash` → `pecutopus/pecut/glm-5.3-flash` → `sp/deepseek-v4-flash` → `sp/glm-5.3-flash`
- **fast-cheap** — free (THB, OC) → `pecutopus/pecut/deepseek-v4.1-flash-ultrafast` → `pecutopus/pecut/glm-5.3-flash` → `sp/deepseek-v4-flash` → `sp/hy4-flash`
- **reasoning-coding** — `thb/deepseek-v4.1-flash:free` → `pecutopus/pecut/deepseek-v4.1-flash` → `pecutopus/pecut/glm-5.3` → `sp/deepseek-v4-flash` → `sp/gpt-5.6-sol` (terakhir, hanya jika butuh kualitas ekstra)
- **vision-coding** — free (THB, OpenRouter) → `pecutopus/pecut/gemini-3.1-flash-lite` → `pecutopus/pecut/qwen3.8-flash` → `sp/gemini/gemini-3.5-flash-lite` → `sp/gemini/gemini-3.8-flash`

Catatan harga: 9router tidak mengekspos harga PecutOpus/Sumopod lewat `/api/pricing`. Pilihan murah didasarkan pada kelas model (flash/nano/lite) dan referensi harga publik; semua kandidat sudah diuji HTTP 200. Urutan fallback pecutopus → sumopod sudah diuji dengan combo sementara (model invalid di urutan pertama; request jatuh ke `pecut/deepseek-v4.1-flash`).

Catatan penting: kirim `"stream": true` atau `"stream": false` secara eksplisit. Jika field `stream` dihilangkan, deteksi konten 9router kadang menganggap respons provider sebagai "empty" dan fallback ke model terakhir.

## Token saver

- RTK: aktif (default)
- Ponytail: `full` (diturunkan dari `ultra` — ultra terlalu agresif untuk kode produksi)
- Caveman: aktif, level `full`

## Integrasi OpenCode (sudah diterapkan)

Di `~/.config/opencode/opencode.jsonc`:

- `"model": "9r/free-coding"` sebagai default.
- Provider `9r` → `http://localhost:20128/v1`, API key dibaca dari file: `settings.apiKey: "{file:~/.secrets/9router-key}"` (dibuat `install.sh` dari env `AI_9ROUTER`; env itu sendiri tidak dipakai saat runtime).
- 6 combo didaftarkan sebagai model: `free-coding`, `thb-free`, `daily-coding`, `fast-cheap`, `reasoning-coding`, `vision-coding`.
- Provider `sp` (Sumopod langsung) sengaja **dibiarkan** sesuai permintaan.

Catatan: `9router show`/`connect` membaca `opencode.json`, bukan `opencode.jsonc`, jadi CLI connect tidak dipakai.

Verifikasi: `opencode models` menampilkan ke-6 `9r/*`; `opencode run --model 9r/free-coding` berhasil dan usage harian 9router mencatat request dengan API key tersebut.

## Catatan

- Server bind ke `0.0.0.0` tanpa password. Pemakaian hanya lokal, jadi tidak diubah.
- 9router dijalankan ulang oleh user dengan `9router`.

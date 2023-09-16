# Petunjuk Membuka Deploy Model ML

## Persyaratan
- Python 3.7 atau lebih baru
- Library Python: FastAPI, uvicorn, pydantic, numpy, pandas, dan pickle

## Langkah-langkah
1. Pastikan Anda telah menginstal semua persyaratan yang disebutkan di atas.
2. Unduh kode sumber dari repositori ini.
3. Buka terminal/command prompt dan navigasikan ke direktori tempat Anda menyimpan kode sumber.
4. Jalankan server FastAPI dengan perintah berikut:
    ```bash
    uvicorn main:app --reload
    ```
5. Buka browser dan kunjungi `http://127.0.0.1:8000` untuk melihat aplikasi berjalan.
6. Anda dapat mengakses dokumentasi interaktif FastAPI di `http://127.0.0.1:8000/docs`.
7. Untuk melakukan prediksi, gunakan endpoint `/predict` dengan metode POST dan kirimkan data dalam format JSON.

## Contoh Penggunaan
Berikut adalah contoh penggunaan endpoint `/predict` dengan curl:
```bash
curl -X POST "http://127.0.0.1:8000/predict" -H  "accept: application/json" -H  "Content-Type: application/json" -d "{\"variance\":3.6216,\"skewness\":8.6661,\"curtosis\":-2.8073,\"entropy\":-0.44699}"
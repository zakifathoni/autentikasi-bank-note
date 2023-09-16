# 1. Mengimpor library yang diperlukan
import uvicorn
from fastapi import FastAPI
from BankNotes import BankNote
import numpy as np
import pickle
import pandas as pd

# 2. Membuat objek aplikasi FastAPI
app = FastAPI()
pickle_in = open("classifier.pkl","rb")
classifier=pickle.load(pickle_in)

@app.get('/')
def index():
    """
    Fungsi ini mengembalikan pesan selamat datang ketika pengguna mengakses halaman utama.
    
    Returns:
        dict: Pesan selamat datang.
    """
    return {'message': 'Hey hey, not bad!'}

@app.get('/{name}')
def get_name(name: str):
    """
    Fungsi ini mengembalikan pesan selamat datang kepada pengguna dengan nama yang diberikan.

    Args:
        name (str): Nama pengguna.

    Returns:
        dict: Pesan selamat datang kepada pengguna.
    """
    return {'Welcome here': f'{name}'}

@app.post('/predict')
def predict_banknote(data:BankNote):
    """
    Fungsi ini menerima data nota bank dalam bentuk JSON,
    melakukan prediksi menggunakan model yang telah dilatih,
    dan mengembalikan hasil prediksi.

    Args:
        data (BankNote): Data nota bank yang akan diprediksi.

    Returns:
        dict: Hasil prediksi.
    """
    data = data.dict()
    variance=data['variance']
    skewness=data['skewness']
    curtosis=data['curtosis']
    entropy=data['entropy']
   # print(classifier.predict([[variance,skewness,curtosis,entropy]]))
    prediction = classifier.predict([[variance,skewness,curtosis,entropy]])
    prediction = "Fake note" if (prediction[0]>0.5) else "It's a Bank note"
    return {
        'prediction': prediction
    }

if __name__ == '__main__':
    # Menjalankan aplikasi dengan uvicorn pada http://127.0.0.1:8000
    uvicorn.run(app, host='127.0.0.1', port=8000)
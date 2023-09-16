from pydantic import BaseModel

class BankNote(BaseModel):
    """
    Kelas yang mendeskripsikan pengukuran Nota Bank.

    Args:
    variance (float): Variansi dari gambar nota.
    skewness (float): Kemiringan dari gambar nota.
    curtosis (float): Curtosis dari gambar nota.
    entropy  (float): Entropi dari gambar nota.
    """
    variance: float 
    skewness: float 
    curtosis: float 
    entropy: float
# -*- coding: utf-8 -*-
"""Tugas 2 Pramudya Riandanu .ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/11Pkc1IUdD6WFnvA8NwCo3E-KhyY2V2tV
"""

# import package
import numpy as np
import matplotlib.pyplot as plt

# Fungsi untuk menyelesaikan persamaan diferensial secara analitik
def perubahan_suhu(t, To, Ta, k):
    """
    Menyelesaikan T = Ta + e^(-k * t) * To

    Parameter:
        t : array-like, titik waktu
        To : float, suhu awal
        Ta : suhu ruangan
        k : float, laju perbandingan

    Mengembalikan:
        P : array-like, suhu
    """
    return Ta + np.exp(-k * t) * To

# Parameter contoh
To = 90  # suhu awal
Ta = 25  #suhu ruangan
k = 0.1   # Laju perubahan suhu (10% per satuan suhu)
t = np.linspace(0, 100, 5)  # Titik waktu dari 0 hingga 100(menit)

# Menyelesaikan persamaan
T = perubahan_suhu(t, To, Ta, k)

# Plot hasilnya
plt.figure(figsize=(8, 6))
plt.plot(t, T, label=f"T = {Ta} + exp({-k} * t) * To", color="magenta")
plt.title("Perubahan suhu kopi")
plt.xlabel("Waktu (t)")
plt.ylabel("Suhu (T)")
plt.legend()
plt.grid()
plt.show()
import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import sympy as sp

st.title("Project UAS Matematika Komputasi")

st.write("""
Aplikasi ini digunakan untuk mencari akar persamaan nonlinier menggunakan:

1. Metode Bisection
2. Metode Newton-Raphson
3. Metode Secant
""")

metode = st.selectbox(
    "Pilih metode yang akan digunakan:",
    ["Bisection", "Newton-Raphson", "Secant"]
)

st.write("Metode yang dipilih:", metode)

if metode == "Bisection":

    st.header("Metode Bisection")

    fungsi = st.text_input(
        "Masukkan fungsi",
        value="x**3 - 4*x - 9"
    )

    batas_bawah = st.number_input(
        "Masukkan batas bawah",
        value=2.0
    )

    batas_atas = st.number_input(
        "Masukkan batas atas",
        value=3.0
    )

    toleransi = st.number_input(
        "Masukkan toleransi",
        value=0.001,
        format="%.6f"
    )

    if st.button("Hitung Bisection"):

        def hitung_fungsi(x):
            return eval(fungsi)

        if hitung_fungsi(batas_bawah) * hitung_fungsi(batas_atas) > 0:

            st.error(
                "Interval tidak memenuhi syarat Metode Bisection"
            )

        else:

            data_iterasi = []

            jumlah_iterasi = 0

            while abs(batas_atas - batas_bawah) > toleransi:

                titik_tengah = (
                    batas_bawah + batas_atas
                ) / 2

                data_iterasi.append([
                    jumlah_iterasi + 1,
                    batas_bawah,
                    batas_atas,
                    titik_tengah
                ])

                if (
                    hitung_fungsi(batas_bawah)
                    * hitung_fungsi(titik_tengah)
                    < 0
                ):
                    batas_atas = titik_tengah
                else:
                    batas_bawah = titik_tengah

                jumlah_iterasi += 1

            akar = (
                batas_bawah + batas_atas
            ) / 2

            st.success(
                f"Akar persamaan = {akar}"
            )

            st.write(
                f"Jumlah iterasi = {jumlah_iterasi}"
            )

            tabel_iterasi = pd.DataFrame(
                data_iterasi,
                columns=[
                    "Iterasi",
                    "Batas Bawah",
                    "Batas Atas",
                    "Titik Tengah"
                ]
            )

            st.dataframe(tabel_iterasi)

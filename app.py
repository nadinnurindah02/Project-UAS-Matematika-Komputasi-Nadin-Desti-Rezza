import streamlit as st

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

import streamlit as st
from streamlit_option_menu import option_menu

#sidebar
with st.sidebar:
    selected=option_menu ('HITUNG LUAS BANGUN',
    ['HITUNG LUAS PERSEGI PANJANG',
     'HITUNG LUAS SEGITIGA'],      
    default_index=0)

#halaman persegipanjang
if(selected== 'HITUNG LUAS PERSEGI PANJANG'):
    st.title('HITUNG LUAS PERSEGI PANJANG')

    panjang= st.number_input("MASUKAN NILAI PANJANG", 0)
    lebar= st.number_input("MASUKAN NILAI LEBAR", 0)
    hitung= st.button("HITUNG")

    if hitung :
        luas = panjang * lebar
        st.write("LUAS PERSEGI PANJANG =", luas)
        st.success(f"LUAS PERSEGI PANJANG = {luas}")

if(selected== 'HITUNG LUAS SEGITIGA'):
    st.title('HITUNG LUAS SEGITIGA')

    alas=st.slider("MASUKAN NILAI ALAS",0,100)
    tinggi=st.slider("MASUKAN NILAI TIMGGI",0,100)
    hitung= st.button("HITUNG")

    if hitung :
        luas = 0.5 * alas * tinggi
        st.write("LUAS SEGITIGA =", luas)
        st.success(f"LUAS SEGITIGA = {luas}")
   
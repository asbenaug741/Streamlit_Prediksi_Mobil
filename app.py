
import streamlit as st

st.title('Prediksi Harga Mobil Bekas')

year = st.number_input('input tahun mobil')
Present_Price = st.number_input('input harga mobil terbaru')
Kms_Driven = st.number_input('input km mobil')
Fuel_Type = st.number_input('input tipe bahan bakar mobil')
Seller_Type = st.number_input('input jenis penjual')
Transmission = st.number_input('input jenis transmisi mobil')
Owner = st.number_input('input jumlah kepemilikan mobil sebelumnya')

predict = ''
if st.button('estimasi harga:'):
  predict = rf_model.predict(
    [[year, Present_Price, Kms_Driven, Fuel_Type, Seller_Type, Transmission, Owner]]
  )
  st.write('estimasi harga mobil bekas dalam rupiah;', predict*2053000)

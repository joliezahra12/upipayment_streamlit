import pickle
import streamlit as st

# Membaca model
upitrans_model = pickle.load(open('upitrans_model.sav', 'rb'))

# Judul web
st.title('Prediksi Status')

# Membuat input
amount_inr = st.text_input('Input Amount (INR)')

# Code untuk prediksi
upitrans_pred = ''

# Membuat tombol untuk prediksi
if st.button('Test Prediksi Status'):
    try:
        # Coba konversi input menjadi float
        amount_inr = float(amount_inr)
        
        # Debugging: Tampilkan nilai amount_inr
        st.write(f'Nilai Amount (INR) yang dimasukkan: {amount_inr}')
        
        # Pastikan input ke model adalah array 2D
        input_data = [[amount_inr]]
        
        # Debugging: Tampilkan format input_data
        st.write(f'Format Input Data: {input_data}')
        
        # Prediksi menggunakan model
        upitrans_pred = upitrans_model.predict(input_data)
        
        # Debugging: Tampilkan hasil prediksi sebelum menampilkan ke UI
        st.write(f'Hasil Prediksi dari Model: {upitrans_pred}')
        
        # Menampilkan hasil prediksi
        st.success(f'Prediksi Status: {upitrans_pred[0]}')
    
    except ValueError:
        st.error('Input Amount (INR) harus berupa angka.')
    except Exception as e:
        st.error(f'Error: {e}')

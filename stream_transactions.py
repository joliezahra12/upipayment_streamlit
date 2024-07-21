import pickle
import streamlit as st

# Membaca model
diabetes_model = pickle.load(open('upitrans_model.sav', 'rb'))

# Judul web
st.title('Prediksi Status')

# Membagi kolom
col1 = st.columns(1)

with col1:
    amount_inr = st.text_input('Input Amount (INR)')

# Code untuk prediksi
upitrans_pred = ''

# Membuat tombol untuk prediksi
if st.button('Test Prediksi Status'):
    try:
        amount_inr = float(amount_inr)  # Konversi input menjadi float
        upitrans_pred = diabetes_model.predict([[amount_inr]])

        # Memetakan hasil prediksi
        if upitrans_pred == 'FAILED':
            upitrans_pred = 0
        elif upitrans_pred == 'SUCCESS':
            upitrans_pred = 1
        else:
            upitrans_pred = None

        st.success(f'Prediksi Status: {upitrans_pred}')
    except ValueError:
        st.error('Input Amount (INR) harus berupa angka.')

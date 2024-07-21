import pickle
import streamlit as st

# Membaca model
diabetes_model = pickle.load(open('upitrans_model.sav', 'rb'))

# Judul web
st.title('Prediksi Status')

# Membagi kolom
col1, col2 = st.columns(2)

with col1:
    TransactionID = st.text_input('Input TransactionID')

with col2:
    SenderName = st.text_input('Input SenderName')

with col1:
    SenderUPIID = st.text_input('Input SenderUPIID')

with col2:
    ReceiverName = st.text_input('Input ReceiverName')

with col1:
    ReceiverUPIID = st.text_input('Input ReceiverUPIID')

with col2:
    Timestamp = st.text_input('Input Timestamp')

# Code untuk prediksi
upitrans_pred = ''

# Membuat tombol untuk prediksi
if st.button('Test Prediksi Status'):
    upitrans_pred = diabetes_model.predict([[TransactionID, SenderName, SenderUPIID, ReceiverName, ReceiverUPIID, Timestamp]])

    # Memetakan hasil prediksi
    if upitrans_pred == 'FAILED':
        upitrans_pred = 0
    elif upitrans_pred == 'SUCCESS':
        upitrans_pred = 1
    else:
        upitrans_pred = None

    st.success(f'Prediksi Status: {upitrans_pred}')

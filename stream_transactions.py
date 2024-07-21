import pickle
import streamlit as st
from sklearn.preprocessing import LabelEncoder

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
    # Label encoding untuk data string
    le = LabelEncoder()
    encoded_sender_name = le.fit_transform([SenderName])
    encoded_sender_upi_id = le.fit_transform([SenderUPIID])
    encoded_receiver_name = le.fit_transform([ReceiverName])
    encoded_receiver_upi_id = le.fit_transform([ReceiverUPIID])
    encoded_transaction_id = le.fit_transform([TransactionID])
    encoded_timestamp = le.fit_transform([Timestamp])

    # Prediksi menggunakan model
    upitrans_pred = diabetes_model.predict([[encoded_transaction_id[0], encoded_sender_name[0], encoded_sender_upi_id[0], encoded_receiver_name[0], encoded_receiver_upi_id[0], encoded_timestamp[0]]])

    # Memetakan hasil prediksi
    if upitrans_pred == 'FAILED':
        upitrans_pred = 0
    elif upitrans_pred == 'SUCCESS':
        upitrans_pred = 1
    else:
        upitrans_pred = None

    st.success(f'Prediksi Status: {upitrans_pred}')

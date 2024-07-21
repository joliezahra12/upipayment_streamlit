import pickle
import streamlit as st

# membaca model
diabetes_model = pickle.load(open('upitrans_model.sav', 'rb'))

#judul web
st.title('Prediksi Status')

#membagi kolom
col1, col2 = st.columns(2)

with col1 :
    TransactionID = st.text_input ('input TransactionID')

with col2 :
    SenderName = st.text_input ('input SenderName')

with col1 :
    SenderUPIID = st.text_input ('input SenderUPIID')

with col2 :
    ReceiverName = st.text_input ('input ReceiverName')

with col1 :
    ReceiverUPIID = st.text_input ('input ReceiverUPIID')

with col2 :
    Timestamp = st.text_input ('input Timestamp')


# code untuk prediksi
upitrans_pred = ''

# membuat tombol untuk prediksi
if st.button('Test Prediksi Status'):
    resto_prediction = resto_model.predict([[TransactionID, SenderName, SenderUPIID, ReceiverName, ReceiverUPIID, Timestamp]])

   if upitrans_pred == 'Failed':
    return 0
elif upitrans_pred == 'SUCCESS':
    return 1
else:
    return None
st.success(upitrans_pred)

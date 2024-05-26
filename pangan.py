import streamlit as st
import pickle
import pandas as pd
from sklearn.preprocessing import LabelEncoder, OneHotEncoder
from sklearn.ensemble import RandomForestClassifier
import logging
logging.basicConfig(level=logging.INFO)



#create a function to preprocess the data
def main():
    
    #set page title
    st.set_page_config(page_title='Prediksi Ketersediaan Pangan di Kabupaten Pangandaran')
    #set heading
    st.sidebar.title('Data Ketersediaan Pangan')
    
    #INPUT KOMODITAS
    komoditas = st.sidebar.selectbox('komoditas', ['BERAS', 'JAGUNG', 'BAWANG MERAH', 'BAWANG PUTIH', 'CABAI BESAR', 'CABAI RAWIT', 'DAGING SAPI/KERBAU', 'DAGING AYAM RAS', 'TELUR AYAM RAS', 'GULA PASIR', 'MINYAK GORENG'])
    if komoditas=="BERAS":
        komoditas=1
    elif komoditas=="JAGUNG":
        komoditas=2
    elif komoditas=="BAWANG MERAH":
        komoditas=3
    elif komoditas=="BAWANG PUTIH":
        komoditas=4
    elif komoditas=="CABAI BESAR":
        komoditas=5
    elif komoditas=="CABAI RAWIT":
        komoditas=6
    elif komoditas=="DAGING SAPI/KERBAU":
        komoditas=7
    elif komoditas=="DAGING AYAM RAS":
        komoditas=8
    elif komoditas=="TELUR AYAM RAS":
        komoditas=9
    elif komoditas=="GULA PASIR":
        komoditas=10  
    elif komoditas=="MINYAK GORENG":
        komoditas=11
    
    #INPUT KEBUTUHAN
    kebutuhan = st.sidebar.number_input('kebutuhan', min_value=0.360000, max_value=810.176971, step=0.360000)
    
    #INPUT KETERSEDIAAN
    ketersediaan = st.sidebar.number_input('ketersediaan', min_value=-100.0, max_value=820.000000, step=0.000000)
    
    #INPUT NERACA
    neraca = st.sidebar.number_input('neraca', min_value=-100.0, max_value=860.000000, step=0.000000)
    
    #INPUT MINGGU KE
    minggu_ke = st.sidebar.selectbox('minggu_ke', [1, 2, 3, 4, 5])
    if minggu_ke==1:
        minggu_ke=1
    elif minggu_ke==2:
        minggu_ke=2
    elif minggu_ke==3:
        minggu_ke=3
    elif minggu_ke==4:
        minggu_ke=4
    elif minggu_ke==5:
        minggu_ke=5
        
    #INPUT BULAN
    bulan = st.sidebar.selectbox('bulan', ['JANUARI', 'FEBRUARI', 'MARET', 'APRIL', 'MEI', 'JUNI', 'JULI', 'AGUSTUS', 'SEPTEMBER', 'OKTOBER', 'NOVEMBER', 'DESEMBER'])
    if bulan=="JANUARI":
        bulan=1
    elif bulan=="FEBRUARI":
        bulan=2
    elif bulan=="MARET":
        bulan=3
    elif bulan=="APRIL":
        bulan=4
    elif bulan=="MEI":
        bulan=5
    elif bulan=="JUNI":
        bulan=6
    elif bulan=="JULI":
        bulan=7
    elif bulan=="AGUSTUS":
        bulan=8
    elif bulan=="SEPTEMBER":
        bulan=9
    elif bulan=="OKTOBER":
        bulan=10
    elif bulan=="NOVEMBER":
        bulan=11
    elif bulan=="DESEMBER":
        bulan=12

    
    #INPUT TAHUN
    tahun = st.sidebar.selectbox('tahun', [2022, 2023])
    if tahun==2022:
        tahun=1
    else:
        tahun=0
    

        
    #create a dictionary with input data
    input_data = {
        'komoditas': [komoditas],
        'kebutuhan': [kebutuhan],
        'ketersediaan': [ketersediaan],
        'neraca': [neraca],
        'minggu_ke': [minggu_ke],
        'bulan': [bulan],
        'tahun': [tahun]
    }
    
    #create a dataframe from the input data
    input_df = pd.DataFrame(input_data)
    
    #train the model
    model = pickle.load(open('pangan.pkl', 'rb'))
    
    #make klasifikasi
    st.markdown(f'<h1 style="text-align: center; color: brown;">Prediksi Ketersediaan Pangan di Kabupaten Pangandaran</h1>', unsafe_allow_html=True)
    st.write('Prediksi ketersediaan pangan di Kabupaten Pangandaran merupakan suatu usaha untuk memproyeksikan atau mengantisipasi jumlah, jenis, dan status ketersediaan pangan di wilayah Kabupaten Pangandaran dalam periode waktu tertentu.')
    
    #display the predicition
    st.title("Hasil Klasifikasinya Adalah:")
    if st.button('Predict'):
        #make predictions
        prediction = prediction = model.predict(input_df)[0]
        
        #display the prediction
        if prediction == 0:
            st.markdown("<h2 style='color:red;'>DEFISIT</h2>", unsafe_allow_html=True)
            st.write("Kondisi ketersediaan pangan kurang dari yang dibutuhkan atau diharapkan untuk memenuhi kebutuhan masyarakat tertentu di Kabupaten Pangandaran")
        else:
            st.markdown("<h2 style='color:green;'>SURPLUS</h2>", unsafe_allow_html=True)
            st.write("Kondisi ketersediaan pangan lebih banyak yang tersedia daripada yang dibutuhkan untuk memenuhi kebutuhan masyarakat di Kabupaten Pangandaran")

if __name__ == '__main__':
    main()
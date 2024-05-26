import streamlit as st
import pickle
import pandas as pd
import logging
from sklearn.ensemble import RandomForestClassifier

logging.basicConfig(level=logging.INFO)

#create a function to preprocess the data
def main():
    # Set page title
    st.set_page_config(page_title='Prediksi Ketersediaan Pangan di Kabupaten Pangandaran')
    # Set heading
    st.sidebar.title('Data Ketersediaan Pangan')
    
    # INPUT KOMODITAS
    komoditas = st.sidebar.selectbox('komoditas', ['BERAS', 'JAGUNG', 'BAWANG MERAH', 'BAWANG PUTIH', 'CABAI BESAR', 'CABAI RAWIT', 'DAGING SAPI/KERBAU', 'DAGING AYAM RAS', 'TELUR AYAM RAS', 'GULA PASIR', 'MINYAK GORENG'])
    komoditas_dict = {'BERAS': 1, 'JAGUNG': 2, 'BAWANG MERAH': 3, 'BAWANG PUTIH': 4, 'CABAI BESAR': 5, 'CABAI RAWIT': 6, 'DAGING SAPI/KERBAU': 7, 'DAGING AYAM RAS': 8, 'TELUR AYAM RAS': 9, 'GULA PASIR': 10, 'MINYAK GORENG': 11}
    komoditas = komoditas_dict[komoditas]
    
    # INPUT KEBUTUHAN
    kebutuhan = st.sidebar.number_input('kebutuhan', min_value=0.360000, max_value=810.176971, step=0.360000)
    
    # INPUT KETERSEDIAAN
    ketersediaan = st.sidebar.number_input('ketersediaan', min_value=-100.0, max_value=820.000000, step=0.000000)
    
    # INPUT NERACA
    neraca = st.sidebar.number_input('neraca', min_value=-100.0, max_value=860.000000, step=0.000000)
    
    # INPUT MINGGU KE
    minggu_ke = st.sidebar.selectbox('minggu_ke', [1, 2, 3, 4, 5])
    
    # INPUT BULAN
    bulan = st.sidebar.selectbox('bulan', ['JANUARI', 'FEBRUARI', 'MARET', 'APRIL', 'MEI', 'JUNI', 'JULI', 'AGUSTUS', 'SEPTEMBER', 'OKTOBER', 'NOVEMBER', 'DESEMBER'])
    bulan_dict = {'JANUARI': 1, 'FEBRUARI': 2, 'MARET': 3, 'APRIL': 4, 'MEI': 5, 'JUNI': 6, 'JULI': 7, 'AGUSTUS': 8, 'SEPTEMBER': 9, 'OKTOBER': 10, 'NOVEMBER': 11, 'DESEMBER': 12}
    bulan = bulan_dict[bulan]
    
    # INPUT TAHUN
    tahun = st.sidebar.selectbox('tahun', [2022, 2023])
    tahun = 1 if tahun == 2022 else 0
    
    # Create a dictionary with input data
    input_data = {
        'komoditas': [komoditas],
        'kebutuhan': [kebutuhan],
        'ketersediaan': [ketersediaan],
        'neraca': [neraca],
        'minggu_ke': [minggu_ke],
        'bulan': [bulan],
        'tahun': [tahun]
    }
    
    # Create a dataframe from the input data
    input_df = pd.DataFrame(input_data)
    
    # Log the input DataFrame
    logging.info(f"Input DataFrame: {input_df}")
    
    # Load the trained model
    try:
        model = pickle.load(open('pangan.pkl', 'rb'))
    except Exception as e:
        st.error(f"Error loading the model: {e}")
        return
    
    # Display the prediction title
    st.markdown('<h1 style="text-align: center; color: brown;">Prediksi Ketersediaan Pangan di Kabupaten Pangandaran</h1>', unsafe_allow_html=True)
    st.write('Prediksi ketersediaan pangan di Kabupaten Pangandaran merupakan suatu usaha untuk memproyeksikan atau mengantisipasi jumlah, jenis, dan status ketersediaan pangan di wilayah Kabupaten Pangandaran dalam periode waktu tertentu.')
    
    # Display the prediction
    st.title("Hasil Klasifikasinya Adalah:")
    if st.button('Predict'):
        # Make predictions
        try:
            prediction = model.predict(input_df)[0]
            # Display the prediction
            if prediction == 0:
                st.markdown("<h2 style='color:red;'>DEFISIT</h2>", unsafe_allow_html=True)
                st.write("Kondisi ketersediaan pangan kurang dari yang dibutuhkan atau diharapkan untuk memenuhi kebutuhan masyarakat tertentu di Kabupaten Pangandaran")
            else:
                st.markdown("<h2 style='color:green;'>SURPLUS</h2>", unsafe_allow_html=True)
                st.write("Kondisi ketersediaan pangan lebih banyak yang tersedia daripada yang dibutuhkan untuk memenuhi kebutuhan masyarakat di Kabupaten Pangandaran")
        except Exception as e:
            st.error(f"Error making prediction: {e}")

if __name__ == '__main__':
    main()

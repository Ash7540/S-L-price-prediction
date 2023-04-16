import streamlit as st
import pandas as pd
import joblib

# Load the pre-trained model
model = joblib.load('smartphone_model.joblib')


# Define the reshaped lists

brand_options = ['MOTOROLA', 'Infinix', 'realme', 'POCO', 'REDMI', 'SAMSUNG',
                 'Micromax', 'Google', 'vivo', 'Realme', 'OPPO', 'itel', 'VIVO',
                 'Tecno', 'Nothing', 'ASUS', 'Mi', 'Redmi', 'YU', 'LAVA', 'IQOO',
                 'Xiaomi', 'I', 'Moto', 'LYF']
brand_options_encoded = list(range(len(brand_options)))
processor_options = ['Snapdragon', 'Helio', 'Spreadtrum']
processor_options_encoded = list(range(len(processor_options)))


def main():

    # Define the app layout
    st.title('Mobile Price Predictor')
    st.write('Enter the specifications of the laptop to get a price prediction:')

    # Define the input fields

    brand = st.selectbox('Brand', brand_options, index=0)
    brand_encoded = brand_options_encoded[brand_options.index(brand)]
    rating = st.slider('Rating (out of 5)', 0.0, 5.0, 4.0, 0.1)
    processor = st.selectbox('Processor', processor_options, index=0)
    processor_encoded = processor_options_encoded[processor_options.index(
        processor)]
    ram = st.slider('RAM', 1, 16, 6, 1)
    storage = st.slider('Storage (in GB)', 8, 256, 108, 8)
    display = st.slider('Display (in cm)', 13.00, 20.00, 14.00, 0.01)
    rearcamera1 = st.slider('Rear Camera 1', 2, 108, 64, 1)
    rearcamera2 = st.slider('Rear Camera 2', 2, 50, 25, 1)
    rearcamera3 = st.slider('Rear Camera 3', 2, 12, 6, 1)
    frontcamera = st.slider('Front Camera', 2, 60, 30, 1)
    battery = st.slider('Battery', 3000, 6000, 4500, 10)

    # Create a predict button
    if st.button('Predict'):
        # Create a DataFrame with the input data
        new_data = pd.DataFrame({'Brand_Encoded': [brand_encoded],
                                 'Rating': [rating],
                                 'Processor_Encoded': [processor_encoded],
                                 'RAM': [ram],
                                 'Storage': [storage],
                                 'Display': [display],
                                 'RearCamera1': [rearcamera1],
                                 'RearCamera2': [rearcamera2],
                                 'RearCamera3': [rearcamera3],
                                 'FrontCamera': [frontcamera],
                                 'Battery': [battery]})

        prediction = model.predict(new_data)

        # Display the prediction to the user
        st.write(f'Estimated price: Rs{prediction[0]:,.2f}')


if __name__ == '__main__':
    main()

import pickle
import streamlit as st

st.title("Dự đoán giá nhà")
st.write("Thực hành deploy mô hình lên streamlit")

@st.cache_resource
def load_model():
    with open('/home/u22/mlops/basic-deployment/notebook/model2.pkl', 'rb') as file:
        return pickle.load(file)
    
model = load_model()

def predict(bedrooms, bathrooms, size):
    x = [[bedrooms, bathrooms, size]]
    return model.predict(x)[0]

bedrooms = st.number_input('Dien tich phong ngu', min_value=1, max_value=50, value=1, step=1)
bathrooms = st.number_input('Dien tich phong tam', min_value=1, max_value=50, value=1, step=1)
size = st.number_input('Size (sqft)', min_value=230.0, max_value=65535.0, value=230.0, step=10.0)

if st.button('Predict'):
    price = predict(bathrooms, bedrooms, size)
    st.write(f"Du doan gia cua ngoi nha la ${price:,.2f}")
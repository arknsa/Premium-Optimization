import streamlit as st
import pandas as pd
import joblib

# Definisi pilihan dropdown dengan deskripsi singkat
education_levels = ['High School', 'PhD', 'Bachelor', 'Master']

interaction_levels = [
    "Low (<5 interaksi)",      # rendah
    "Medium (5-14 interaksi)", # sedang
    "High (≥15 interaksi)"     # tinggi
]

customer_preferences = [
    "Eco-Friendly (Produk ramah lingkungan)", 
    "Price Sensitive (Mengutamakan harga murah)", 
    "Brand Loyal (Setia pada merek tertentu)", 
    "No Preference (Tidak ada preferensi khusus)"
]

@st.cache_resource
def load_model():
    return joblib.load('ridge_model.pkl')

st.title("🛡️ Insurance Premium Prediction (Ridge Model)")
st.write("Fill in the data below to predict the **Premium Amount**.")

education = st.selectbox("Education Level", education_levels)
interaction = st.selectbox("Interactions with Customer Service", interaction_levels)
insurance_products_owned = st.number_input("Insurance Products Owned (jumlah produk)", min_value=0, step=1, value=0)
deductible = st.number_input("Deductible", min_value=0.0, step=1.0, value=0.0)
customer_preference = st.selectbox("Customer Preferences", customer_preferences)

# Mapping untuk label encoding sesuai training
edu_map = {v: i for i, v in enumerate(education_levels)}

# Mapping interaction levels (buang deskripsi saat encode)
interaction_map_keys = ["Low", "Medium", "High"]
interaction_map = {v: i for i, v in enumerate(interaction_map_keys)}
selected_interaction_key = interaction.split(" ")[0]  # Ambil kata pertama (Low/Medium/High)

# Mapping customer preferences (buang deskripsi saat encode)
cust_pref_map_keys = [
    "Eco-Friendly",
    "Price Sensitive",
    "Brand Loyal",
    "No Preference"
]
cust_pref_map = {v: i for i, v in enumerate(cust_pref_map_keys)}
selected_pref_key = customer_preference.split(" (")[0]

if st.button("Predict Premium"):
    X_new = pd.DataFrame([[
        edu_map[education],
        interaction_map[selected_interaction_key],
        insurance_products_owned,
        deductible,
        cust_pref_map[selected_pref_key]
    ]], columns=[
        "Education Level",
        "Interactions with Customer Service",
        "Insurance Products Owned",
        "Deductible",
        "Customer Preferences"
    ])
    
    model = load_model()
    pred = model.predict(X_new)[0]
    st.success(f"💰 **Predicted Premium Amount:** `{pred:,.2f}`")

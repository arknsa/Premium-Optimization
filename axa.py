import streamlit as st
import pandas as pd
import joblib

# Define dropdown options with brief descriptions
education_levels = ['High School', 'PhD', 'Bachelor', 'Master']

interaction_levels = [
    "Low (<5 interactions)",      # low
    "Medium (5-14 interactions)", # medium
    "High (≥15 interactions)"     # high
]

customer_preferences = [
    "Eco-Friendly (Environmentally friendly products)", 
    "Price Sensitive (Prioritizing low prices)", 
    "Brand Loyal (Loyal to a specific brand)", 
    "No Preference (No specific preference)"
]

insurance_products_owned_options = [
    "Health",
    "Auto",
    "Multiple",
    "Life",
    "Home",
    "Travel"
]

@st.cache_resource
def load_model():
    return joblib.load('ridge_model.pkl')

st.title("PREMO (Premium Optimization through Regression Modeling)")
st.write("Fill in the data below to predict the **Premium Amount**.")

education = st.selectbox("Education Level", education_levels)
interaction = st.selectbox("Interactions with Customer Service", interaction_levels)
insurance_products_owned = st.selectbox("Insurance Products Owned", insurance_products_owned_options)
deductible = st.number_input("Deductible", min_value=0.0, step=1.0, value=0.0)
customer_preference = st.selectbox("Customer Preferences", customer_preferences)

# Mapping for label encoding according to training
edu_map = {v: i for i, v in enumerate(education_levels)}

# Mapping interaction levels (remove description when encoding)
interaction_map_keys = ["Low", "Medium", "High"]
interaction_map = {v: i for i, v in enumerate(interaction_map_keys)}
selected_interaction_key = interaction.split(" ")[0]  # Take the first word (Low/Medium/High)

# Mapping customer preferences (remove description when encoding)
cust_pref_map_keys = [
    "Eco-Friendly",
    "Price Sensitive",
    "Brand Loyal",
    "No Preference"
]
cust_pref_map = {v: i for i, v in enumerate(cust_pref_map_keys)}
selected_pref_key = customer_preference.split(" (")[0]

# Mapping insurance products owned
insurance_map = {"Health": 0, "Auto": 1, "Multiple": 2, "Life": 3, "Home": 4, "Travel": 5}

if st.button("Predict Premium"):
    X_new = pd.DataFrame([[
        edu_map[education],
        interaction_map[selected_interaction_key],
        insurance_map[insurance_products_owned],
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
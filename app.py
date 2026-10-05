import streamlit as st
import pandas as pd
import joblib

# --------------------------------------------------
# PAGE CONFIGURATION
# --------------------------------------------------

st.set_page_config(
    page_title="Air Quality Prediction",
    page_icon="🌍",
    layout="wide"
)

# --------------------------------------------------
# LOAD MODEL
# --------------------------------------------------

model = joblib.load("air_quality_model.pkl")

# --------------------------------------------------
# WEBSITE STYLING
# --------------------------------------------------

st.markdown("""
<style>

.main {
    background-color: #f5f7fa;
}

h1 {
    color: #1f4e79;
    font-size: 42px;
}

h2 {
    color: #2c3e50;
}

h3 {
    color: #34495e;
}

[data-testid="stSidebar"] {
    background-color: #eaf4f4;
}

[data-testid="stSidebar"] h1,
[data-testid="stSidebar"] h2,
[data-testid="stSidebar"] h3 {
    color: #1f4e79;
}

.stButton > button {
    width: 100%;
    border-radius: 8px;
    font-size: 16px;
    font-weight: 600;
}

.stMetric {
    background-color: white;
    padding: 15px;
    border-radius: 10px;
}

</style>
""", unsafe_allow_html=True)

# --------------------------------------------------
# SIDEBAR NAVIGATION
# --------------------------------------------------

st.sidebar.title("🌍 Air Quality App")

page = st.sidebar.radio(
    "Select a page:",
    [
        "Home / Overview",
        "AQI Prediction",
        "Air Quality Analysis",
        "Visualizations",
        "About"
    ]
)

# ==================================================
# HOME PAGE
# ==================================================

if page == "Home / Overview":

    st.title("🌍 Air Quality Prediction and Analysis")

    st.subheader("Using Machine Learning")

    st.write(
        "This application uses Machine Learning to predict "
        "the Air Quality Index (AQI) using pollution and "
        "environmental features."
    )

    st.markdown("---")

    st.subheader("📊 Model Performance")

    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric("Best Model", "Random Forest")

    with col2:
        st.metric("R² Score", "0.9106")

    with col3:
        st.metric("RMSE", "40.46")

    st.markdown("---")

    st.subheader("🎯 Project Objective")

    st.write(
        "The main objective of this project is to analyze air "
        "quality data and predict AQI using Machine Learning."
    )

    st.success(
        "Use the AQI Prediction page to enter pollution values "
        "and predict the Air Quality Index."
    )

# ==================================================
# AQI PREDICTION PAGE
# ==================================================

elif page == "AQI Prediction":

    st.title("🎯 AQI Prediction")

    st.write(
        "Enter the air pollution values below to predict "
        "the Air Quality Index (AQI)."
    )

    # City and State
    city_options = {
        "Ahmedabad - Gujarat": "Ahmedabad",
        "Amritsar - Punjab": "Amritsar",
        "Bengaluru - Karnataka": "Bengaluru",
        "Bhopal - Madhya Pradesh": "Bhopal",
        "Bhubaneswar - Odisha": "Bhubaneswar",
        "Chandigarh - Chandigarh": "Chandigarh",
        "Chennai - Tamil Nadu": "Chennai",
        "Coimbatore - Tamil Nadu": "Coimbatore",
        "Delhi - Delhi": "Delhi",
        "Gurugram - Haryana": "Gurugram",
        "Guwahati - Assam": "Guwahati",
        "Hyderabad - Telangana": "Hyderabad",
        "Jaipur - Rajasthan": "Jaipur",
        "Jodhpur - Rajasthan": "Jodhpur",
        "Kochi - Kerala": "Kochi",
        "Kolkata - West Bengal": "Kolkata",
        "Lucknow - Uttar Pradesh": "Lucknow",
        "Mumbai - Maharashtra": "Mumbai",
        "Patna - Bihar": "Patna",
        "Pune - Maharashtra": "Pune",
        "Thiruvananthapuram - Kerala": "Thiruvananthapuram",
        "Visakhapatnam - Andhra Pradesh": "Visakhapatnam"
    }

    selected_city = st.selectbox(
        "Select City and State",
        list(city_options.keys())
    )

    city = city_options[selected_city]

    # Pollution inputs
    pm25 = st.number_input(
        "PM2.5",
        min_value=0.0,
        value=50.0
    )

    pm10 = st.number_input(
        "PM10",
        min_value=0.0,
        value=50.0
    )

    no = st.number_input(
        "NO",
        min_value=0.0,
        value=10.0
    )

    no2 = st.number_input(
        "NO2",
        min_value=0.0,
        value=20.0
    )

    nox = st.number_input(
        "NOx",
        min_value=0.0,
        value=30.0
    )

    nh3 = st.number_input(
        "NH3",
        min_value=0.0,
        value=10.0
    )

    co = st.number_input(
        "CO",
        min_value=0.0,
        value=1.0
    )

    so2 = st.number_input(
        "SO2",
        min_value=0.0,
        value=10.0
    )

    o3 = st.number_input(
        "O3",
        min_value=0.0,
        value=30.0
    )

    benzene = st.number_input(
        "Benzene",
        min_value=0.0,
        value=1.0
    )

    toluene = st.number_input(
        "Toluene",
        min_value=0.0,
        value=5.0
    )

    year = st.number_input(
        "Year",
        min_value=2015,
        max_value=2020,
        value=2019,
        step=1
    )

    month = st.number_input(
        "Month",
        min_value=1,
        max_value=12,
        value=1,
        step=1
    )

    day = st.number_input(
        "Day",
        min_value=1,
        max_value=31,
        value=1,
        step=1
    )

    # Prediction
    if st.button("🎯 Predict AQI"):

        input_data = pd.DataFrame([{
            "City": city,
            "PM2.5": pm25,
            "PM10": pm10,
            "NO": no,
            "NO2": no2,
            "NOx": nox,
            "NH3": nh3,
            "CO": co,
            "SO2": so2,
            "O3": o3,
            "Benzene": benzene,
            "Toluene": toluene,
            "Year": year,
            "Month": month,
            "Day": day
        }])

        prediction = model.predict(input_data)[0]

        st.success(
            f"Predicted AQI: {prediction:.2f}"
        )

        if prediction <= 50:
            category = "Good"
        elif prediction <= 100:
            category = "Satisfactory"
        elif prediction <= 200:
            category = "Moderate"
        elif prediction <= 300:
            category = "Poor"
        elif prediction <= 400:
            category = "Very Poor"
        else:
            category = "Severe"

        st.info(
            f"AQI Category: {category}"
        )

# ==================================================
# AIR QUALITY ANALYSIS
# ==================================================

elif page == "Air Quality Analysis":

    st.title("📊 Air Quality Analysis")

    st.write(
        "This section provides an overview of the air quality dataset."
    )

    data = pd.read_csv("data/city_day.csv")

    st.subheader("Dataset Overview")

    col1, col2 = st.columns(2)

    with col1:
        st.metric(
            "Total Records",
            len(data)
        )

    with col2:
        st.metric(
            "Total Columns",
            len(data.columns)
        )

    st.subheader("Dataset Preview")

    st.dataframe(
        data.head(10),
        use_container_width=True
    )

# ==================================================
# VISUALIZATIONS
# ==================================================

elif page == "Visualizations":

    st.title("📈 Air Quality Visualizations")

    st.write(
        "This page displays visualizations related to air quality."
    )

    st.info(
        "Visualizations will be added here using the existing project plots."
    )

# ==================================================
# ABOUT
# ==================================================

elif page == "About":

    st.title("ℹ️ About the Project")

    st.subheader(
        "Air Quality Prediction and Analysis Using Machine Learning"
    )

    st.write(
        """
        This project focuses on predicting the Air Quality Index (AQI)
        using Machine Learning techniques.

        Three Machine Learning models were compared:

        • Linear Regression
        • Random Forest Regressor
        • Gradient Boosting Regressor

        Random Forest Regressor achieved the best performance
        among the tested models.
        """
    )

    st.subheader("🎓 Project Information")

    st.write("B.Tech 2nd Year – CSE (Data Science)")

    st.write("Dataset: Air Quality Data in India")
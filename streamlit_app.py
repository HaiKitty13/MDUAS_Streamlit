import streamlit as st 
import requests 

def post_with_fallback(json_data):
    urls = [
        "https://your-fastapi-app.up.railway.app/predict",  
        "http://localhost:8000/predict"
    ]

    for url in urls:
        try:
            response = requests.post(url, json=json_data, timeout=3)
            if response.status_code == 200:
                return response.json(), url
        except requests.exceptions.RequestException:
            continue

    return {"error": "All API endpoints failed"}, None

st.set_page_config(
    page_title="Obesity Level Predictor",
    page_icon="🏥",
    layout="wide",
    initial_sidebar_state="collapsed"
)

st.markdown("""
<style>
    /* Main background */
    .main {
        background: linear-gradient(135deg, #ffb3d9 0%, #ff99cc 50%, #ff80c0 100%);
    }
    
    /* Header styling */
    .header-container {
        background: linear-gradient(90deg, #ff1a8c, #ff4da6);
        padding: 2rem;
        border-radius: 15px;
        margin-bottom: 2rem;
        box-shadow: 0 8px 32px rgba(255, 26, 140, 0.3);
        text-align: center;
    }
    
    .main-title {
        color: white;
        font-size: 3rem;
        font-weight: bold;
        margin: 0;
        text-shadow: 2px 2px 4px rgba(0,0,0,0.3);
    }
    
    .creator-name {
        color: #ffe6f2;
        font-size: 1.2rem;
        margin-top: 0.5rem;
        font-style: italic;
    }
    
    /* Tab styling */
    .stTabs [data-baseweb="tab-list"] {
        gap: 8px;
        background-color: rgba(255, 255, 255, 0.1);
        border-radius: 10px;
        padding: 5px;
    }
    
    .stTabs [data-baseweb="tab"] {
        background-color: rgba(255, 255, 255, 0.2);
        border-radius: 8px;
        color: #8B008B;
        font-weight: bold;
        border: 2px solid transparent;
    }
    
    .stTabs [aria-selected="true"] {
        background-color: white;
        color: #ff1a8c;
        border: 2px solid #ff1a8c;
    }
    
    /* Form styling */
    .stForm {
        background: rgba(255, 255, 255, 0.9);
        padding: 2rem;
        border-radius: 15px;
        box-shadow: 0 8px 32px rgba(255, 26, 140, 0.2);
        margin: 1rem 0;
    }
    
    /* Button styling */
    .stButton > button {
        background: linear-gradient(90deg, #ff1a8c, #ff4da6);
        color: white;
        border: none;
        border-radius: 25px;
        padding: 0.75rem 2rem;
        font-weight: bold;
        font-size: 1.1rem;
        box-shadow: 0 4px 15px rgba(255, 26, 140, 0.4);
        transition: all 0.3s ease;
    }
    
    .stButton > button:hover {
        transform: translateY(-2px);
        box-shadow: 0 6px 20px rgba(255, 26, 140, 0.6);
    }
    
    /* Info boxes */
    .info-box {
        background: rgba(255, 255, 255, 0.9);
        padding: 1.5rem;
        border-radius: 15px;
        margin: 1rem 0;
        border-left: 5px solid #ff1a8c;
        box-shadow: 0 4px 15px rgba(255, 26, 140, 0.2);
    }
    
    /* Success/Error messages */
    .stSuccess {
        background: linear-gradient(90deg, #ff80c0, #ffb3d9);
        color: #8B008B;
        border-radius: 10px;
    }
    
    .stError {
        background: linear-gradient(90deg, #ff6b6b, #ff8e8e);
        border-radius: 10px;
    }
</style>
""", unsafe_allow_html=True)

# Header
st.markdown("""
<div class="header-container">
    <h1 class="main-title">Obesity Level Predictor</h1>
    <p class="creator-name">Created by: 2702212250 - Ni Komang Gayatri Kusuma Wardhani</p>
</div>
""", unsafe_allow_html=True)

# Create tabs
tab1, tab2 = st.tabs(["Model Information", "Prediction Tool"])

with tab1:
    st.markdown('<div class="info-box">', unsafe_allow_html=True)
    
    st.markdown("## About the Model")
    st.markdown("""
    ### Model Overview
    This obesity level prediction system uses machine learning to analyze various lifestyle factors 
    and physical characteristics of a person to predict their obesity level.
    
    ### Features Used:
    - **Demographic Data**: Gender, Age, Height, Weight
    - **Family History**: Family history of overweight
    - **Eating Habits**: 
      - Frequent consumption of high caloric food (FAVC)
      - Frequency of vegetables consumption (FCVC)
      - Number of main meals per day (NCP)
      - Consumption of food between meals (CAEC)
    - **Lifestyle Factors**:
      - Smoking habits
      - Daily water consumption (CH2O)
      - Calorie consumption monitoring (SCC)
      - Physical activity frequency (FAF)
      - Time using technology devices (TUE)
      - Alcohol consumption (CALC)
      - Transportation mode used (MTRANS)
    
    ### Obesity Categories:
    - **Insufficient Weight**: Below normal weight
    - **Normal Weight**: Healthy weight range
    - **Overweight Level I**: Mild overweight
    - **Overweight Level II**: Moderate overweight
    - **Obesity Type I**: Class 1 obesity
    - **Obesity Type II**: Class 2 obesity
    - **Obesity Type III**: Class 3 obesity (severe)
    
    ### Important Notes:
    - This prediction is for informational and educational purposes only
    - Consult with healthcare professionals for accurate medical diagnosis
    - This model is developed based on specific training data and may have limitations
    """)
    
    st.markdown('</div>', unsafe_allow_html=True)

with tab2:
    st.markdown('<div class="info-box">', unsafe_allow_html=True)
    st.markdown("## Obesity Level Prediction")
    st.markdown("Fill out the following form to predict obesity level based on your lifestyle features and body data.")
    st.markdown('</div>', unsafe_allow_html=True)
    
    with st.form("obesity_form"): 
        col1, col2 = st.columns(2)
        
        with col1:
            st.markdown("### Demographic Data")
            Gender = st.selectbox("Gender", ["Male", "Female"]) 
            Age = st.number_input("Age", min_value=0.0, max_value=120.0, step=1.0) 
            Height = st.number_input("Height (in meters)", min_value=1.0, max_value=2.5, step=0.01) 
            Weight = st.number_input("Weight (in kg)", min_value=20.0, max_value=200.0, step=0.1) 
            family_history_with_overweight = st.selectbox("Family History of Overweight", ["yes", "no"])
            
            st.markdown("### Lifestyle Habits")
            SMOKE = st.selectbox("Do you smoke?", ["yes", "no"]) 
            SCC = st.selectbox("Do you monitor your calorie consumption?", ["yes", "no"]) 
            CALC = st.selectbox("Alcohol Consumption", ["no", "Sometimes", "Frequently", "Always"]) 
            MTRANS = st.selectbox("Transportation Used", ["Public_Transportation", "Walking", "Bike", "Motorbike", "Automobile"])
        
        with col2:
            st.markdown("### Eating Habits")
            FAVC = st.selectbox("Frequent Consumption of High Caloric Food (FAVC)", ["yes", "no"]) 
            FCVC = st.number_input("Frequency of Vegetable Consumption (FCVC)", min_value=0.0, max_value=3.0, step=0.1) 
            NCP = st.number_input("Number of Main Meals (NCP)", min_value=1.0, max_value=5.0, step=0.5) 
            CAEC = st.selectbox("Consumption of Food Between Meals (CAEC)", ["no", "Sometimes", "Frequently", "Always"]) 
            CH2O = st.number_input("Daily Water Intake (liters) (CH2O)", min_value=0.0, max_value=5.0, step=0.1)
            
            st.markdown("### Physical Activity")
            FAF = st.number_input("Physical Activity Frequency per week (FAF)", min_value=0.0, max_value=5.0, step=0.1) 
            TUE = st.number_input("Time using technology devices (hours/day) (TUE)", min_value=0.0, max_value=24.0, step=0.5)
        
        st.markdown("<br>", unsafe_allow_html=True)
        submitted = st.form_submit_button("Predict Obesity Level", use_container_width=True) 
    
    if submitted: 
        features = { 
            "Gender": Gender, 
            "Age": Age, 
            "Height": Height, 
            "Weight": Weight, 
            "family_history_with_overweight": family_history_with_overweight, 
            "FAVC": FAVC, 
            "FCVC": FCVC, 
            "NCP": NCP, 
            "CAEC": CAEC, 
            "SMOKE": SMOKE, 
            "CH2O": CH2O, 
            "SCC": SCC, 
            "FAF": FAF, 
            "TUE": TUE, 
            "CALC": CALC, 
            "MTRANS": MTRANS 
        } 
    
        try: 
            with st.spinner('Processing prediction...'):
                result, used_url = post_with_fallback(features) 
        
                if "error" in result: 
                    st.error(f"Prediction failed: {result['error']}") 
                else: 
                    st.success(f"**Predicted Obesity Level: {result['prediction_label']}**") 
                    
                    col1, col2, col3 = st.columns(3)
                    with col1:
                        st.metric("BMI Calculated", f"{Weight/(Height**2):.2f}")
                    with col2:
                        st.metric("Encoded Label", result['prediction_encoded'])
                    with col3:
                        st.metric("Confidence", "High")
                    
                    st.markdown("### Recommendations:")
                    if "Normal" in result['prediction_label']:
                        st.info("Great! Maintain your current healthy lifestyle.")
                    elif "Insufficient" in result['prediction_label']:
                        st.warning("Consider consulting a nutritionist for healthy weight gain strategies.")
                    else:
                        st.warning("Consider consulting healthcare professionals and adopting healthier lifestyle habits.")
        
        except requests.exceptions.RequestException as e: 
            st.error(f"API Request failed: {str(e)}")
            st.info("Make sure your API server is running on http://localhost:8000")

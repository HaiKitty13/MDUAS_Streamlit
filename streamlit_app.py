import streamlit as st 
import requests 

def post_with_fallback(json_data):
    urls = [
        "https://mduasapi-production.up.railway.app/predict",  
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
    page_icon="🌸",
    layout="wide",
    initial_sidebar_state="collapsed"
)

st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&display=swap');
    
    /* Global font */
    html, body, [class*="css"] {
        font-family: 'Inter', sans-serif;
    }
    
    /* Main background with subtle gradient */
    .main {
        background: linear-gradient(135deg, #fef7f7 0%, #fdf2f8 25%, #fce7f3 50%, #fbcfe8 75%, #f9a8d4 100%);
        min-height: 100vh;
    }
    
    /* Remove default padding */
    .block-container {
        padding-top: 2rem;
        padding-bottom: 2rem;
    }
    
    /* Header styling with elegant soft pink */
    .header-container {
        background: linear-gradient(135deg, #ec4899 0%, #f472b6 50%, #f9a8d4 100%);
        padding: 3rem 2rem;
        border-radius: 25px;
        margin-bottom: 3rem;
        box-shadow: 0 20px 40px rgba(236, 72, 153, 0.15);
        text-align: center;
        backdrop-filter: blur(10px);
        border: 1px solid rgba(255, 255, 255, 0.2);
    }
    
    .main-title {
        color: white;
        font-size: 3.5rem;
        font-weight: 700;
        margin: 0;
        text-shadow: 0 4px 8px rgba(0,0,0,0.1);
        letter-spacing: -0.02em;
    }
    
    .creator-name {
        color: #fdf2f8;
        font-size: 1.1rem;
        margin-top: 1rem;
        font-weight: 400;
        opacity: 0.9;
    }
    
    /* Tab styling with soft pink theme */
    .stTabs [data-baseweb="tab-list"] {
        gap: 12px;
        background: linear-gradient(135deg, rgba(255, 255, 255, 0.8), rgba(253, 242, 248, 0.8));
        border-radius: 20px;
        padding: 8px;
        margin-bottom: 2rem;
        backdrop-filter: blur(10px);
        border: 1px solid rgba(236, 72, 153, 0.1);
    }
    
    .stTabs [data-baseweb="tab"] {
        background: transparent;
        border-radius: 15px;
        color: #be185d;
        font-weight: 500;
        border: 2px solid transparent;
        padding: 12px 24px;
        transition: all 0.3s ease;
    }
    
    .stTabs [aria-selected="true"] {
        background: linear-gradient(135deg, #f9a8d4, #fbbf24);
        color: white;
        border: 2px solid rgba(255, 255, 255, 0.3);
        box-shadow: 0 8px 25px rgba(236, 72, 153, 0.2);
        transform: translateY(-2px);
    }
    
    /* Form styling with glass morphism effect */
    .stForm {
        background: linear-gradient(135deg, rgba(255, 255, 255, 0.9), rgba(253, 242, 248, 0.8));
        padding: 2.5rem;
        border-radius: 25px;
        box-shadow: 0 25px 50px rgba(236, 72, 153, 0.1);
        margin: 2rem 0;
        backdrop-filter: blur(20px);
        border: 1px solid rgba(255, 255, 255, 0.3);
    }
    
    /* Input field styling */
    .stSelectbox > div > div {
        background: rgba(255, 255, 255, 0.8);
        border: 2px solid rgba(236, 72, 153, 0.1);
        border-radius: 12px;
        transition: all 0.3s ease;
    }
    
    .stSelectbox > div > div:hover {
        border-color: rgba(236, 72, 153, 0.3);
        box-shadow: 0 4px 15px rgba(236, 72, 153, 0.1);
    }
    
    .stNumberInput > div > div > input {
        background: rgba(255, 255, 255, 0.8);
        border: 2px solid rgba(236, 72, 153, 0.1);
        border-radius: 12px;
        transition: all 0.3s ease;
    }
    
    .stNumberInput > div > div > input:focus {
        border-color: #ec4899;
        box-shadow: 0 0 0 3px rgba(236, 72, 153, 0.1);
    }
    
    /* Button styling with elegant gradient */
    .stButton > button {
        background: linear-gradient(135deg, #ec4899 0%, #f472b6 50%, #f9a8d4 100%);
        color: white;
        border: none;
        border-radius: 20px;
        padding: 1rem 3rem;
        font-weight: 600;
        font-size: 1.1rem;
        box-shadow: 0 10px 30px rgba(236, 72, 153, 0.3);
        transition: all 0.3s ease;
        border: 1px solid rgba(255, 255, 255, 0.2);
    }
    
    .stButton > button:hover {
        transform: translateY(-3px);
        box-shadow: 0 15px 40px rgba(236, 72, 153, 0.4);
        background: linear-gradient(135deg, #db2777 0%, #ec4899 50%, #f472b6 100%);
    }
    
    /* Info boxes with soft pink elegance */
    .info-box {
        background: linear-gradient(135deg, rgba(255, 255, 255, 0.9), rgba(253, 242, 248, 0.8));
        padding: 2.5rem;
        border-radius: 25px;
        margin: 2rem 0;
        border-left: 6px solid #f9a8d4;
        box-shadow: 0 20px 40px rgba(236, 72, 153, 0.1);
        backdrop-filter: blur(20px);
        border: 1px solid rgba(255, 255, 255, 0.3);
    }
    
    /* Section headers */
    .stMarkdown h3 {
        color: #be185d;
        font-weight: 600;
        margin-bottom: 1.5rem;
        font-size: 1.3rem;
        border-bottom: 2px solid #fce7f3;
        padding-bottom: 0.5rem;
    }
    
    .stMarkdown h2 {
        color: #be185d;
        font-weight: 700;
        margin-bottom: 1.5rem;
        font-size: 1.8rem;
    }
    
    /* Success/Error messages with soft styling */
    .stSuccess {
        background: linear-gradient(135deg, #dcfce7, #bbf7d0);
        color: #166534;
        border-radius: 15px;
        border: 1px solid #86efac;
        box-shadow: 0 8px 25px rgba(34, 197, 94, 0.1);
    }
    
    .stError {
        background: linear-gradient(135deg, #fef2f2, #fecaca);
        color: #dc2626;
        border-radius: 15px;
        border: 1px solid #fca5a5;
        box-shadow: 0 8px 25px rgba(239, 68, 68, 0.1);
    }
    
    .stWarning {
        background: linear-gradient(135deg, #fffbeb, #fed7aa);
        color: #d97706;
        border-radius: 15px;
        border: 1px solid #fdba74;
        box-shadow: 0 8px 25px rgba(245, 158, 11, 0.1);
    }
    
    .stInfo {
        background: linear-gradient(135deg, #f0f9ff, #dbeafe);
        color: #1e40af;
        border-radius: 15px;
        border: 1px solid #93c5fd;
        box-shadow: 0 8px 25px rgba(59, 130, 246, 0.1);
    }
    
    /* Metrics styling */
    .stMetric {
        background: linear-gradient(135deg, rgba(255, 255, 255, 0.8), rgba(253, 242, 248, 0.6));
        padding: 1.5rem;
        border-radius: 20px;
        border: 1px solid rgba(236, 72, 153, 0.1);
        box-shadow: 0 10px 25px rgba(236, 72, 153, 0.05);
        backdrop-filter: blur(10px);
    }
    
    /* Spinner customization */
    .stSpinner > div {
        border-top-color: #ec4899 !important;
    }
    
    /* Form submit button container */
    .stForm > div:last-child {
        display: flex;
        justify-content: center;
        margin-top: 2rem;
    }
    
    /* Smooth animations */
    * {
        transition: all 0.3s ease;
    }
    
    /* Hide Streamlit menu and footer */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    
    /* Custom scrollbar */
    ::-webkit-scrollbar {
        width: 8px;
    }
    
    ::-webkit-scrollbar-track {
        background: #fdf2f8;
    }
    
    ::-webkit-scrollbar-thumb {
        background: linear-gradient(135deg, #f9a8d4, #ec4899);
        border-radius: 4px;
    }
    
    ::-webkit-scrollbar-thumb:hover {
        background: linear-gradient(135deg, #ec4899, #db2777);
    }
</style>
""", unsafe_allow_html=True)

# Header with elegant design
st.markdown("""
<div class="header-container">
    <h1 class="main-title">🌸 Obesity Level Predictor</h1>
    <p class="creator-name">Created by: 2702212250 - Ni Komang Gayatri Kusuma Wardhani</p>
</div>
""", unsafe_allow_html=True)

# Create tabs
tab1, tab2 = st.tabs(["📊 Model Information", "🔮 Prediction Tool"])

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
    st.markdown("## 🌸 Obesity Level Prediction")
    st.markdown("Fill out the following form to predict obesity level based on your lifestyle features and body data.")
    st.markdown('</div>', unsafe_allow_html=True)
    
    with st.form("obesity_form"): 
        col1, col2 = st.columns(2)
        
        with col1:
            st.markdown("### 👤 Demographic Data")
            Gender = st.selectbox("Gender", ["Male", "Female"]) 
            Age = st.number_input("Age", min_value=0.0, max_value=120.0, step=1.0) 
            Height = st.number_input("Height (in meters)", min_value=1.0, max_value=2.5, step=0.01) 
            Weight = st.number_input("Weight (in kg)", min_value=20.0, max_value=200.0, step=0.1) 
            family_history_with_overweight = st.selectbox("Family History of Overweight", ["yes", "no"])
            
            st.markdown("### 🚬 Lifestyle Habits")
            SMOKE = st.selectbox("Do you smoke?", ["yes", "no"]) 
            SCC = st.selectbox("Do you monitor your calorie consumption?", ["yes", "no"]) 
            CALC = st.selectbox("Alcohol Consumption", ["no", "Sometimes", "Frequently", "Always"]) 
            MTRANS = st.selectbox("Transportation Used", ["Public_Transportation", "Walking", "Bike", "Motorbike", "Automobile"])
        
        with col2:
            st.markdown("### 🍽️ Eating Habits")
            FAVC = st.selectbox("Frequent Consumption of High Caloric Food (FAVC)", ["yes", "no"]) 
            FCVC = st.number_input("Frequency of Vegetable Consumption (FCVC)", min_value=0.0, max_value=3.0, step=0.1) 
            NCP = st.number_input("Number of Main Meals (NCP)", min_value=1.0, max_value=5.0, step=0.5) 
            CAEC = st.selectbox("Consumption of Food Between Meals (CAEC)", ["no", "Sometimes", "Frequently", "Always"]) 
            CH2O = st.number_input("Daily Water Intake (liters) (CH2O)", min_value=0.0, max_value=5.0, step=0.1)
            
            st.markdown("### 🏃‍♀️ Physical Activity")
            FAF = st.number_input("Physical Activity Frequency per week (FAF)", min_value=0.0, max_value=5.0, step=0.1) 
            TUE = st.number_input("Time using technology devices (hours/day) (TUE)", min_value=0.0, max_value=24.0, step=0.5)
        
        st.markdown("<br>", unsafe_allow_html=True)
        submitted = st.form_submit_button("🌸 Predict Obesity Level", use_container_width=True) 
    
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
            with st.spinner('✨ Processing prediction...'):
                result, used_url = post_with_fallback(features) 
        
                if "error" in result: 
                    st.error(f"🚫 Prediction failed: {result['error']}") 
                else: 
                    st.success(f"**🎯 Predicted Obesity Level: {result['prediction_label']}**") 
                    
                    col1, col2, col3 = st.columns(3)
                    with col1:
                        st.metric("📊 BMI Calculated", f"{Weight/(Height**2):.2f}")
                    with col2:
                        st.metric("🏷️ Encoded Label", result['prediction_encoded'])
                    with col3:
                        st.metric("🎯 Confidence", "High")
                    
                    st.markdown("### 💡 Recommendations:")
                    if "Normal" in result['prediction_label']:
                        st.info("🌟 Great! Maintain your current healthy lifestyle.")
                    elif "Insufficient" in result['prediction_label']:
                        st.warning("⚖️ Consider consulting a nutritionist for healthy weight gain strategies.")
                    else:
                        st.warning("🏥 Consider consulting healthcare professionals and adopting healthier lifestyle habits.")
        
        except requests.exceptions.RequestException as e: 
            st.error(f"🚫 API Request failed: {str(e)}")
            st.info("💡 Make sure your API server is running on http://localhost:8000")
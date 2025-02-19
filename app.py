import os
import streamlit as st
import pickle
from streamlit_option_menu import option_menu

st.set_page_config(page_title="Prediction of Disease Outbreak",
                   layout="wide",
                   page_icon="👨‍⚕️")
working_dir=os.path.dirname(os.path.abspath(__file__))
diabetes_model=pickle.load(open("/Users/aakashtiru/Desktop/AICTE Internship (Jan-Feb) 2025/models/diabetes_model.sav","rb"))
heart_model=pic=pickle.load(open("/Users/aakashtiru/Desktop/AICTE Internship (Jan-Feb) 2025/models/heart_model.sav","rb"))
parkinsons_model=pickle.load(open("/Users/aakashtiru/Desktop/AICTE Internship (Jan-Feb) 2025/models/parkinsons_model.sav","rb"))

with st.sidebar:
    selected=option_menu("Prediction of Disease Outbreak",
                         ['Diabetes Prediction',
                          'Heart disease Prediction',
                          'Parkinsons Prediction'],
                          menu_icon='hospital-fill',
                          icons=['activity','heart','person'],
                          default_index=0)
if selected == 'Diabetes Prediction':
    st.title('Diabetes Prediction using ML')
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        Pregnancies = st.text_input('Number of Pregnancies', value="0")
    with col2:
        Glucose = st.text_input('Glucose', value="0")
    with col3:
        BloodPressure = st.text_input('Blood Pressure', value="0")
    with col1:
        SkinThickness = st.text_input('Skin Thickness', value="0")
    with col2:
        Insulin = st.text_input('Insulin', value="0")
    with col3:
        BMI = st.text_input('BMI', value="0")
    with col1:
        DiabetesPedigreeFunction = st.text_input('Diabetes Pedigree Function', value="0")
    with col2:
        Age = st.text_input('Age', value="0")

    diab_diagnosis = ''

    # Prediction button
    if st.button('Diabetes Test Result'):
        try:
            # Convert user input values to float
            user_input = [
                float(Pregnancies), float(Glucose), float(BloodPressure),
                float(SkinThickness), float(Insulin), float(BMI),
                float(DiabetesPedigreeFunction), float(Age)
            ]

            # Make prediction
            diab_prediction = diabetes_model.predict([user_input])

            # Display result
            if diab_prediction[0] == 1:
                diab_diagnosis = 'The Person is Diabetic'
            else:
                diab_diagnosis = 'The Person is not Diabetic'

        except ValueError:
            st.error("Please enter valid numerical values in all fields.")

    st.success(diab_diagnosis)

if selected == 'Heart disease Prediction':
    st.title('Heart Disease Prediction using ML')
    col1,col2,col3=st.columns(3)
    with col1:
        Age=st.text_input('Age')
    with col2:
        sex=st.text_input('Sex')
    with col3:
        cp=st.text_input('Chest Pain Types')
    with col1:
        trestbps=st.text_input('Resting Blood Pressure')
    with col2:
        chol=st.text_input('Serum Cholestoral in mg/dl')
    with col3:
        fbs=st.text_input('Fasting Blood Sugar > 120 mg/dl')
    with col1:
        restecg=st.text_input('Resting ElectroCardioGraphic Results')
    with col2:
        thalach=st.text_input('Max Heart Rate Achieved')
    with col3:
        exang=st.text_input('Exercise Induced Angena')
    with col1:
        oldpeak=st.text_input('ST depression indiced by excercise')
    with col2:
        slope=st.text_input('Slope of peak excercise ST segment')
    with col3:
        ca=st.text_input('Major vessels colored by fluoroscopy')
    with col1:
        thal=st.text_input('thal:0=normal;1=fixed defect;2=reversable defect')

    heart_diagnosis=''
    if st.button('Heart Test Result'):
        try:
            user_input = [
                float(Age), float(sex), float(cp), float(trestbps), float(chol),
                float(fbs), float(restecg), float(thalach), float(exang), float(oldpeak),
                float(slope), float(ca), float(thal)
            ]
            heart_prediction = heart_model.predict([user_input])
            if heart_prediction[0] == 1:
                heart_diagnosis = 'The Person is having Heart Disease'
            else:
                heart_diagnosis = 'The Person is not having Heart Disease'   
        except ValueError:
            st.error("Please enter valid numerical values.")

    st.success(heart_diagnosis)




if selected == 'Parkinsons Prediction':
    st.title('Parkinsons Prediction using ML')

    # Input fields
    col1, col2, col3 = st.columns(3)

    def get_float_input(label):
        """Safely gets a float input from user, handling empty or invalid values."""
        value = st.text_input(label).strip()
        try:
            return float(value) if value else 0.0  # Convert to float, default 0.0
        except ValueError:
            st.error(f"Invalid input for {label}. Please enter a numerical value.")
            return None  # Return None if invalid

    with col1:
        MDVP_Fo = get_float_input('MDVP:Fo(Hz)')
        MDVP_Jitter = get_float_input('MDVP:Jitter(%)')
        Jitter_DDP = get_float_input('Jitter:DDP')
        Shimmer_APQ3 = get_float_input('Shimmer:APQ3')
        NHR = get_float_input('NHR')
        RPDE = get_float_input('RPDE')
        spread1 = get_float_input('spread1')
        missing_feature_1 = get_float_input('Missing Feature 1')  # Added

    with col2:
        MDVP_Fhi = get_float_input('MDVP:Fhi(Hz)')
        MDVP_Jitter_Abs = get_float_input('MDVP:Jitter(Abs)')
        MDVP_Shimmer = get_float_input('MDVP:Shimmer')
        Shimmer_APQ5 = get_float_input('Shimmer:APQ5')
        HNR = get_float_input('HNR')
        DFA = get_float_input('DFA')
        spread2 = get_float_input('spread2')
        missing_feature_2 = get_float_input('Missing Feature 2')  # Added

    with col3:
        MDVP_Flo = get_float_input('MDVP:Flo(Hz)')
        MDVP_RAP = get_float_input('MDVP:RAP')
        MDVP_Shimmer_dB = get_float_input('MDVP:Shimmer(dB)')
        MDVP_APQ = get_float_input('MDVP:APQ')
        Shimmer_DDA = get_float_input('Shimmer:DDA')
        D2 = get_float_input('D2')
        PPE = get_float_input('PPE')

    parkinsons_diagnosis = ''

    if st.button('Parkinsons Test Result'):
        # Check if any value is None (i.e., invalid input detected)
        if None in [MDVP_Fo, MDVP_Fhi, MDVP_Flo, MDVP_Jitter, MDVP_Jitter_Abs, MDVP_RAP, Jitter_DDP,
                    MDVP_Shimmer, MDVP_Shimmer_dB, Shimmer_APQ3, Shimmer_APQ5, MDVP_APQ, Shimmer_DDA,
                    NHR, HNR, RPDE, DFA, spread1, spread2, D2, PPE, missing_feature_1, missing_feature_2]:
            st.error("Please fix all invalid inputs before proceeding.")
        else:
            # Make prediction
            user_input = [
                MDVP_Fo, MDVP_Fhi, MDVP_Flo, MDVP_Jitter, MDVP_Jitter_Abs,
                MDVP_RAP, Jitter_DDP, MDVP_Shimmer, MDVP_Shimmer_dB,
                Shimmer_APQ3, Shimmer_APQ5, MDVP_APQ, Shimmer_DDA,
                NHR, HNR, RPDE, DFA, spread1, spread2, D2, PPE,
                missing_feature_1, missing_feature_2
            ]

            parkinsons_prediction = parkinsons_model.predict([user_input])

            # Display result
            if parkinsons_prediction[0] == 1:
                parkinsons_diagnosis = 'The Person is likely to have Parkinsons Disease'
            else:
                parkinsons_diagnosis = 'The Person is unlikely to have Parkinsons Disease'
            
            st.success(parkinsons_diagnosis)

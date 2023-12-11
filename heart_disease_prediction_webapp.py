import numpy as np
import pickle
import streamlit as st

trained_model = pickle.load(open(r"C:\Users\91903\Desktop\machine_learning\trained_model.sav",'rb'))

def prediction(input):
    input_np_array = np.asarray(input,dtype=float)
    input_np_array_reshaped = input_np_array.reshape(1,-1)
    prediction = trained_model.predict(input_np_array_reshaped)
    print(prediction)
    
    if prediction[0] == 0:
        return "The patient has a healthy heart"
    else:
        return "The patient has a heart disease"
    
def main():
    st.title('Heart Disease Prediction Web App ')
    age = st.text_input('Age')
    sex = st.text_input('Sex')
    cp = st.text_input('Chest pain type (4 values)')
    trestbps = st.text_input('Resting blood pressure')
    chol = st.text_input('Serum cholestoral in mg\dl')
    fbs = st.text_input('Fasting blood sugar > 120 mg\dl')
    restecg = st.text_input('Resting electrocardiographic results (values 0,1,2)')
    thalach = st.text_input('Maximum heart rate achieved')
    exang = st.text_input('Exercise induced angina')
    oldpeak = st.text_input('Oldpeak = ST depression induced by exercise relative to rest')
    slope = st.text_input('The slope of the peak exercise ST segment')
    ca = st.text_input('Number of major vessels (0-3) colored by flourosopy')
    thal = st.text_input('thal: 0 = normal; 1 = fixed defect; 2 = reversable defect')

    diagnosis = ''

    if st.button('Heart Test Result'):
        diagnosis = prediction([age,sex,cp,trestbps,chol,fbs,restecg,thalach,exang,oldpeak,slope,ca,thal])

    st.success(diagnosis)


if __name__=='__main__':
    main()


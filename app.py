import pandas as pd
import joblib as jb
import streamlit as st

st.set_page_config(
    page_title="Student performance prediction",
    page_icon="logo.png"
)
col1, col2 = st.columns([1, 3]) 
with col1:
    st.image("logo.png", width=200)
with col2:
    st.title("Students Performance Prediction Based On Their Habits")
student_performance_predictor_model=jb.load('students_performance_model.pkl')
with st.form('students_habits'):

    st.header('Enter your details to predict your performance!')

    age = st.slider('Age',1,30,17)
    gender=st.radio('Gender',['Male','Female','Other'])
    study_hours_per_day=st.number_input('Avegrave number of hours you study every day',0.0,15.0,5.4)
    social_media_hours=st.number_input('Average number of hours you spend on social media every day',0.0,15.0,2.5)
    netflix_hours=st.number_input('Average number of hours you spend on netflix every day',0.0,15.0,1.8)
    part_time_job=st.radio('Do you do part time job?',["No","Yes"])
    attendance_percentage=st.number_input('Percentage of your class attendance',30.0,100.0,84.1)
    sleep_hours=st.number_input('Average hours you sleep every day',5.0,18.0,6.4)
    diet_quality=st.radio('How is your diet quality?',["Fair","Good",'Poor'])
    exercise_frequency=st.number_input('Average number of time you exercise every week',0,10,3)
    internet_quality=st.radio('What is the quality of your internet?',['Good','Average','Poor'])
    mental_health_rating=st.number_input('What is the rating of your mental health?',0,10,5)
    extracurricular_participation=st.radio('Do you participate in extracurricular activities?',['Yes','No'])

    student_data=pd.DataFrame({
        "age":[age],
        'gender':[gender],
        'study_hours_per_day':[study_hours_per_day],
        'social_media_hours':[social_media_hours],
        'netflix_hours':[netflix_hours],
        'part_time_job':[part_time_job],
        'attendance_percentage':[attendance_percentage],
        'sleep_hours':[sleep_hours],
        'diet_quality':[diet_quality],
        'exercise_frequency':[exercise_frequency],
        'internet_quality':[internet_quality],
        'mental_health_rating':[mental_health_rating],
        "extracurricular_participation":[extracurricular_participation]
    })
    submitted=st.form_submit_button('Predict my score')

if submitted:
    score=student_performance_predictor_model.predict(student_data)
    if score>=100:
        score[0]=99.99
    st.success(f'Yous predicted score is {score[0]:.2f}%')
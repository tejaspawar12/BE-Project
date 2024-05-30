import streamlit as st
import tensorflow as tf
import requests
from dotenv import load_dotenv
load_dotenv() 

import streamlit as st
import os
import google.generativeai as genai
from joblib import load

base = "light" # Choose between 'light' or 'dark'
primaryColor = "#0099FF"
backgroundColor = "#F0F2F5"


st.title("CAREER ROADMAP SOLUTION USING MACHIN LEARNING AND WEB INTERFACE")
st.write("A personalized tool powered by Machine Learning")

Database_Fundamentals = st.selectbox("Select your level in Database fundamentals:", ["Begineer", "Poor", "Excellent", "Average", "Not interested", "Professional", "Intermediate"])
Computer_architecture = st.selectbox("Select your level in computer architecture:", ["Begineer", "Poor", "Excellent", "Average", "Not interested", "Professional", "Intermediate"])
Distributed_Computing_Systems = st.selectbox("Select your level in Distributed Computing Systems:", ["Begineer", "Poor", "Excellent", "Average", "Not interested", "Professional", "Intermediate"])
Cyber_Security = st.selectbox("Select your level in Cyber Security:", ["Begineer", "Poor", "Excellent", "Average", "Not interested", "Professional", "Intermediate"])

Networking = st.selectbox("Select your level in Networking:", ["Begineer", "Poor", "Excellent", "Average", "Not interested", "Professional", "Intermediate"])
Software_Development = st.selectbox("Select your level in Software Development:", ["Begineer", "Poor", "Excellent", "Average", "Not interested", "Professional", "Intermediate"])
Programming_Skills = st.selectbox("Select your level in Programming Skills:", ["Begineer", "Poor", "Excellent", "Average", "Not interested", "Professional", "Intermediate"])
DSA= st.selectbox("Select your level in Data Structure and algorithms:", ["Begineer", "Poor", "Excellent", "Average", "Not interested", "Professional", "Intermediate"])
OOP = st.selectbox("Select your level in Object Oriented Programming:", ["Begineer", "Poor", "Excellent", "Average", "Not interested", "Professional", "Intermediate"])

AI_ML = st.selectbox("Select your level in AI ML:", ["Begineer", "Poor", "Excellent", "Average", "Not interested", "Professional", "Intermediate"])
Data_Science= st.selectbox("Select your level in Data Science:", ["Begineer", "Poor", "Excellent", "Average", "Not interested", "Professional", "Intermediate"])
O_S = st.selectbox("Select your level in Operating System:", ["Begineer", "Poor", "Excellent", "Average", "Not interested", "Professional", "Intermediate"])
Programming_Language = st.selectbox("Select your prefered Programming Language:", ["C", "C++", "Python", "R", "Java", "Ruby"])
#Logic_Building = st.selectbox("Select your level in Logic Building:", ["C", "C++", "Python", "R", "Java", "Ruby"])
Logic_Building = st.selectbox("Select your level in Logic Building:", ["Begineer", "Poor", "Excellent", "Average", "Not interested", "Professional", "Intermediate"])
Mathematics = st.selectbox("Select your level in Mathematics :", ["Begineer", "Poor", "Excellent", "Average", "Not interested", "Professional", "Intermediate"])
 
Intrested_Subject = st.selectbox("Select your intrested subject:", ["Networks", "IOT", "Data Engineer", "Computer Architecture", "Hacking", "Programming", "Cloud Computing", "Software Engineering", "Management", "Parallel Computing", "Other"])
Other1 = st.text_input("mention your interested subject if you selected other otherwise type NA:")

ICA = st.selectbox("Select your intrested Career area:", ["testing", "System developer", "Cloud computing", "Security", "Web Developer", "Application developer", "Security", "Data Scientist", "AI ML Engineer", "Business Process Analyst", "Project Manager", "Product Manager", "OTHER"])
Other2 = st.text_input("mention your interested career area if you selected other OPTION otherwise type NA:")

TOCYWTSI = st.selectbox("Select type of comapny you want to settele in:", ["Service Based", "Product Based", "Cloud Service", "Web services", "Finance", "Testing and maintaince service", "Cloud Computing", "Product Development", "Business Process automtion", "AI ML based", "Sales and Marketing"])
 #Store inputs in a dictionary

user_data = {
       "Database_Fundamentals": Database_Fundamentals,
       "Computer_architecture": Computer_architecture,
       "Distributed_Computing_Systems": Distributed_Computing_Systems,
       "Cyber_Security": Cyber_Security,
       "Software_Development": Software_Development,
       "Programming_Skills": Programming_Skills,
       "DSA" : DSA,
       "OOP" : OOP,

       "AI_ML ": AI_ML,
       "Data_Science" : Data_Science,
       "Operating_System" : O_S,
       "Programming_Language" : Programming_Language,
       "Logic_Building" : Logic_Building ,
       "Mathematics" : Mathematics,
       "Intrested_Subject" : Intrested_Subject,
       "Other1" : Other1,
       "ICA" : ICA,
       "Other2" : Other2,
       "TOCYWTSI" : TOCYWTSI

}
submit=st.button("Provide me solution")
model = load("carrerlast2.pkl")
prediction = model.predict(user_data)



if submit:
    model = load("carrerlast2.pkl")
    prediction = model.predict(user_data)

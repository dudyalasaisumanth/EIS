from msilib import sequence
import streamlit as st
import pandas as pd
import numpy as np
import random


st.header("BIAS in Artificial Intelligence")
st.write('Artificial intelligence is the ability of computers, programs, machines to learn and improve themselves overtime by using the data they are given and predict an output of something they haven’t seen before. There are many forms of AI. Bias as definition means prejudice in favor of or against a thing, a person or a group and bias in AI is the AI predicting an output with a bias, one of the recently popular bias in AI which is well spoken about in the news, technologists and data scientists is about how Apple card when lending credit had a bias towards men and would lend higher credit to men regardless of the credit score.When we think about it, a machine or a computer doesn’t have any prejudice, feelings about anything, there is no judgement of its own unless we, humans feed it with data or train it with data that inherently has bias in it.  The AI can learn on the basis of the data that it has access to in the same way humans learn from data or instances, cultures they are exposed to. Sometimes the data might not even be biased and the data could be a representation of factual data and AI is just behaving the way it is expected to be and the results look as we they are biased although it is not for instance it is a fact that certain genders have earnings less than that of the counterpart which could’ve been because of a higher number of people of one gender choose to take up jobs which are inherently paid higher or the society itself has such representation that when the AI predicts the output it appears to be biased when in it was just putting out facts.')

# age=st.text_input("Age")

st.subheader('Predict Credit Score based on below inputs', anchor=None)

st.write("This model illustrates BIAS in credit score rating")


age=st.slider('Age', 0, 100, 25)
Income=st.slider('Income', 0, 100000, 5000)

Education = st.selectbox(
     'Education',
     ('High School', 'Bachelors', 'Masters','Post-grad'))


Eth = st.selectbox(
     'Ethnicity',
     ('Caucasian', 'Hispanic','African American'))

Gender = st.selectbox(
     'Gender',
     ('Male', 'Female'))
Married = st.selectbox(
     'Married',
     ('Married', 'UnMarried'))
# Married = st.checkbox('Married')

if st.button('Submit'):

    if(Gender=="Male"):
        if(Income>80000):
            # st.write('male')
            st.write("For the given inputs model predicted credit score is ",random.randint(600, 900))
        elif(Income>60000):
            st.write("For the given inputs model predicted credit score is ",random.randint(600, 800))
        elif(Income>40000):
            st.write("For the given inputs model predicted credit score is ",random.randint(600, 750))
        else:
            st.write("For the given inputs model predicted credit score is ",random.randint(200, 700))


        # st.write("for the given inputs model predicted credit score is ",random.randint(100, 820))
    else:
        if(Income>80000):
            # st.write('male')
            st.write("For the given inputs model predicted credit score is ",random.randint(500, 800))
        elif(Income>60000):
            st.write("For the given inputs model predicted credit score is ",random.randint(500, 700))
        elif(Income>40000):
            st.write("For the given inputs model predicted credit score is ",random.randint(500, 650))
        else:
            st.write("For the given inputs model predicted credit score is ",random.randint(100, 550))

st.subheader("To check more about AI BIAS models, Please refer to the below links")

# st.markdown("[Google](www.google.com)"
import webbrowser

url1= 'https://www.reuters.com/article/us-amazon-com-jobs-automation-insight/amazon-scraps-secret-ai-recruiting-tool-that-showed-bias-against-women-idUSKCN1MK08G'
url2='https://mashable.com/archive/google-photos-black-people-gorillas#M.3Be4dBfuqB';
url3="https://www.nytimes.com/2019/11/10/business/Apple-credit-card-investigation.html";

if st.button('BIAS in Apple Credit card approval'):
    webbrowser.open_new_tab(url3)
# if st.button('Amazon Recruitment BIAS Model'):
#     webbrowser.open_new_tab(url1)
if st.button('Amazon Recruitment BIAS Model'):
    webbrowser.open_new_tab(url1)
if st.button('Google Image recognization BIAS'):
    webbrowser.open_new_tab(url2)

# if st.button('Amazon Recruitment BIAS Model'):
#     webbrowser.open_new_tab(url1)

st.subheader("Ways to Control BIAS in AI models")
st.write('We can handle the bias in AI systems in several stages, in the deployment stages and in the pre-built stages. During the deployment stage, the most strategic way to handle the bias is to use the “Blind Taste Tests” strategy.In order to reduce the bias in AI systems in the pre-build models, European Union has drafted a blueprint with seven fundamental principles of AI trustworthiness.')
    
        





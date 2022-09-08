

# importing necessary libraries
import joblib
import streamlit as st
import pandas as pd
import numpy as np
import sklearn

#load the model
classifier = joblib.load('cluster_CDA1.pkl')




#page configuration
st.set_page_config(page_title = 'Customer Segmentation Web App', layout='centered')
st.title('Customer Segmentation Web App')

# customer segmentation function
def segment_customers(input_data):
    
    prediction=classifier.predict(pd.DataFrame(input_data, columns=['Income','Age','Month_Customer','TotalSpendings','Children']))
    print(prediction)
    #pred_1 = 0
    if prediction == 1:
            pred_1 = 'Highly Active Customer'

    elif prediction == 2:
            pred_1 = 'Moderately Active Customer'

    elif prediction == 3:
            pred_1 = 'Least Active Customer'
    

    return pred_1

def main():
    
    Income = st.text_input("Type In The Household Income")
    Children = st.radio ( "Select Number Of children", ('0', '1','2','3') )
    TotalSpendings = st.text_input("Type TotalSpendings ")
    Age = st.slider ( "Select Age", 18, 85 )
    Month_Customer = st.text_input("type Month_Customer")
 
    
    result = ""

    # when 'Predict' is clicked, make the prediction and store it
    if st.button("Segment Customer"):
        result=segment_customers([[Income,Children,TotalSpendings,Age,Month_Customer]])
    
    st.success(result)
    

if __name__ == '__main__':
        main ()

#!/usr/bin/env python
# coding: utf-8

# In[20]:


# importing necessary libraries
import joblib
import pandas as pd
import streamlit as st



#load the model
KMeansCls = joblib.load('clust1_cba.pkl')

#page configuration
st.set_page_config(page_title = 'Customer Behaviour Analysis', layout='centered')
st.title('Customer Behaviour Analysis')

# customer segmentation function
def segment_customers(input_data):
    
    prediction=KMeansCls.predict(pd.DataFrame(input_data, columns=['Income', 'Age', 'Month_Customer', 'TotalSpendings', 'Children']))
    print(prediction)
    pred_1 = 0
    if prediction == 0:
            pred_1 = 'High'

    elif prediction == 1:
            pred_1 = 'Modarate'

    elif prediction == 2:
            pred_1 = 'Low'

    return pred_1
def main():
    st.image("""https://d2s30hray1l0uq.cloudfront.net/frontend/xWcdySUP-Untitled-design-8.jpg""")
    
    Income = st.text_input("Type In The Household Income")
    Children = st.radio ( "Select Number Of Kids In Household", ('0', '1','2','3') )
    Month_Customer = st.text_input( "Month")
    Age = st.slider ( "Select Age", 18, 85 )
    TotalSpendings= st.text_input( "TotalSpendings")
    
    
    result = ""

    # when 'Predict' is clicked, make the prediction and store it
    if st.button("Customer"):
        result=segment_customers([[Income,Age,Month_Customer,TotalSpendings,Children]])
    
    st.success(result)
if __name__ == '__main__':
        main ()



# In[ ]:





# In[15]:





# In[16]:





# In[ ]:





# In[ ]:





import streamlit as st    
import pandas as pd 
import numpy as np
import plotly.express as pe
import time


#we will load the csv data.
data=pd.read_csv("https://raw.githubusercontent.com/Lexie88rus/bank-marketing-analysis/master/bank.csv")


st.set_page_config(
    page_title="live dashboard",
    page_icon="📈",
    layout="wide"
)
st.title("Live Dashboard")
Filter =st.sidebar.selectbox("select the job", pd.unique(data['job']))
placeholder=st.empty()

data=data[data['job']==Filter]
for s in range(200):
    data['newage']=data['age']* np.random.choice(range(1,5))
    data['newbalance']=data['balance']*np.random.choice(range(1,5))

    avgage=np.mean(data['newage'])
    married_count = int(data[(data["marital"]=='married')]['marital'].count() + np.random.choice(range(1,30)))
    balance=np.mean(data['newbalance'])

    with placeholder.container():
        ind1,ind2,ind3=st.columns(3)

        ind1.metric(label="Age", value=round(avgage), delta= round(avgage) - 10)
        ind2.metric(label="Married Count", value= int(married_count), delta= - 10 + married_count)
        ind3.metric(label="A/C Balance", value= f"$ {round(balance,2)} ", delta= - round(balance/married_count) * 100)
    

        col1,col2=st.columns(2)
        with col1:
           st.markdown("Heat Map")
           heatmap = pe.density_heatmap(data_frame=data, y = 'newage', x = 'marital')
           st.write(heatmap)
        with col2:
           st.markdown("histogram")
           histogram = pe.histogram(data_frame = data, x = 'newage')
           st.write(histogram)
        st.markdown("Detailed Data View")
        st.dataframe(data)
        time.sleep(1)

import dashboard as ds
import pandas as pd
import streamlit as sl
df= pd.read_csv("cleaned_data.csv")
df.sort_values(df.columns[-14],axis=0,ascending=[False],inplace=True)
sl.title("Covid-19 Dashboard")
sl.write("This is a dashboard for covid-19 Data")

a=ds.Drop(df)


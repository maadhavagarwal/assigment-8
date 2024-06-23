import pandas as pd
import streamlit as sl
import exception as ex
try:
# import matplotlib.pyplot as plt
        df= pd.read_csv("country_wise_latest.csv")
        print(df)
        sl.title("Header")
        sl.write(df)
        sl.write(df.isna().sum())
        sl.write(df.duplicated().sum())
except ex.inp  as e:
        print(e)
        sl.write("Data is not loaded")

#saving file
def clean_data():
        try:
                df.to_csv("cleaned_data.csv",index=False)
                sl.write("Data is cleaned and saved as cleaned_data.csv")
        except Exception as e:
                print(e)
                sl.write("Data is not saved")
                

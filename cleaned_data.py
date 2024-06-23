import pandas as pd
import streamlit as sl
import data_cleaning as dc
# import matplotlib.pyplot as plt
dc.clean_data()
def load():
    try:
        df= pd.read_csv("cleaned_data.csv")
        print(df)
        sl.title("Cleaned File")
        sl.write(df)
    except Exception as e:
        print(e)
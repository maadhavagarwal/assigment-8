import matplotlib.pyplot as plt
import pandas as pd
import streamlit as sl
import numpy as np
# df = pd.read_csv('cleaned_data.csv')
def plot_total_cases(df):
    # plt.figure(900*100)
    plt.figure().set_figheight(40)
    sl.write("Total cases vs Country")
    sl.write("Confrim cases")
    plt.scatter(df['Confirmed'], df['Country/Region'])
    sl.pyplot(plt)
    plt.savefig("confim.png")
    sl.write("Death cases")
    
    plt.scatter(df['Deaths'], df['Country/Region'])
    sl.pyplot(plt)
    plt.savefig("death.png")
    sl.write("Recoverd cases")
    plt.scatter(df['Recovered'], df['Country/Region'])
    plt.savefig("recoverd.png")
    sl.pyplot(plt)
    # plt.savefig("")
def plot_daily_cases(df):
      plt.figure().set_figheight(35)
      plt.scatter(df['New cases'], df['Country/Region'])
      plt.savefig("daily_cases.png")
      sl.pyplot(plt)
# plot_daily_cases()
# plot_total_cases()
def plot_countries_with_max_cases(df):
    plt.figure().set_figwidth(10)
    plt.scatter( df['Country/Region'],df['Confirmed'])
    plt.savefig("countries_with_max_cases.png")
    sl.pyplot(plt)  

def plot_country(df,country):
    filtered_df = df[df["Country/Region"] == country]
    
    if filtered_df.empty:
        raise ValueError(f"No data found for country: {country}")
    
    # Create a scatter plot
    plt.scatter(filtered_df['Country/Region'], filtered_df[filtered_df.columns[4]])
    plt.title(f"Covid-19 Cases in {country}")
  
    plt.ylabel("Number of active Cases")
    
    # Display the plot in Streamlit
    sl.pyplot(plt)
    
    # Save the plot to a file
    plt.savefig(country + ".png")
    

    
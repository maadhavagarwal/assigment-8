import pandas as pd
import streamlit as sl
import visulation as vis
    
def Drop(df):
   a=sl.selectbox("choose one",df.columns,index=14)
  
   if a == "Country/Region":
      i=sl.selectbox("choose one",df["Country/Region"])
      vis.plot_country(df,i)
   if a == "Deaths" or a == "Confirmed" or a == "Recovered":
      vis.plot_total_cases(df)
   # sl.write(df)
   else:
       sl.bar_chart(df[a])
   
   sl.write("Top 10 countries with maximum cases")
   vis.plot_countries_with_max_cases(df.head(10))
   sl.write("Death range selection")
   a=sl.slider("choose death range",df["Deaths"].min(),df["Deaths"].max(),step=1000)
   sl.write("Death range selection",a)
   sl.bar_chart(df[df["Deaths"]>=a]["Country/Region"])
   sl.write("New cases")
   vis.plot_daily_cases(df)
   return a

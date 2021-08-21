import pandas as pd
import plotly.express as px

df=pd.read_csv(r"C:\Users\Chiranjeev\OneDrive\Desktop\covidGraph\Copy+of+data+-+data.csv")

fig=px.scatter(df,x="date",y="cases",color="country")

fig.show()
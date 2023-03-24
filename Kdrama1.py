#!/usr/bin/env python
# coding: utf-8

# In[2]:


import pandas as pd
import dash
from dash import dcc
from dash import html
import plotly.express as px


# In[3]:


df = pd.read_csv('top100_kdrama.csv')


# In[8]:


app = dash.Dash(__name__)


# In[ ]:


app.layout = html.Div(children=[
   html.H1(children='Top 100 Kdramas Dashboard'),
   html.Div(children='''
       Analyzing the Top 100 Kdramas using Plotly Dash
   '''),
   dcc.Graph(
       id='histogram',
       figure={
           'data': [
               {'x': df['Rank'], 'type': 'histogram', 'name': 'Rank'},
           ],
           'layout': {
               'title': 'Rank of Kdrama'
           }
       }
   ),
   dcc.Graph(
       id='boxplot',
       figure={
           'data': [
               {'y': df['Score'], 'type': 'box', 'name': 'Score'},
           ],
           'layout': {
               'title': 'Distribution of Score'
           }
       }
   ),
   dcc.Graph(
       id='scatterplot',
       figure={
           'data': [
               {'x': df['Genre'], 'y': df['Score'], 'mode': 'markers', 'name': 'Genre vs. Score'},
           ],
           'layout': {
               'title': 'Genre vs. Score'
           }
       }
   ),
   dcc.Graph(
       id='barchart',
       figure={
           'data': [
               {'x': df['Episodes'], 'type': 'bar', 'name': 'Episodes'},
           ],
           'layout': {
               'title': 'Episodes Distribution'
           }
       }
   ),
   dcc.Graph(
       id='mosaicplot',
       figure=px.histogram(df, x="Score", color="Genre", barmode="overlay", nbins=10, width=800, height=500)
   )
    ])


# In[ ]:


if __name__ == '__main__':
   app.run_server(port=4050)


# In[ ]:





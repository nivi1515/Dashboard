from plotly.subplots import make_subplots
import plotly.graph_objects as go
from dash import Dash, html, dcc
from datetime import date
from dash import Dash, html, dcc, callback, Output, Input, dash_table
import plotly.express as px
import pandas as pd

df=pd.read_csv('P6-UK-Bank-Customers (1).csv')
fig = go.Figure()
rows,columns=df.shape
print(rows)
fig.add_trace(go.Indicator(
    mode = "number",
    value = rows,title='Total Customers'
    ))
fig2 = px.bar(df, x="Region", y="Customer ID", title='Balance by Region')
fig3 = px.bar(df, x="Region", y="Customer ID", title='Customer ID by Region')





app=Dash(__name__)

app.layout= html.Div(children=[
        html.H1(children='UK BANK CUSTOMER REPORT 2015',style={'background-color':'#00165e','text-align':'center','color': 'white'})
        ,html.Div(children=[
        dcc.Graph(id='card',figure=fig,style={'width':'200px','height':'200px','border': '2px solid','display':'inline-block'}),
        dcc.Checklist(id='region-checklist' ,labelClassName='Region',options=df['Region'].unique(),style={'width':'200px','height':'200px','border': '2px solid','display':'inline-block'}),
        dcc.Checklist(id='job-classfication' ,options=df['Job Classification'].unique(),style={'width':'200px','height':'200px','border': '2px solid','display':'inline-block'}),
dcc.Checklist(id='gender' ,options=df['Gender'].unique(),style={'width':'200px','height':'200px','border': '2px solid','display':'inline-block'})
],style={'display':'flex'}
    ),
    html.Div(children=[
        dcc.Graph(id='card1',figure=fig2,style={'border': '2px solid','width':'400px','height':'400px','display':'inline-block'}),
        dcc.Graph(id='card2',figure=fig2,style={'border': '2px solid','width':'400px','height':'400px','display':'inline-block'}),
        dcc.Graph(id='card3',figure=fig2,style={'border': '2px solid','width':'400px','height':'400px','display':'inline-block'})
    ],style={'display':'flex'}
    ),

    html.Div(children=[
dcc.Graph(id='card4',figure=fig3,style={'border': '2px solid','width':'400px','height':'400px','display':'inline-block'}),
dcc.Graph(id='card5',figure=fig3,style={'border': '2px solid','width':'400px','height':'400px','display':'inline-block'}),
dcc.Graph(id='card6',figure=fig3,style={'border': '2px solid','width':'400px','height':'400px','display':'inline-block'})
    ],style={'display':'flex'}
    )
    ]
    )




if __name__ == '__main__':
    app.run(debug=True)

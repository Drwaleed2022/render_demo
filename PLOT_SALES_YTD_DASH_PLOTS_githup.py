import pandas as pd
import plotly.express as px
from plotly.subplots import make_subplots
import plotly.graph_objects as go
import dash
from dash import html,dcc,dash_table
import numpy as np
import calendar
import datetime
sales_rep_sales=pd.read_csv('https://raw.githubusercontent.com/Drwaleed2022/render_demo/main/sales_rep_sales.csv')
Sales_representative=['ESRAA','SHIMAA','AYA','OMET','ISUPPLY','ISLAM','TOTAL']
for i in Sales_representative:
    sales_rep= i
    print(sales_rep)
ALL_YEAR= ['JAN','FEB','MAR','APR','MAY','JUN','JUL','AUG','SEP','OCT','NOV','DEC','YTD']
for i in ALL_YEAR:
    month=i
    print(month)  
sales_rep_sales.set_index('sales_rep',inplace=True)
# Create a dash application
from dash import Output
from dash import Dash
from dash.dash import Input
      
import flask, multiprocessing
app = Dash(__name__, suppress_callback_exceptions=True)
server=app.server
# Build dash app layout
app.layout = html.Div(children=[ html.H1('2024 Sales Statistics Dashboard', 
                                style={'textAlign': 'center', 'color': '#503D36',
                                'font-size': 35}),
                                
                                html.Div([
                                        html.Div(["Sales rep:",dcc.Dropdown(Sales_representative,id='sales_rep', value='SHIMAA', 
                                style={'height':'35px','width':'700px', 'font-size': 20})]),
                                        html.Div(["Month:"  ,dcc.Dropdown(ALL_YEAR,id='month',value='APR', 
                                style={'height':'35px','width':'700px', 'font-size': 20})])                                                            
                                ],style={'font-size': 25,'display': 'flex'}),                               
                                html.Br(),
                                html.Br(),
                                # Segment 1
                                html.Div([
                                        html.Div(dcc.Graph(id='sales_rep_curve1'))
                                ], style={'font-size': 25,'width':'1400px'}),                            
                                # Segment 2
                                html.Div([                                        
                                        html.Div(dcc.Graph(id='sales_rep_curve2'))
                                ], style={'font-size': 25,'width':'1400px'})
                                ])
# Callback decorator
@app.callback( [
               Output(component_id='sales_rep_curve1', component_property='figure'),
               Output(component_id='sales_rep_curve2', component_property='figure')
               
            ],
               [Input(component_id='sales_rep', component_property='value'),
                Input(component_id='month', component_property='value')])

                
# Computation to callback function and return graph
def update_output(sales_rep,month): 
    sales_rep_curve1=px.bar(sales_rep_sales,color=Sales_representative,y=month,title = 'Sales per rep in selected month',text_auto=True)
    sales_rep_curve2=px.bar(sales_rep_sales.loc[sales_rep],color=ALL_YEAR,title = 'Sales  in 2024 by specific sales rep',text_auto=True)
    return[sales_rep_curve1,sales_rep_curve2]
#port=8070
#def open_browser() :
    #webbrowser.open_new("http://localhost:{}".format(port))  

if __name__ == '__main__':
    #Timer(1,open_browser).start();
    app.run_server(host='54.254.162.138',port=8080,debug=False)
 

   

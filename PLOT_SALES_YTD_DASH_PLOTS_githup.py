import pandas as pd
import plotly.express as px
from plotly.subplots import make_subplots
import plotly.graph_objects as go
import dash
from dash import html,dcc,dash_table
import numpy as np
import calendar
import datetime
import gunicorn
#
Area_rep_sales=pd.read_csv('https://raw.githubusercontent.com/Drwaleed2022/render_demo/main/Area_rep_sales.csv')
Area_rep_sales.set_index('Area_rep',inplace=True)
Area_rep_profit=pd.read_csv('e:/DASHBOARD/Area_rep_profit.csv')
Area_rep_profit.set_index('Area_rep',inplace=True)
Area_sales=pd.read_csv('https://raw.githubusercontent.com/Drwaleed2022/render_demo/main/Area_sales.csv')
Area_sales.set_index('Area',inplace=True)
Area_profit=pd.read_csv('e:/DASHBOARD/Area_profit.csv')
Area_profit.set_index('Area',inplace=True)
sales_rep_sales=pd.read_csv('https://raw.githubusercontent.com/Drwaleed2022/render_demo/main/sales_rep_sales.csv')
sales_rep_sales.set_index('sales_rep',inplace=True)
sales_rep_profit=pd.read_csv('e:/DASHBOARD/sales_rep_profit.csv')
sales_rep_profit.set_index('sales_rep',inplace=True) 
Sales_representative=['ESRAA','SHIMAA','AYA','OMET','ISUPPLY','ISLAM','TOTAL']
for i in Sales_representative:
    sales_rep= i
    print(sales_rep)
ALL_YEAR= ['JAN','FEB','MAR','APR','MAY','JUN','JUL','AUG','SEP','OCT','NOV','DEC','YTD']
for i in ALL_YEAR:
    month=i
    print(month)  
AREA=['GOMLA', 'Alexandria', 'Behira', 'Matrouh','Total_pharmacy','Global_sales']
for i in AREA:
    area=i
    print(area)
AREA_REP=['GOMLA / ISLAM','Alexandria / ESRAA','Behira / SHIMAA','Alexandria / SHIMAA','Alexandria / OMET','Matrouh / SHIMAA','Alexandria / AYA','Alexandria / ISUPPLY','Behira / AYA','Alexandria / others','Behira / OMET']
for i in AREA_REP:
    area_rep=i
    print(area_rep)    

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
                                
                                html.Div([html.Div(["Sales rep:",dcc.Dropdown(Sales_representative,id='sales_rep', value='SHIMAA', 
                                style={'height':'35px','width':'500px', 'font-size': 20})]),
                                html.Div(["Area:",dcc.Dropdown(AREA,id='area', value='Global_sales',                               
                                style={'height':'35px','width':'500px', 'font-size': 20})]),  
                                                                                                    
                                ],style={'font-size': 25,'display': 'flex'}),
                                html.Div([
                                        
                                        html.Div(["Month:"  ,dcc.Dropdown(ALL_YEAR,id='month',value='APR', 
                                style={'height':'35px','width':'500px', 'font-size': 20})]),
                                html.Div(["Area_rep:"  ,dcc.Dropdown(AREA_REP,id='area_rep',value='Alexandria / SHIMAA', 
                                style={'height':'35px','width':'500px', 'font-size': 20})])  
                                                            
                                ],style={'font-size': 25,'display': 'flex'}),                               
                                html.Br(),
                                html.Br(), 
                                  # Segment 1
                                html.Div([
                                        html.Div(dcc.Graph(id='area_curve1')),
                                        html.Div(dcc.Graph(id='area_curve2'))
                                ], style={'font-size': 25,'display': 'flex'}),                            
                                # Segment 2
                                html.Div([                                        
                                        html.Div(dcc.Graph(id='sales_rep_curve1')),
                                        html.Div(dcc.Graph(id='sales_rep_curve2'))
                                ], style={'font-size': 25,'display': 'flex'}),
                                 # Segment 3
                                html.Div([                                        
                                        html.Div(dcc.Graph(id='area_rep_curve1')),
                                        html.Div(dcc.Graph(id='area_rep_curve2'))
                                ], style={'font-size': 25,'display': 'flex'})
                                
                                ])


'''def compute_info(df_month_number,month):
    df_X =df_month_number[df_month_number[Month]==int(month)]
    return df_X'''
# Callback decorator
@app.callback( [
               Output(component_id='area_curve1', component_property='figure'),
               Output(component_id='area_curve2', component_property='figure'),
               Output(component_id='sales_rep_curve1', component_property='figure'),
               Output(component_id='sales_rep_curve2', component_property='figure'),
               Output(component_id='area_rep_curve1', component_property='figure'),
               Output(component_id='area_rep_curve2', component_property='figure')
            ],
               [Input(component_id='area', component_property='value'),
                Input(component_id='sales_rep', component_property='value'),
                Input(component_id='month', component_property='value')],
                Input(component_id='area_rep', component_property='value'))
# Computation to callback function and return graph
def update_output(area,sales_rep,month,area_rep): 
    area_curve1=px.bar(Area_sales,y=month,color=month,title =  'Sales per Area in selected month',text_auto=True)
    area_curve2=px.bar(Area_sales.loc[area],color=ALL_YEAR,title =  'Sales in selected Area',text_auto=True)
    sales_rep_curve1=px.bar(sales_rep_sales,y=month,color=month,title = 'Sales per rep in selected month',text_auto=True)
    sales_rep_curve2=px.bar(sales_rep_sales.loc[sales_rep],color=ALL_YEAR,title = 'Sales  in 2024 by specific sales rep',text_auto=True)
    area_rep_curve1=px.bar(Area_rep_sales,y=month,color=month,text_auto=True,title= 'Sales of rep per area in selected month')
    area_rep_curve2=px.bar(Area_rep_sales.loc[area_rep],color=ALL_YEAR,text_auto=True,title= 'Sales of specific rep in specific area')
    return[area_curve1,area_curve2,sales_rep_curve1,sales_rep_curve2,area_rep_curve1,area_rep_curve2]
#port=8070
#def open_browser() :
    #webbrowser.open_new("http://localhost:{}".format(port))  

if __name__ == '__main__':
    #Timer(1,open_browser).start();
    app.run_server(host='0.0.0.0',port=5000,debug=False)
 

   

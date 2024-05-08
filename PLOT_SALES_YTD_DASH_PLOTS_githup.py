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
AREA_REP_SALES_PROFIT=pd.read_csv("https://raw.githubusercontent.com/Drwaleed2022/render_demo/main/AREA_REP_SALES_PROFIT.csv")
AREA_REP_PROFIT=pd.read_csv("https://raw.githubusercontent.com/Drwaleed2022/render_demo/main/Area_rep_profit.csv")
AREA_REP_SALES=pd.read_csv("https://raw.githubusercontent.com/Drwaleed2022/render_demo/main/Area_rep_sales.csv")
AREA_REP_SALES_reindex=pd.read_csv("https://raw.githubusercontent.com/Drwaleed2022/render_demo/main/AREA_REP_SALES_reindex.csv")
all_pharmacies_sales=pd.read_csv("https://raw.githubusercontent.com/Drwaleed2022/render_demo/main/all_pharmacies_sales.csv")
AREA_REP_SALES.set_index('Area_rep',inplace=True)
AREA=AREA_REP_SALES.index
for i in AREA:
    area=i
    print(area)
Date=AREA_REP_SALES.columns
for i in Date:
    date=i
    print(date)
all_pharmacies_sales.set_index('pharmacy',inplace=True)   
PHARMACY=all_pharmacies_sales.index
for i in PHARMACY:
    pharmacy= i
    print(pharmacy)     
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
                                        html.Div(["Date:"  ,dcc.Dropdown(Date,id='date',value='5/2024', 
                                style={'height':'35px','width':'700px', 'font-size': 20})]),
                                        html.Div(["AREA:",dcc.Dropdown(AREA,id='area', value='global_sales', 
                                style={'height':'35px','width':'700px', 'font-size': 20})]),
                                        html.Div(["Pharmacy:"  ,dcc.Dropdown(PHARMACY,id='pharmacy',value='ص المعسكر الروماني/شهري',
                                style={'height':'35px','width':'700px', 'font-size': 20})]),  
                                                                                                    
                                ],style={'font-size': 25,'display': 'flex'}),                                                             
                               
                                                                                    
                                # Segment 1
                                html.Div([                                        
                                        html.Div(dcc.Graph(id='area_rep_curve0')),
                                        html.Div(dcc.Graph(id='area_rep_curve1')),
                                         html.Div(dcc.Graph(id='all_pharmacies_curve'))
                                ], style={'font-size': 25,'display': 'flex'}),
                                # Segment 2
                                html.Div([                                        
                                        html.Div(dcc.Graph(id='area_rep_curve2')),
                                        html.Div(dcc.Graph(id='area_rep_curve3')),
                                        html.Div(dcc.Graph(id='area_rep_curve4'))
                                ], style={'font-size': 25,'display': 'flex'}),
                                # Segment 3
                                html.Div([
                                        html.Div( dash_table.DataTable(AREA_REP_SALES_reindex.to_dict('records'), [{"name": i, "id": i} for i in AREA_REP_SALES_reindex.columns]))
                                ], style={'font-size': 20,'color': 'blue'}), 
                                
                                ])


'''def compute_info(df_month_number,month):
    df_X =df_month_number[df_month_number[Month]==int(month)]
    return df_X'''
# Callback decorator
@app.callback( [
               Output(component_id='area_rep_curve0', component_property='figure'),
               Output(component_id='area_rep_curve1', component_property='figure'),
               Output(component_id='all_pharmacies_curve', component_property='figure'),
               Output(component_id='area_rep_curve2', component_property='figure'),
               Output(component_id='area_rep_curve3', component_property='figure'),
               Output(component_id='area_rep_curve4', component_property='figure')
            ],
               [Input(component_id='area', component_property='value'),
                Input(component_id='date', component_property='value'),
                Input(component_id='pharmacy', component_property='value')])
# Computation to callback function and return graph
def update_output(area,date,pharmacy): 
    area_rep_curve0=px.bar(AREA_REP_SALES,y=date,color=AREA,text_auto=True,title= 'Whole sales per Area & rep in specific date')
    area_rep_curve1=px.bar(AREA_REP_SALES.loc[area],color=Date,text_auto=True,title= 'Whole sales per Area & rep')
    all_pharmacies_curve=px.bar(all_pharmacies_sales.loc[pharmacy],color=Date,orientation='h',text_auto=True,title='Sales of pharmacy in 2024')
    area_rep_curve2=px.scatter(AREA_REP_SALES.loc[['ALEXANDRIA_GLOBAL','BEHIRA_GLOBAL','MATROUH_GLOBAL']], y=date, size=date,text=date,hover_name=date, title='Geographical sales in specific month',color=date, size_max=120)
    area_rep_curve3=px.scatter(AREA_REP_SALES.loc[['SHIMAA_GLOBAL','ESRAA_GLOBAL','AYA_GLOBAL','OMET_GLOBAL','I_SUPPLY_GLOBAL']], y=date, size=date,text=date,hover_name=date, title='Sales rep sales in specific month',color=date, size_max=120)
    area_rep_curve4=px.pie(AREA_REP_SALES.loc[[ 'GOMLA / ISLAM', 'global_pharmacy']],names=['GOMLA / ISLAM', 'global_pharmacy'],values=date,title = ' Gomla & Pharmacy sales ratio in specific month ' )
    return[area_rep_curve0,area_rep_curve1,all_pharmacies_curve,area_rep_curve2,area_rep_curve3,area_rep_curve4]
#port=8070
#def open_browser() :
    #webbrowser.open_new("http://localhost:{}".format(port))  

if __name__ == '__main__':
    #Timer(1,open_browser).start();        
    app.run_server(host='0.0.0.0',port=5000,debug=False)
 

   

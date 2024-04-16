import pandas as pd
import plotly.express as px
from plotly.subplots import make_subplots
import plotly.graph_objects as go
import dash
from dash import html,dcc,dash_table
import numpy as np
import calendar
import datetime

df=pd.read_csv("https://raw.githubusercontent.com/Drwaleed2022/render_demo/main/YTD_2024.csv")
df.columns=['cost','sales','return','return_profit','profit','total_profit','sales_rep','serial','pharmacy','date','rep','driver','store_num']
df['sales']=df['sales']-df['return']
df.drop(axis=1,columns=['cost','return','return_profit','rep','total_profit','serial','driver','store_num'],inplace=True)
df['Area']=df['pharmacy']
dates=df['date'].to_list()
dates=pd.to_datetime(dates,dayfirst=True)
df['Month'] =pd.DatetimeIndex(dates).month
df.drop(axis=1,columns='date',inplace=True)
df['profit']=df['profit'].round()
df['sales']=df['sales'].round()
df['sales_rep'].replace('اسراء خالد','ESRAA',inplace=True)
df['sales_rep'].replace('شيماء','SHIMAA',inplace=True)
df['sales_rep'].replace('اية ','AYA',inplace=True)
df['sales_rep'].replace('اى سبلاى','ISUPPLY',inplace=True)
df['sales_rep'].replace(['اوميت ',   'اوميت/ 357.201/2051823', 'اوميت/ 668.083/2051937',
       'اوميت/ 555.597/2052113', 'اوميت/ 445.768/2052225',
       'اوميت/ 444.760/2052287', 'اوميت/ 543.557/2052304',
       'اوميت/ 497.285/2052510', 'اوميت/ 547.205/2052516',
       'اوميت/ 372.904/2052593', 'اوميت/ 356.543/2052607',
       'اوميت/ 868.129/2052648', 'اوميت/ 385.253/2053042',
       'اوميت/ 400.504/2053046', 'اوميت/ 999.091/2053077',
       'اوميت/ 439.323/2053094', 'اوميت/ 858.509/2053232',
       'اوميت/ 717.567/2053285', 'اوميت/ 573.307/2053328',
       'اوميت/ 2035.411/2053339', 'اوميت/ 535.966/2053358',
       'اوميت/ 707.048/2053365', 'اوميت/ 1166.310/2053385',
       'اوميت/ 617.406/2053393', 'اوميت/ 1128.781/2053416',
       'اوميت/ 591.576/2053420', 'اوميت/ 503.974/2054793',
       'اوميت/ 582.055/2054020', 'اوميت/ 446.054/2054052',
       'اوميت/ 557.986/2054540', 'اوميت/ 1163.262/2054707',
       'اوميت/ 588.797/2054812', 'اوميت/ 810.530/2054886',
       'اوميت/ 1175.903/2054944', 'اوميت/ 420.764/2055357',
       'اوميت/ 818.788/2068110', 'اوميت/ 1761.768/2068547',
       'اوميت/ 746.995/2068591', 'اوميت/ 371.884/2068675',
       'اوميت/ 429.836/2068697', 'اوميت/ 376.954/2068986',
       'اوميت/ 1188.299/2069292', 'اوميت/ 763.653/2069334',
       'اوميت/ 979.160/2069373', 'اوميت/ 421.204/2069450',
       'اوميت/ 593.995/2056069', 'اوميت/ 18364.121/2056122',
       'اوميت/ 369.155/2056228', 'اوميت/ 350.664/2056254','اوميت/ 2093.928/2155575', 'اوميت/ 654.361/2155669','اوميت/ 383.552/2155876', 'اوميت/ 368.007/2155980',
       'اوميت/ 375.000/2156009', 'اوميت/ 528.797/2159781',
       'اوميت/ 794.957/2159794', 'اوميت/ 464.344/2159798','اوميت/ 546.711/2056305', 'اوميت/ 493.004/2056345',
       'اوميت/ 585.046/2056408', 'اوميت/ 351.923/2056474',
       'اوميت/ 375.883/2056477', 'اوميت/ 467.175/2056598',
       'اوميت/ 647.721/2056630', 'اوميت/ 537.535/2056909',
       'اوميت/ 377.750/2057044', 'اوميت/ 865.695/2057047',
       'اوميت/ 467.295/2057059', 'اوميت/ 478.355/2057092',
       'اوميت/ 352.963/2057160', 'اوميت/ 362.111/2057174',
       'اوميت/ 786.400/2057245', 'اوميت/ 401.674/2057298',
       'اوميت/ 431.160/2057329', 'اوميت/ 570.382/2057346',
       'اوميت/ 412.979/2057393', 'اوميت/ 426.487/2057972',
       'اوميت/ 418.500/2060111', 'اوميت/ 407.134/2060160',
       'اوميت/ 735.967/2060184', 'اوميت/ 716.656/2060474',
       'اوميت/ 663.755/2060494', 'اوميت/ 719.102/2060546',
       'اوميت/ 406.883/2060623', 'اوميت/ 377.258/2060678',
       'اوميت/ 366.324/2060693', 'اوميت/ 381.224/2060743',
       'اوميت/ 839.059/2060755', 'اوميت/ 366.843/2060896',
       'اوميت/ 733.256/2060903', 'اوميت/ 1373.765/2060915',
       'اوميت/ 371.532/2061022', 'اوميت/ 578.925/2061322', 'اوميت/ 563.946/2061559', 'اوميت/ 1509.615/2061865',
       'اوميت/ 405.345/2061942', 'اوميت/ 400.343/2062163',
       'اوميت/ 388.189/2062255', 'اوميت/ 452.864/2062326',
       'اوميت/ 511.505/2062447', 'اوميت/ 455.175/2065483',
       'اوميت/ 376.773/2065834', 'اوميت/ 1088.821/2065855',
       'اوميت/ 357.318/2067107', 'اوميت/ 491.494/2067240',
       'اوميت/ 756.386/2067320', 'اوميت/ 463.650/2067350',
       'اوميت/ 426.376/2067384', 'اوميت/ 633.687/2067463',
       'اوميت/ 353.918/2067465', 'اوميت/ 895.861/2067499',
       'اوميت/ 597.523/2067563', 'اوميت/ 551.526/2068012','اوميت/ 397.130/2051711', 'OMET', 'اوميت/ 596.360/2065878',
       'اوميت/ 363.353/2065973', 'اوميت/ 856.940/2066177',
       'اوميت/ 376.163/2066262', 'اوميت/ 358.734/2066309',
       'اوميت/ 512.769/2066367', 'اوميت/ 477.665/2066379',
       'اوميت/ 357.638/2066512', 'اوميت/ 631.806/2066597',
       'اوميت/ 382.504/2066909',
       'اوميت/ 369.433/2159876', 'اوميت/ 379.083/2160230' ],'OMET',inplace=True)
df['sales_rep'].replace('اسلام مشتريات','ISLAM',inplace=True)
df['sales_rep'].replace(['احمد الجندى','هبه الله احمد ', 'رمضان خميس', 'وائل المحمودي','محمد اشرف','د وليد ','اميرة ', 'وائل المحمدي', 'السماك','احمد على', 'احمد علاء سيلز ', 'اسماء سيلز', 'اسماء/سيلز ', 'احمد العزازي', 'البشمهندسة', 'ايه محمد', 'شروق', 'رامي  مشتريات','جودي', 'اسراء حسن', 'محمد حمدى','محمد ايوب'],'others',inplace=True)
Sales_representative=['ESRAA','SHIMAA','AYA','OMET','ISUPPLY','ISLAM','TOTAL']
for i in Sales_representative:
    sales_rep= i
    print(sales_rep)
ALL_YEAR= ['JAN','FEB','MAR','APR','MAY','JUN','JUL','AUG','SEP','OCT','NOV','DEC','YTD']
for i in ALL_YEAR:
    month=i
    print(month)              
all_sales_JAN=df[['pharmacy','sales','profit','sales_rep']][df['Month']==1].groupby(['pharmacy','sales_rep']).agg({"sales":sum,"profit":sum}).sort_values('sales',ascending=False)
all_sales_JAN.rename(columns={'sales':'JAN','profit':'JAN_profit'}, inplace=True)
all_sales_JAN
all_sales_FEB=df[['pharmacy','sales','profit','sales_rep']][df['Month']==2].groupby(['pharmacy','sales_rep']).agg({"sales":sum,"profit":sum}).sort_values('sales',ascending=False)
all_sales_FEB.rename(columns={'sales':'FEB','profit':'FEB_profit'}, inplace=True)
all_sales_FEB
all_sales_MAR=df[['pharmacy','sales','profit','sales_rep']][df['Month']==3].groupby(['pharmacy','sales_rep']).agg({"sales":sum,"profit":sum}).sort_values('sales',ascending=False)
all_sales_MAR.rename(columns={'sales':'MAR','profit':'MAR_profit'}, inplace=True)
all_sales_MAR
all_sales_APR=df[['pharmacy','sales','profit','sales_rep']][df['Month']==4].groupby(['pharmacy','sales_rep']).agg({"sales":sum,"profit":sum}).sort_values('sales',ascending=False)
all_sales_APR.rename(columns={'sales':'APR','profit':'APR_profit'}, inplace=True)
all_sales_APR
all_sales_MAY=df[['pharmacy','sales','profit','sales_rep']][df['Month']==5].groupby(['pharmacy','sales_rep']).agg({"sales":sum,"profit":sum}).sort_values('sales',ascending=False)
all_sales_MAY.rename(columns={'sales':'MAY','profit':'MAY_profit'}, inplace=True)
all_sales_MAY
all_sales_JUN=df[['pharmacy','sales','profit','sales_rep']][df['Month']==6].groupby(['pharmacy','sales_rep']).agg({"sales":sum,"profit":sum}).sort_values('sales',ascending=False)
all_sales_JUN.rename(columns={'sales':'JUN','profit':'JUN_profit'}, inplace=True)
all_sales_JUN
all_sales_JUL=df[['pharmacy','sales','profit','sales_rep']][df['Month']==7].groupby(['pharmacy','sales_rep']).agg({"sales":sum,"profit":sum}).sort_values('sales',ascending=False)
all_sales_JUL.rename(columns={'sales':'JUL','profit':'JUL_profit'}, inplace=True)
all_sales_JUL
all_sales_AUG=df[['pharmacy','sales','profit','sales_rep']][df['Month']==8].groupby(['pharmacy','sales_rep']).agg({"sales":sum,"profit":sum}).sort_values('sales',ascending=False)
all_sales_AUG.rename(columns={'sales':'AUG','profit':'AUG_profit'}, inplace=True)
all_sales_AUG
all_sales_SEP=df[['pharmacy','sales','profit','sales_rep']][df['Month']==9].groupby(['pharmacy','sales_rep']).agg({"sales":sum,"profit":sum}).sort_values('sales',ascending=False)
all_sales_SEP.rename(columns={'sales':'SEP','profit':'SEP_profit'}, inplace=True)
all_sales_SEP
all_sales_OCT=df[['pharmacy','sales','profit','sales_rep']][df['Month']==10].groupby(['pharmacy','sales_rep']).agg({"sales":sum,"profit":sum}).sort_values('sales',ascending=False)
all_sales_OCT.rename(columns={'sales':'OCT','profit':'OCT_profit'}, inplace=True)
all_sales_OCT
all_sales_NOV=df[['pharmacy','sales','profit','sales_rep']][df['Month']==11].groupby(['pharmacy','sales_rep']).agg({"sales":sum,"profit":sum}).sort_values('sales',ascending=False)
all_sales_NOV.rename(columns={'sales':'NOV','profit':'NOV_profit'}, inplace=True)
all_sales_NOV
all_sales_DEC=df[['pharmacy','sales','profit','sales_rep']][df['Month']==12].groupby(['pharmacy','sales_rep']).agg({"sales":sum,"profit":sum}).sort_values('sales',ascending=False)
all_sales_DEC.rename(columns={'sales':'DEC','profit':'DEC_profit'}, inplace=True)
all_sales_DEC
all_sales_YTD=df[['pharmacy','sales','profit','sales_rep']].groupby(['pharmacy','sales_rep']).agg({"sales":sum,"profit":sum}).sort_values('sales',ascending=False)
all_sales_YTD.rename(columns={'sales':'YTD','profit':'YTD_profit'}, inplace=True)
all_sales_YTD
all_sales=all_sales_YTD.join(all_sales_JAN).join(all_sales_FEB).join(all_sales_MAR).join(all_sales_APR).join(all_sales_MAY).join(all_sales_JUN).join(all_sales_JUL).join(all_sales_AUG).join(all_sales_SEP).join(all_sales_OCT).join(all_sales_NOV).join(all_sales_DEC)
all_sales.fillna(0,inplace=True)
all_sales.sort_values('YTD',ascending=False,inplace=True)
all_sales.reset_index(inplace=True)
all_sales
sales_rep_JAN=df[['pharmacy','sales','profit','sales_rep']][df['Month']==1].groupby('sales_rep').agg({"sales":sum,"profit":sum}).sort_values('sales',ascending=False)
sales_rep_JAN.rename(columns={'sales':'JAN','profit':'JAN_profit'}, inplace=True)
sales_rep_JAN
sales_rep_FEB=df[['pharmacy','sales','profit','sales_rep']][df['Month']==2].groupby('sales_rep').agg({"sales":sum,"profit":sum}).sort_values('sales',ascending=False)
sales_rep_FEB.rename(columns={'sales':'FEB','profit':'FEB_profit'}, inplace=True)
sales_rep_FEB
sales_rep_MAR=df[['pharmacy','sales','profit','sales_rep']][df['Month']==3].groupby('sales_rep').agg({"sales":sum,"profit":sum}).sort_values('sales',ascending=False)
sales_rep_MAR.rename(columns={'sales':'MAR','profit':'MAR_profit'}, inplace=True)
sales_rep_MAR
sales_rep_APR=df[['pharmacy','sales','profit','sales_rep']][df['Month']==4].groupby('sales_rep').agg({"sales":sum,"profit":sum}).sort_values('sales',ascending=False)
sales_rep_APR.rename(columns={'sales':'APR','profit':'APR_profit'}, inplace=True)
sales_rep_APR
sales_rep_MAY=df[['pharmacy','sales','profit','sales_rep']][df['Month']==5].groupby('sales_rep').agg({"sales":sum,"profit":sum}).sort_values('sales',ascending=False)
sales_rep_MAY.rename(columns={'sales':'MAY','profit':'MAY_profit'}, inplace=True)
sales_rep_MAY
sales_rep_JUN=df[['pharmacy','sales','profit','sales_rep']][df['Month']==6].groupby('sales_rep').agg({"sales":sum,"profit":sum}).sort_values('sales',ascending=False)
sales_rep_JUN.rename(columns={'sales':'JUN','profit':'JUN_profit'}, inplace=True)
sales_rep_JUN
sales_rep_JUL=df[['pharmacy','sales','profit','sales_rep']][df['Month']==7].groupby('sales_rep').agg({"sales":sum,"profit":sum}).sort_values('sales',ascending=False)
sales_rep_JUL.rename(columns={'sales':'JUL','profit':'JUL_profit'}, inplace=True)
sales_rep_JUL
sales_rep_AUG=df[['pharmacy','sales','profit','sales_rep']][df['Month']==8].groupby('sales_rep').agg({"sales":sum,"profit":sum}).sort_values('sales',ascending=False)
sales_rep_AUG.rename(columns={'sales':'AUG','profit':'AUG_profit'}, inplace=True)
sales_rep_AUG
sales_rep_SEP=df[['pharmacy','sales','profit','sales_rep']][df['Month']==9].groupby('sales_rep').agg({"sales":sum,"profit":sum}).sort_values('sales',ascending=False)
sales_rep_SEP.rename(columns={'sales':'SEP','profit':'SEP_profit'}, inplace=True)
sales_rep_SEP
sales_rep_OCT=df[['pharmacy','sales','profit','sales_rep']][df['Month']==10].groupby('sales_rep').agg({"sales":sum,"profit":sum}).sort_values('sales',ascending=False)
sales_rep_OCT.rename(columns={'sales':'OCT','profit':'OCT_profit'}, inplace=True)
sales_rep_OCT
sales_rep_NOV=df[['pharmacy','sales','profit','sales_rep']][df['Month']==11].groupby('sales_rep').agg({"sales":sum,"profit":sum}).sort_values('sales',ascending=False)
sales_rep_NOV.rename(columns={'sales':'NOV','profit':'NOV_profit'}, inplace=True)
sales_rep_NOV
sales_rep_DEC=df[['pharmacy','sales','profit','sales_rep']][df['Month']==12].groupby('sales_rep').agg({"sales":sum,"profit":sum}).sort_values('sales',ascending=False)
sales_rep_DEC.rename(columns={'sales':'DEC','profit':'DEC_profit'}, inplace=True)
sales_rep_DEC
sales_rep_YTD=df[['pharmacy','sales','profit','sales_rep']].groupby('sales_rep').agg({"sales":sum,"profit":sum}).sort_values('sales',ascending=False)
sales_rep_YTD.rename(columns={'sales':'YTD','profit':'YTD_profit'}, inplace=True)
sales_rep_YTD
sales_rep_sales=sales_rep_YTD.join(sales_rep_JAN).join(sales_rep_FEB).join(sales_rep_MAR).join(sales_rep_APR).join(sales_rep_MAY).join(sales_rep_JUN).join(sales_rep_JUL).join(sales_rep_AUG).join(sales_rep_SEP).join(sales_rep_OCT).join(sales_rep_NOV).join(sales_rep_DEC)
sales_rep_sales.fillna(0,inplace=True)
sales_rep_sales.sort_values('YTD',ascending=False,inplace=True)
sales_rep_sales.reset_index(inplace=True)
sales_rep_profit=sales_rep_sales[['sales_rep', 'YTD_profit','JAN_profit','FEB_profit','MAR_profit','APR_profit','MAY_profit', 'JUN_profit','JUL_profit','AUG_profit','SEP_profit','OCT_profit','NOV_profit','DEC_profit']].sort_values('YTD_profit',ascending=False)
sales_rep_profit.rename(columns={'JAN_profit':'JAN','FEB_profit':'FEB','MAR_profit':'MAR','APR_profit':'APR','MAY_profit':'MAY', 'JUN_profit':'JUN','JUL_profit':'JUL','AUG_profit':'AUG','SEP_profit':'SEP','OCT_profit':'OCT','NOV_profit':'NOV','DEC_profit':'DEC', 'YTD_profit':'YTD'},inplace=True)
sales_rep_sales.drop(axis=1,columns=['JAN_profit','FEB_profit','MAR_profit','APR_profit','MAY_profit','JUN_profit','JUL_profit','AUG_profit','SEP_profit','OCT_profit','NOV_profit','DEC_profit','YTD_profit'],inplace=True)
sales_rep_sales.set_index('sales_rep',inplace=True)
sales_rep_sales.loc['TOTAL']=sales_rep_sales.loc['ISLAM']+sales_rep_sales.loc['SHIMAA']+sales_rep_sales.loc['ESRAA']+sales_rep_sales.loc['AYA']+sales_rep_sales.loc['OMET']+sales_rep_sales.loc['ISUPPLY']
sales_rep_sales=sales_rep_sales.sort_values('YTD',ascending=False)
sales_rep_sales.drop(axis=0,index='others',inplace=True)
sales_rep_sales=sales_rep_sales.transpose()
def create_tables():
    # The following line will remove this handler, making it
    # only run on the first request
    app.before_request_funcs[None].remove(create_tables)

    db.create_all()
    
# Create a dash application
from dash import Output
from dash.dash import Input
app = Dash(__name__)
server=app.server

# Build dash app layout
# Callback decorator
@app.callback( [
               Output(component_id='sales_rep_curve1', component_property='figure'),
               Output(component_id='sales_rep_curve2', component_property='figure')
               
            ],
               [Input(component_id='sales_rep', component_property='value'),
                Input(component_id='month', component_property='value')])

                
# Computation to callback function and return graph
def update_output(sales_rep,month): 
    sales_rep_curve1=px.bar(sales_rep_sales.loc[month],color=Sales_representative,title = 'Sales per rep in selected month',text_auto=True)
    sales_rep_curve2=px.bar(sales_rep_sales,color=ALL_YEAR,y=sales_rep,title = 'Sales  in 2024 by specific sales rep',text_auto=True)
    return[sales_rep_curve1,sales_rep_curve2]
#def open_browser() :
    #webbrowser.open_new("http://localhost:{}".format(port))                 
if __name__ == '__main__':
    #Timer(1,open_browser).start();
    app.run_server(debug=False)    
   

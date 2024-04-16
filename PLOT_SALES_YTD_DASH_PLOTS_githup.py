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
x=df['Area'][df['Area'].str.startswith('شركة')].to_list()
B=df['Area'][df['Area'].str.contains('البحير')].to_list()
M=df['Area'][df['Area'].str.contains('عماد حمد')].to_list()
G=df['Area'][df['Area'].str.startswith('مخزن')].to_list()
A=df['Area'][-df['Area'].str.startswith('شركة')][-df['Area'].str.contains('عماد حمد','مطروح')][-df['Area'].str.contains('البحير')][-df['Area'].str.startswith('مخزن')].to_list()
df['Area']=pd.DataFrame(df['Area'].replace(B,'Behira'))
df['Area']=pd.DataFrame(df['Area'].replace(M,'Matrouh'))
df['Area']=pd.DataFrame(df['Area'].replace(A,'Alexandria'))
df['Area']=pd.DataFrame(df['Area'].replace(G,'GOMLA'))
df['Area']=pd.DataFrame(df['Area'].replace(x,'Nile'))
dates=df['date'].to_list()
dates=pd.to_datetime(dates,dayfirst=True)
df['Month'] =pd.DatetimeIndex(dates).month
for i in df['Month']:
    df['Month'].replace(i,calendar.month_abbr[i],inplace=True)
    print(df['Month'])
df['Month']=df['Month'].str.upper()    
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
Sales_representative=['ESRAA','SHIMAA','AYA','OMET','ISUPPLY','ISLAM','others']
for i in Sales_representative:
    sales_rep= i
    print(sales_rep)
df['Area_rep']=df['Area']+" / "+df['sales_rep']
AREA=['GOMLA', 'Alexandria', 'Behira', 'Matrouh','Total_pharmacy','Global_sales']
for i in AREA:
    area=i
    print(area)
AREA_REP=['GOMLA / ISLAM','Alexandria / ESRAA','Behira / SHIMAA','Alexandria / SHIMAA','Alexandria / OMET','Matrouh / SHIMAA','Alexandria / AYA','Alexandria / ISUPPLY','Behira / AYA','Alexandria / others','Behira / OMET']
for i in AREA_REP:
    area_rep=i
    print(area_rep)
ALL_YEAR= ['JAN','FEB','MAR','APR','MAY','JUN','JUL','AUG','SEP','OCT','NOV','DEC','YTD']
for i in ALL_YEAR:
    month=i
    print(month)
Nile_df=df[df['Area'].str.startswith('Nile')]
N=df['Area'][df['Area'].str.startswith('Nile')].to_list()
df.set_index('Area',inplace=True)
df.drop(axis=0,index=N,inplace=True)
df.reset_index(inplace=True)
df['Area'].unique()                
all_sales_JAN=df[['pharmacy','sales','profit','sales_rep']][df['Month']=='JAN'].groupby(['pharmacy','sales_rep']).agg({"sales":sum,"profit":sum}).sort_values('sales',ascending=False)
all_sales_JAN.rename(columns={'sales':'JAN','profit':'JAN_profit'}, inplace=True)
all_sales_JAN
all_sales_FEB=df[['pharmacy','sales','profit','sales_rep']][df['Month']=='FEB'].groupby(['pharmacy','sales_rep']).agg({"sales":sum,"profit":sum}).sort_values('sales',ascending=False)
all_sales_FEB.rename(columns={'sales':'FEB','profit':'FEB_profit'}, inplace=True)
all_sales_FEB
all_sales_MAR=df[['pharmacy','sales','profit','sales_rep']][df['Month']=='MAR'].groupby(['pharmacy','sales_rep']).agg({"sales":sum,"profit":sum}).sort_values('sales',ascending=False)
all_sales_MAR.rename(columns={'sales':'MAR','profit':'MAR_profit'}, inplace=True)
all_sales_MAR
all_sales_APR=df[['pharmacy','sales','profit','sales_rep']][df['Month']=='APR'].groupby(['pharmacy','sales_rep']).agg({"sales":sum,"profit":sum}).sort_values('sales',ascending=False)
all_sales_APR.rename(columns={'sales':'APR','profit':'APR_profit'}, inplace=True)
all_sales_APR
all_sales_MAY=df[['pharmacy','sales','profit','sales_rep']][df['Month']=='MAY'].groupby(['pharmacy','sales_rep']).agg({"sales":sum,"profit":sum}).sort_values('sales',ascending=False)
all_sales_MAY.rename(columns={'sales':'MAY','profit':'MAY_profit'}, inplace=True)
all_sales_MAY
all_sales_JUN=df[['pharmacy','sales','profit','sales_rep']][df['Month']=='JUN'].groupby(['pharmacy','sales_rep']).agg({"sales":sum,"profit":sum}).sort_values('sales',ascending=False)
all_sales_JUN.rename(columns={'sales':'JUN','profit':'JUN_profit'}, inplace=True)
all_sales_JUN
all_sales_JUL=df[['pharmacy','sales','profit','sales_rep']][df['Month']=='JUL'].groupby(['pharmacy','sales_rep']).agg({"sales":sum,"profit":sum}).sort_values('sales',ascending=False)
all_sales_JUL.rename(columns={'sales':'JUL','profit':'JUL_profit'}, inplace=True)
all_sales_JUL
all_sales_AUG=df[['pharmacy','sales','profit','sales_rep']][df['Month']=='AUG'].groupby(['pharmacy','sales_rep']).agg({"sales":sum,"profit":sum}).sort_values('sales',ascending=False)
all_sales_AUG.rename(columns={'sales':'AUG','profit':'AUG_profit'}, inplace=True)
all_sales_AUG
all_sales_SEP=df[['pharmacy','sales','profit','sales_rep']][df['Month']=='SEP'].groupby(['pharmacy','sales_rep']).agg({"sales":sum,"profit":sum}).sort_values('sales',ascending=False)
all_sales_SEP.rename(columns={'sales':'SEP','profit':'SEP_profit'}, inplace=True)
all_sales_SEP
all_sales_OCT=df[['pharmacy','sales','profit','sales_rep']][df['Month']=='OCT'].groupby(['pharmacy','sales_rep']).agg({"sales":sum,"profit":sum}).sort_values('sales',ascending=False)
all_sales_OCT.rename(columns={'sales':'OCT','profit':'OCT_profit'}, inplace=True)
all_sales_OCT
all_sales_NOV=df[['pharmacy','sales','profit','sales_rep']][df['Month']=='NOV'].groupby(['pharmacy','sales_rep']).agg({"sales":sum,"profit":sum}).sort_values('sales',ascending=False)
all_sales_NOV.rename(columns={'sales':'NOV','profit':'NOV_profit'}, inplace=True)
all_sales_NOV
all_sales_DEC=df[['pharmacy','sales','profit','sales_rep']][df['Month']=='DEC'].groupby(['pharmacy','sales_rep']).agg({"sales":sum,"profit":sum}).sort_values('sales',ascending=False)
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
all_pharmacies_sales=all_sales[['pharmacy', 'sales_rep', 'JAN','FEB','MAR', 'APR', 'MAY','JUN','JUL','AUG','SEP','OCT','NOV','DEC','YTD']][all_sales['pharmacy'].str.startswith('ص')].groupby(['pharmacy'],as_index=False).agg({'YTD':sum,'JAN':sum,'FEB':sum,'MAR':sum,'APR':sum,'MAY':sum,'JUN':sum,'JUL':sum,'AUG':sum,'SEP':sum,'OCT':sum,'NOV':sum,'DEC':sum}).sort_values('YTD',ascending=False)
all_pharmacies_profit=all_sales[['pharmacy', 'sales_rep','JAN_profit','FEB_profit','MAR_profit','APR_profit','MAY_profit', 'JUN_profit','JUL_profit','AUG_profit','SEP_profit','OCT_profit','NOV_profit','DEC_profit', 'YTD_profit']][all_sales['pharmacy'].str.startswith('ص')].groupby(['pharmacy'],as_index=False).agg({'YTD_profit':sum,'JAN_profit':sum,'FEB_profit':sum,'MAR_profit':sum,'APR_profit':sum,'MAY_profit':sum,'JUN_profit':sum,'JUL_profit':sum,'AUG_profit':sum,'SEP_profit':sum,'OCT_profit':sum,'NOV_profit':sum,'DEC_profit':sum}).sort_values('YTD_profit',ascending=False)
all_pharmacies_profit.rename(columns={'JAN_profit':'JAN','FEB_profit':'FEB','MAR_profit':'MAR','APR_profit':'APR','MAY_profit':'MAY', 'JUN_profit':'JUN','JUL_profit':'JUL','AUG_profit':'AUG','SEP_profit':'SEP','OCT_profit':'OCT','NOV_profit':'NOV','DEC_profit':'DEC', 'YTD_profit':'YTD'},inplace=True)
sales_rep_JAN=df[['pharmacy','sales','profit','sales_rep']][df['Month']=='JAN'].groupby('sales_rep').agg({"sales":sum,"profit":sum}).sort_values('sales',ascending=False)
sales_rep_JAN.rename(columns={'sales':'JAN','profit':'JAN_profit'}, inplace=True)
sales_rep_JAN
sales_rep_FEB=df[['pharmacy','sales','profit','sales_rep']][df['Month']=='FEB'].groupby('sales_rep').agg({"sales":sum,"profit":sum}).sort_values('sales',ascending=False)
sales_rep_FEB.rename(columns={'sales':'FEB','profit':'FEB_profit'}, inplace=True)
sales_rep_FEB
sales_rep_MAR=df[['pharmacy','sales','profit','sales_rep']][df['Month']=='MAR'].groupby('sales_rep').agg({"sales":sum,"profit":sum}).sort_values('sales',ascending=False)
sales_rep_MAR.rename(columns={'sales':'MAR','profit':'MAR_profit'}, inplace=True)
sales_rep_MAR
sales_rep_APR=df[['pharmacy','sales','profit','sales_rep']][df['Month']=='APR'].groupby('sales_rep').agg({"sales":sum,"profit":sum}).sort_values('sales',ascending=False)
sales_rep_APR.rename(columns={'sales':'APR','profit':'APR_profit'}, inplace=True)
sales_rep_APR
sales_rep_MAY=df[['pharmacy','sales','profit','sales_rep']][df['Month']=='MAY'].groupby('sales_rep').agg({"sales":sum,"profit":sum}).sort_values('sales',ascending=False)
sales_rep_MAY.rename(columns={'sales':'MAY','profit':'MAY_profit'}, inplace=True)
sales_rep_MAY
sales_rep_JUN=df[['pharmacy','sales','profit','sales_rep']][df['Month']=='JUN'].groupby('sales_rep').agg({"sales":sum,"profit":sum}).sort_values('sales',ascending=False)
sales_rep_JUN.rename(columns={'sales':'JUN','profit':'JUN_profit'}, inplace=True)
sales_rep_JUN
sales_rep_JUL=df[['pharmacy','sales','profit','sales_rep']][df['Month']=='JUL'].groupby('sales_rep').agg({"sales":sum,"profit":sum}).sort_values('sales',ascending=False)
sales_rep_JUL.rename(columns={'sales':'JUL','profit':'JUL_profit'}, inplace=True)
sales_rep_JUL
sales_rep_AUG=df[['pharmacy','sales','profit','sales_rep']][df['Month']=='AUG'].groupby('sales_rep').agg({"sales":sum,"profit":sum}).sort_values('sales',ascending=False)
sales_rep_AUG.rename(columns={'sales':'AUG','profit':'AUG_profit'}, inplace=True)
sales_rep_AUG
sales_rep_SEP=df[['pharmacy','sales','profit','sales_rep']][df['Month']=='SEP'].groupby('sales_rep').agg({"sales":sum,"profit":sum}).sort_values('sales',ascending=False)
sales_rep_SEP.rename(columns={'sales':'SEP','profit':'SEP_profit'}, inplace=True)
sales_rep_SEP
sales_rep_OCT=df[['pharmacy','sales','profit','sales_rep']][df['Month']=='OCT'].groupby('sales_rep').agg({"sales":sum,"profit":sum}).sort_values('sales',ascending=False)
sales_rep_OCT.rename(columns={'sales':'OCT','profit':'OCT_profit'}, inplace=True)
sales_rep_OCT
sales_rep_NOV=df[['pharmacy','sales','profit','sales_rep']][df['Month']=='NOV'].groupby('sales_rep').agg({"sales":sum,"profit":sum}).sort_values('sales',ascending=False)
sales_rep_NOV.rename(columns={'sales':'NOV','profit':'NOV_profit'}, inplace=True)
sales_rep_NOV
sales_rep_DEC=df[['pharmacy','sales','profit','sales_rep']][df['Month']=='DEC'].groupby('sales_rep').agg({"sales":sum,"profit":sum}).sort_values('sales',ascending=False)
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
Area_rep_JAN=df[['pharmacy','sales','profit','sales_rep','Area_rep']][df['Month']=='JAN'].groupby('Area_rep').agg({"sales":sum,"profit":sum}).sort_values('sales',ascending=False)
Area_rep_JAN.rename(columns={'sales':'JAN','profit':'JAN_profit'}, inplace=True)
Area_rep_JAN
Area_rep_FEB=df[['pharmacy','sales','profit','sales_rep','Area_rep']][df['Month']=='FEB'].groupby('Area_rep').agg({"sales":sum,"profit":sum}).sort_values('sales',ascending=False)
Area_rep_FEB.rename(columns={'sales':'FEB','profit':'FEB_profit'}, inplace=True)
Area_rep_FEB
Area_rep_MAR=df[['pharmacy','sales','profit','sales_rep','Area_rep']][df['Month']=='MAR'].groupby('Area_rep').agg({"sales":sum,"profit":sum}).sort_values('sales',ascending=False)
Area_rep_MAR.rename(columns={'sales':'MAR','profit':'MAR_profit'}, inplace=True)
Area_rep_MAR
Area_rep_APR=df[['pharmacy','sales','profit','sales_rep','Area_rep']][df['Month']=='APR'].groupby('Area_rep').agg({"sales":sum,"profit":sum}).sort_values('sales',ascending=False)
Area_rep_APR.rename(columns={'sales':'APR','profit':'APR_profit'}, inplace=True)
Area_rep_APR
Area_rep_MAY=df[['pharmacy','sales','profit','sales_rep','Area_rep']][df['Month']=='MAY'].groupby('Area_rep').agg({"sales":sum,"profit":sum}).sort_values('sales',ascending=False)
Area_rep_MAY.rename(columns={'sales':'MAY','profit':'MAY_profit'}, inplace=True)
Area_rep_MAY
Area_rep_JUN=df[['pharmacy','sales','profit','sales_rep','Area_rep']][df['Month']=='JUN'].groupby('Area_rep').agg({"sales":sum,"profit":sum}).sort_values('sales',ascending=False)
Area_rep_JUN.rename(columns={'sales':'JUN','profit':'JUN_profit'}, inplace=True)
Area_rep_JUN
Area_rep_JUL=df[['pharmacy','sales','profit','sales_rep','Area_rep']][df['Month']=='JUL'].groupby('Area_rep').agg({"sales":sum,"profit":sum}).sort_values('sales',ascending=False)
Area_rep_JUL.rename(columns={'sales':'JUL','profit':'JUL_profit'}, inplace=True)
Area_rep_JUL
Area_rep_AUG=df[['pharmacy','sales','profit','sales_rep','Area_rep']][df['Month']=='AUG'].groupby('Area_rep').agg({"sales":sum,"profit":sum}).sort_values('sales',ascending=False)
Area_rep_AUG.rename(columns={'sales':'AUG','profit':'AUG_profit'}, inplace=True)
Area_rep_AUG
Area_rep_SEP=df[['pharmacy','sales','profit','sales_rep','Area_rep']][df['Month']=='SEP'].groupby('Area_rep').agg({"sales":sum,"profit":sum}).sort_values('sales',ascending=False)
Area_rep_SEP.rename(columns={'sales':'SEP','profit':'SEP_profit'}, inplace=True)
Area_rep_SEP
Area_rep_OCT=df[['pharmacy','sales','profit','sales_rep','Area_rep']][df['Month']=='OCT'].groupby('Area_rep').agg({"sales":sum,"profit":sum}).sort_values('sales',ascending=False)
Area_rep_OCT.rename(columns={'sales':'OCT','profit':'OCT_profit'}, inplace=True)
Area_rep_OCT
Area_rep_NOV=df[['pharmacy','sales','profit','sales_rep','Area_rep']][df['Month']=='NOV'].groupby('Area_rep').agg({"sales":sum,"profit":sum}).sort_values('sales',ascending=False)
Area_rep_NOV.rename(columns={'sales':'NOV','profit':'NOV_profit'}, inplace=True)
Area_rep_NOV
Area_rep_DEC=df[['pharmacy','sales','profit','sales_rep','Area_rep']][df['Month']=='DEC'].groupby('Area_rep').agg({"sales":sum,"profit":sum}).sort_values('sales',ascending=False)
Area_rep_DEC.rename(columns={'sales':'DEC','profit':'DEC_profit'}, inplace=True)
Area_rep_DEC
Area_rep_YTD=df[['pharmacy','sales','profit','sales_rep','Area_rep']].groupby('Area_rep').agg({"sales":sum,"profit":sum}).sort_values('sales',ascending=False)
Area_rep_YTD.rename(columns={'sales':'YTD','profit':'YTD_profit'}, inplace=True)
Area_rep_YTD
Area_rep_sales=Area_rep_YTD.join(Area_rep_JAN).join(Area_rep_FEB).join(Area_rep_MAR).join(Area_rep_APR).join(Area_rep_MAY).join(Area_rep_JUN).join(Area_rep_JUL).join(Area_rep_AUG).join(Area_rep_SEP).join(Area_rep_OCT).join(Area_rep_NOV).join(Area_rep_DEC)
Area_rep_sales.fillna(0,inplace=True)
Area_rep_sales.sort_values('YTD',ascending=False,inplace=True)
Area_rep_sales.drop(axis=0,index=['Alexandria / ISLAM','Matrouh / ISLAM','GOMLA / others','GOMLA / SHIMAA','GOMLA / AYA'],inplace=True)
Area_rep_sales.reset_index(inplace=True)
Area_rep_profit=Area_rep_sales[['Area_rep','YTD_profit','JAN_profit','FEB_profit','MAR_profit','APR_profit','MAY_profit', 'JUN_profit','JUL_profit','AUG_profit','SEP_profit','OCT_profit','NOV_profit','DEC_profit']].sort_values('YTD_profit',ascending=False)
Area_rep_profit.rename(columns={'JAN_profit':'JAN','FEB_profit':'FEB','MAR_profit':'MAR','APR_profit':'APR','MAY_profit':'MAY', 'JUN_profit':'JUN','JUL_profit':'JUL','AUG_profit':'AUG','SEP_profit':'SEP','OCT_profit':'OCT','NOV_profit':'NOV','DEC_profit':'DEC', 'YTD_profit':'YTD'},inplace=True)
Area_rep_sales.drop(axis=1,columns=['YTD_profit','JAN_profit','FEB_profit','MAR_profit','APR_profit','MAY_profit', 'JUN_profit','JUL_profit','AUG_profit','SEP_profit','OCT_profit','NOV_profit','DEC_profit'],inplace=True)
Area_JAN=df[['pharmacy','sales','profit','sales_rep','Area']][df['Month']=='JAN'].groupby('Area').agg({"sales":sum,"profit":sum}).sort_values('sales',ascending=False)
Area_JAN.rename(columns={'sales':'JAN','profit':'JAN_profit'}, inplace=True)
Area_JAN
Area_FEB=df[['pharmacy','sales','profit','sales_rep','Area']][df['Month']=='FEB'].groupby('Area').agg({"sales":sum,"profit":sum}).sort_values('sales',ascending=False)
Area_FEB.rename(columns={'sales':'FEB','profit':'FEB_profit'}, inplace=True)
Area_FEB
Area_MAR=df[['pharmacy','sales','profit','sales_rep','Area']][df['Month']=='MAR'].groupby('Area').agg({"sales":sum,"profit":sum}).sort_values('sales',ascending=False)
Area_MAR.rename(columns={'sales':'MAR','profit':'MAR_profit'}, inplace=True)
Area_MAR
Area_APR=df[['pharmacy','sales','profit','sales_rep','Area']][df['Month']=='APR'].groupby('Area').agg({"sales":sum,"profit":sum}).sort_values('sales',ascending=False)
Area_APR.rename(columns={'sales':'APR','profit':'APR_profit'}, inplace=True)
Area_rep_APR
Area_MAY=df[['pharmacy','sales','profit','sales_rep','Area']][df['Month']=='MAY'].groupby('Area').agg({"sales":sum,"profit":sum}).sort_values('sales',ascending=False)
Area_MAY.rename(columns={'sales':'MAY','profit':'MAY_profit'}, inplace=True)
Area_MAY
Area_JUN=df[['pharmacy','sales','profit','sales_rep','Area']][df['Month']=='JUN'].groupby('Area').agg({"sales":sum,"profit":sum}).sort_values('sales',ascending=False)
Area_JUN.rename(columns={'sales':'JUN','profit':'JUN_profit'}, inplace=True)
Area_JUN
Area_JUL=df[['pharmacy','sales','profit','sales_rep','Area']][df['Month']=='JUL'].groupby('Area').agg({"sales":sum,"profit":sum}).sort_values('sales',ascending=False)
Area_JUL.rename(columns={'sales':'JUL','profit':'JUL_profit'}, inplace=True)
Area_JUL
Area_AUG=df[['pharmacy','sales','profit','sales_rep','Area']][df['Month']=='AUG'].groupby('Area').agg({"sales":sum,"profit":sum}).sort_values('sales',ascending=False)
Area_AUG.rename(columns={'sales':'AUG','profit':'AUG_profit'}, inplace=True)
Area_AUG
Area_SEP=df[['pharmacy','sales','profit','sales_rep','Area']][df['Month']=='SEP'].groupby('Area').agg({"sales":sum,"profit":sum}).sort_values('sales',ascending=False)
Area_SEP.rename(columns={'sales':'SEP','profit':'SEP_profit'}, inplace=True)
Area_SEP
Area_OCT=df[['pharmacy','sales','profit','sales_rep','Area']][df['Month']=='OCT'].groupby('Area').agg({"sales":sum,"profit":sum}).sort_values('sales',ascending=False)
Area_OCT.rename(columns={'sales':'OCT','profit':'OCT_profit'}, inplace=True)
Area_OCT
Area_NOV=df[['pharmacy','sales','profit','sales_rep','Area']][df['Month']=='NOV'].groupby('Area').agg({"sales":sum,"profit":sum}).sort_values('sales',ascending=False)
Area_NOV.rename(columns={'sales':'NOV','profit':'NOV_profit'}, inplace=True)
Area_NOV
Area_DEC=df[['pharmacy','sales','profit','sales_rep','Area']][df['Month']=='DEC'].groupby('Area').agg({"sales":sum,"profit":sum}).sort_values('sales',ascending=False)
Area_DEC.rename(columns={'sales':'DEC','profit':'DEC_profit'}, inplace=True)
Area_DEC
Area_YTD=df[['pharmacy','sales','profit','sales_rep','Area']].groupby('Area').agg({"sales":sum,"profit":sum}).sort_values('sales',ascending=False)
Area_YTD.rename(columns={'sales':'YTD','profit':'YTD_profit'}, inplace=True)
Area_YTD
Area_sales=Area_YTD.join(Area_JAN).join(Area_FEB).join(Area_MAR).join(Area_APR).join(Area_MAY).join(Area_JUN).join(Area_JUL).join(Area_AUG).join(Area_SEP).join(Area_OCT).join(Area_NOV).join(Area_DEC)
Area_sales.fillna(0,inplace=True)
Area_sales.sort_values('YTD',ascending=False,inplace=True)
Area_sales.loc['Total_pharmacy']=Area_sales.loc['Alexandria']+Area_sales.loc['Behira']+Area_sales.loc['Matrouh']
Area_sales.loc['Global_sales']=Area_sales.loc['Alexandria']+Area_sales.loc['Behira']+Area_sales.loc['Matrouh']+Area_sales.loc['GOMLA']
Area_sales.reset_index(inplace=True)
Area_profit=Area_sales[['Area','YTD_profit','JAN_profit','FEB_profit','MAR_profit','APR_profit','MAY_profit', 'JUN_profit','JUL_profit','AUG_profit','SEP_profit','OCT_profit','NOV_profit','DEC_profit']].sort_values('YTD_profit',ascending=False)
Area_profit.rename(columns={'JAN_profit':'JAN','FEB_profit':'FEB','MAR_profit':'MAR','APR_profit':'APR','MAY_profit':'MAY', 'JUN_profit':'JUN','JUL_profit':'JUL','AUG_profit':'AUG','SEP_profit':'SEP','OCT_profit':'OCT','NOV_profit':'NOV','DEC_profit':'DEC', 'YTD_profit':'YTD'},inplace=True)
Area_sales.drop(axis=1,columns=['JAN_profit','FEB_profit','MAR_profit','APR_profit','MAY_profit', 'JUN_profit','JUL_profit','AUG_profit','SEP_profit','OCT_profit','NOV_profit','DEC_profit', 'YTD_profit'],inplace=True)
Area_rep_sales.set_index('Area_rep',inplace=True)
Area_rep_profit.set_index('Area_rep',inplace=True)
Area_sales.set_index('Area',inplace=True)
Area_profit.set_index('Area',inplace=True)
sales_rep_sales.set_index('sales_rep',inplace=True)
sales_rep_profit.set_index('sales_rep',inplace=True) 
all_pharmacies_sales.set_index('pharmacy',inplace=True)
PHARMACY=all_pharmacies_sales.index
for i in PHARMACY:
    pharmacy= i
    print(pharmacy)
# Create a dash application
from dash import Output
from dash.dash import Input
app = dash.Dash(__name__)
server=app.server
# Build dash app layout
app.layout = html.Div(children=[ html.H1('2024 Sales Statistics Dashboard', 
                                style={'textAlign': 'center', 'color': '#503D36',
                                'font-size': 35}),
                                
                                html.Div([
                                        html.Div(["Area:",dcc.Dropdown(AREA,id='area', value='Global_sales', 
                                style={'height':'35px','width':'700px', 'font-size': 20})]),
                                        html.Div(["Pharmacy:"  ,dcc.Dropdown(PHARMACY,id='pharmacy',value='ص المعسكر الروماني/شهري',
                                style={'height':'35px','width':'700px', 'font-size': 20})]),  
                                                                                                    
                                ],style={'font-size': 25,'display': 'flex'}),
                                html.Div([
                                        html.Div(["Sales rep:",dcc.Dropdown(Sales_representative,id='sales_rep', value='SHIMAA', 
                                style={'height':'35px','width':'500px', 'font-size': 20})]),
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
                                ], style={'font-size': 25,'display': 'flex'}),
                                # Segment 4
                                        html.Div([
                                        html.Div(dcc.Graph(id='all_pharmacies_curve1'))
                                ], style={'font-size': 25,'width':'1400px'}),
                                
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
               Output(component_id='area_rep_curve2', component_property='figure'),
               Output(component_id='all_pharmacies_curve1', component_property='figure')
            ],
               [Input(component_id='area', component_property='value'),
                Input(component_id='pharmacy', component_property='value'),
                Input(component_id='sales_rep', component_property='value'),
                Input(component_id='month', component_property='value')],
                Input(component_id='area_rep', component_property='value'))
# Computation to callback function and return graph
def update_output(area,pharmacy,sales_rep,month,area_rep): 
    area_curve1=px.bar(Area_sales,y=month,color=month,title =  'Sales per Area in selected month',text_auto=True)
    area_curve2=px.bar(Area_sales.loc[area],color=ALL_YEAR,title =  'Sales in selected Area',text_auto=True)
    sales_rep_curve1=px.bar(sales_rep_sales,y=month,color=month,title = 'Sales per rep in selected month',text_auto=True)
    sales_rep_curve2=px.bar(sales_rep_sales.loc[sales_rep],color=ALL_YEAR,title = 'Sales  in 2024 by specific sales rep',text_auto=True)
    area_rep_curve1=px.bar(Area_rep_sales,y=month,color=month,text_auto=True,title= 'Sales of rep per area in selected month')
    area_rep_curve2=px.bar(Area_rep_sales.loc[area_rep],color=ALL_YEAR,text_auto=True,title= 'Sales of specific rep in specific area')
    all_pharmacies_curve1=px.bar(all_pharmacies_sales.loc[pharmacy],text_auto=True,color=ALL_YEAR,title='Sales of pharmacy in 2024')
    return[area_curve1,area_curve2,sales_rep_curve1,sales_rep_curve2,area_rep_curve1,area_rep_curve2,all_pharmacies_curve1]
#urllib.request.urlopen('http://127.0.0.1:8060/',verify=False)
#response = requests.get("http://127.0.0.1:8060/",verify=False) 
# Run the application
#port=8060
#def open_browser() :
    #webbrowser.open_new("http://localhost:{}".format(port))                 
if __name__ == '__main__':
    #Timer(1,open_browser).start();
    app.run_server()    
   

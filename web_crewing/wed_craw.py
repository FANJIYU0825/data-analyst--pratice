#爬取大陸國家假統計肺炎網站(扣除台灣/香港/澳門)
import requests as res
from bs4 import BeautifulSoup
import pandas as pd
import numpy as np 
from tqdm import tqdm 
url = 'http://ncov.dxy.cn/ncovh5/view/pneumonia'
response = res.get(url) # text 屬性就是 html 檔案
response.encoding = 'utf-8'
soup = BeautifulSoup(response.text, "lxml") # 指定 lxml 作為解析器
get_area = soup.find(id="getAreaStat")
area_text = get_area.text
area_catreplace = area_text.replace('}catch(e){}','') #replace 多餘的文字
area_json = area_catreplace.replace('try { window.getAreaStat = ','')#replace 多於文字

##area_json 是一個字串(str) 把字串轉化(list) 
import json
area_json = json.loads(area_json)
provinceName = []
for area_select in area_json:
    if area_select['provinceName'] !='香港':
      if area_select['provinceName'] !='台湾':
        if area_select['provinceName'] !='澳门':
          provinceName.append(area_select)
## 當日以及 所天數檔案的`json`{statisticsData}	
today_df = pd.DataFrame(provinceName)
today_df.head(1)
provinceName        

all_data_url = today_df.loc[:,['provinceName','statisticsData']]
all_data_url[0]


to_names =[]
to_prevname = []
with tqdm(total = len(all_data_url) ) as pbar:
  for x in range (len(all_data_url)) :
    df = pd.read_json(all_data_url['statisticsData'][x])
    provinceName = all_data_url['provinceName'][x]
    df[f'{provinceName}'] =provinceName
    df = df.loc[:,[f'{provinceName}','data']]
    df_n= df.loc[:,[f'{provinceName}']]
    df_n['dateId']= [x['dateId']
                      for x in df['data']]
    df_n['confirmedCount']= [x['confirmedCount']
                      for x in df['data']]
    df_n['confirmedCount']= [x['confirmedCount']
                      for x in df['data']]
    df_n['curedCount']= [x['curedCount']
                      for x in df['data']]
    df_n['deadCount']= [x['deadCount']
                      for x in df['data']]
    #時間處理程序 
df_n['dateId']= pd.to_datetime(df_n['dateId'], format='%Y%m%d', errors='ignore')
to_names.append(df_n)
pbar.update()

df_convir= pd.concat(to_names,axis=1,join='inner')
df_convir.head(1)


data =[]
province_ls= []
with tqdm(total = len(df_info) ) as pbar:
  for x in range (len(df_info)) :
    df = pd.read_json(df_info['statisticsData'][x])
    provinceName = df_info['provinceName'][x]
    df['provincenae'] =provinceName
    df = df.loc[:,['provincenae','data']]
    province_ls.append(provinceName)
    data.append(df)
    pbar.update()

to_csv = []
to_name = []
with tqdm(total = len(data) ) as pbar:
  for x in data:
    for xs in x['data']:
      
      to_csv.append({'dateId':xs['dateId'],
          'confirmedCount':xs['confirmedCount'],
          'curedCount':xs['curedCount'],
          'deadCount':xs['deadCount']})
      pbar.update()


with tqdm(total = len(data) ) as pbar:
  for x in data:
    for xs in x['provincenae']:
      
      to_name.append({'provinceName':xs})
      pbar.update()


df_csv = pd.DataFrame(to_csv)
df_name = pd.DataFrame(to_name)
df_all= pd.concat([df_name,df_csv],axis=1)
df_all['dateId']= pd.to_datetime(df_all['dateId'], format='%Y%m%d', errors='ignore')

df_all.to_csv('/content/drive/My Drive/PAPER/df_all.csv')

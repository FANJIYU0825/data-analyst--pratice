import pandas as pd
import numpy as np

"""
data
"""
df_a = pd.read_csv('./openpublic/data/a_lvr_land_a.csv',encoding ='utf-8')
df_a = df_a.drop([0,0])
df_b = pd.read_csv('./openpublic/data/b_lvr_land_a.csv',encoding ='utf-8')
df_b = df_b.drop([0,0])
df_e = pd.read_csv('./openpublic/data/e_lvr_land_a.csv',encoding ='utf-8')
df_e = df_e.drop([0,0])
df_f = pd.read_csv('./openpublic/data/f_lvr_land_a.csv',encoding ='utf-8')
df_f = df_f.drop([0,0])
df_h = pd.read_csv('./openpublic/data/h_lvr_land_a.csv',encoding ='utf-8')
df_h = df_h.drop([0,0])

#dataf_Mix
df_all = pd.concat([df_a,df_b,df_e,df_f,df_h],axis = 0)
'''
function
'''
#處理樓層數中中文數字轉英文數字
def trans(s):
    digit = {'一': 1, '二': 2, '三': 3, '四': 4, '五': 5, '六': 6, '七': 7, '八': 8, '九': 9}
    num = 0
    if type(s) == str:
        idx_b, idx_s =  s.find('百'), s.find('十')
        
        if idx_b != -1:
            num += digit[s[idx_b - 1:idx_b]] * 100
        if idx_s != -1:
            # 當判斷10 忽略1
            num += digit.get(s[idx_s - 1:idx_s], 1) * 10
        if s[-1] in digit:
            num += digit[s[-1]]

        return num       

#去除'層'字
df_all['總樓層數'] = df_all['總樓層數'].str.replace("層","")
#套入國字轉數字fuc apply
df_all['總樓層數'] = df_all['總樓層數'].apply(trans)

'''
data sort
'''
#條件：filter_a,篩選並輸出csv檔
condition_1 = df_all['主要用途']=='住家用'
condition_2 = df_all['建物型態'].str.contains('住宅大樓')
condition_3 = df_all['總樓層數']>=13
filter_a = df_all[(condition_1 & condition_2 & condition_3)]
# filter_a.to_csv('filter_a.csv',encoding ='UTF-8')



#條件：filter_b,篩選並輸出csv檔
total_mount = len(df_all)
#交易筆棟數格式為：土地1建物1車位2，從'車位'一詞分割出車位數，再進行加總
total_berth_mount = df_all['交易筆棟數'].str.split('車位',expand=True)[1].astype('int64').sum()
avg_price = df_all['總價元'].astype('int64').mean()
avg_berth_price = df_all['車位總價元'].astype('int64').mean()

info_dict ={
    '總件數':total_mount,
    '總車位數':total_berth_mount,
    '平均總價元':avg_price,
    '平均車位總價元':avg_berth_price
}
print(info_dict)
# pd.Series(info_dict).to_csv('filter_b.csv',encoding ='UTF-8')
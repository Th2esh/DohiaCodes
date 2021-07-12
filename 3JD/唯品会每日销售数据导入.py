import pandas as pd
import datetime
import pymysql
import logging
import os
import xlrd
import openpyxl

#连接数据库
db = pymysql.connect(host='192.168.20.12', user='ych', password='123456', database='qudao_sale', port=3306,
                     charset='utf8')
cur = db.cursor()

#读入数据表
df = pd.read_excel('wph.xlsx')
pd.set_option('display.max_columns',10)
df = df[['商品名称','条形码','日期','销售量（不含拒退）','实收金额（不含拒退）']]
df_wph = pd.read_excel('唯品会条码货号对照表.xlsx',sheet_name = '全部产品明细')
df_wph = df_wph[['商品条形码','商品货号']]
df_kc = pd.read_excel('库存统计.xlsx',sheet_name = '库存统计',header = 1)
df_kc = df_kc[['13位条形码','产品货号']]

#重命名字段名
df.rename(columns = {'商品名称':'mc','条形码':'txm','日期':'rq','销售量（不含拒退）':'sl','实收金额（不含拒退）':'je'},inplace = True)
df_wph.rename(columns = {'商品条形码':'txm','商品货号':'hh'},inplace = True)
df_kc.rename(columns = {'13位条形码':'txm','产品货号':'hh'},inplace = True)

#将txm,hh字段改为字符串格式
def num(a):
    if a == a:
        return int(a)
    else:
        return 0
df['txm'] = df['txm'].apply(num)
df['txm'] = df['txm'].apply(lambda x: str(x))
df_wph['txm'] = df_wph['txm'].apply(lambda x: str(x))
df_wph['hh'] = df_wph['hh'].apply(lambda x: str(x))
df_kc['txm'] = df_kc['txm'].apply(num)
df_kc['txm'] = df_kc['txm'].apply(lambda x: str(x))
df_kc['hh'] = df_kc['hh'].apply(lambda x: str(x))

#将库存表和条码对照表合并
df1 = pd.concat([df_wph,df_kc],ignore_index=True).drop_duplicates()

#匹配货号列
df = pd.merge(df,df1,how = 'left',on = 'txm')

#新增一个店铺列
df['dp'] = '唯品会'

#调整字段的位置
cols = list(df)
cols.insert(0,cols.pop(cols.index('dp')))
cols.insert(3,cols.pop(cols.index('hh')))
df = df.loc[:,cols]

#除去不必要的行
df = df[~df['txm'].isin(['0'])]

df = df.astype(object).where(pd.notnull(df), None)
df.to_excel(r"Z:\IT部\个人文件\燕江洪\※每日销售数据\唯品会\唯品会"+df['rq'][0]+".xlsx",index = False)

#将数据导入数据库
columns = ','.join(list(df.columns))
data_list = [tuple(i) for i in df.values]
s_count = len(data_list[0]) * '%s,'

with db.cursor() as cursor:
    try:
        sql = "insert into wph_sale("+columns+") value("+s_count[:-1]+")"
        cursor.executemany(sql,data_list)
        db.commit()
    except:
        logging.exception('exception')
        db.rollback()
db.close()
os._exit(0)





























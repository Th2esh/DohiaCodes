# -*- code=utf-8 -*-
import requests
import json
import hashlib
import time
import pandas as pd
import os

def hsmd(secert):
    str = secert
    m = hashlib.md5()
    b = str.encode(encoding='utf-8')
    m.update(b)
    str_md5 = m.hexdigest()
    return str_md5

def ckycd(content):
    # 单据编号的变量值
    dj_random = str(time.strftime("%Y%m%d%H%M", time.localtime()))
    # 时间参数
    rt = str(time.strftime("%Y%m%d%H%M%S", time.localtime()))
    # 接口类型
    jk = 'ckycd.add'
    # json数据
    js_data = '{'+str(content)+'}'

    dqm_data = "key=test&requestTime="+rt+"&secret=1a2b3c4d5e6f7g8h9i10j11k12l&version=3.0&serviceType="+jk+"&data" \
                                                                                                            "="+js_data
    sign_data = hsmd(dqm_data)
    # return js_data


    url = "http://39.100.94.96/e3/webopm/web/?app_act=api/ec&app_mode=func"

    params = {
        'key' : 'test',
        'sign' : sign_data,
        'requestTime' : rt,
        'version' : '3.0',
        'serviceType' : jk,
        'data' : js_data
    }
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                      'Chrome/81.0.4044.122 Safari/537.36',
    }
    response = requests.get(url=url, params=params, headers=headers)
    data = json.loads(response.text)
    return data

def app_ckycd(ycck,yrck):
    df = pd.read_excel('ycd.xlsx')
    sku_list = []
    for i in range(len(df['SKU'].to_list())):
        sku_list.append('{"sku":"'+str(df['SKU'].to_list()[i])+'","dj":"1.00","sl":"'+str(df['SL'].to_list()[i])+'"}')
    sku_list_str = str(sku_list).replace("'","")

    rts = str(time.strftime("%Y%m%d%H%M%S", time.localtime()))
    yycs = '"djbh":"qhycrw'+str(rts)+'","warehouseCode":"'+str(ycck)+'","warehouseCodeIn":"'+str(yrck)+'",' \
                                     '"sku":'+str(sku_list_str)+''
    return  print(ckycd(yycs))




if __name__ == '__main__':

    print(
          "##欢迎使用移仓工具请查看列表##\n"
          "\n"
          "1.月罗成品仓-临时仓\n"
          "2.临时仓-月罗成品仓\n"
          "3.南通成品仓-冻结仓\n"
          "4.冻结仓-南通成品仓\n"
          )

    cc = input("输入代码:")

    if cc == str(1):
        ycck = '310010'
        yrck = '310031'
        app_ckycd(ycck,yrck)
    elif cc == str(2):
        ycck = '310031'
        yrck = '310010'
        app_ckycd(ycck, yrck)
    elif cc == str(3):
        ycck = '400022'
        yrck = '400021'
        app_ckycd(ycck, yrck)
    elif cc == str(4):
        ycck = '400021'
        yrck = '400022'
        app_ckycd(ycck, yrck)
    else:
        print('代码错误，程序退出')
        os._exit(0)









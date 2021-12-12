#-*- coding:utf-8 -*-
import requests
import json
import pandas as pd
import datetime

import time

def myinterface(zl,sp):
    url = "http://39.100.94.96/e3/dohia/interfaces/updatewg1.php"
    params = {
        "sp":sp,
        "zl":zl
    }
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                      'Chrome/81.0.4044.122 Safari/537.36',
    }
    response = requests.get(url=url, params=params, headers=headers)
    # data = json.loads(response.text, encoding='utf-8')
    # return data






if __name__=='__main__':
    # df = pd.read_excel("1.xlsx", sheet_name="Sheet1")
    # zl = []
    # sp = []
    # a = df['sku'].to_list()
    # for i in a:
    #     sp.append(str(i))
    # b = df['zl'].to_list()
    # for m in b:
    #     zl.append(str(m))
    # for j in range (len(sp)):
    #     # print(df['zl'].to_list()[j]+df['sku'].to_list()[j])
    #     # print(sp+zl)
    #     print(sp[j],zl[j])
    sp = '114021315560520'
    zl = '10'
    print(myinterface(zl,sp))
        # time.sleep(6)




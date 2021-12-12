# -*- coding:utf-8 -*-

import hmac
import requests
import json
import hashlib
import time
import pandas as pd

# 此函数在本接口中无效 系MD5加密 用于百胜接口
def hsmd(secert):
    str = secert
    m = hashlib.md5()
    b = str.encode(encoding='utf-8')
    m.update(b)
    str_md5 = m.hexdigest()
    return str_md5

# 此函数为HMAC-MD5加密方式
def hmac_md5(key, value):
    message = value.encode('utf-8')
    return hmac.new(key.encode('utf-8'), message, digestmod=hashlib.md5).hexdigest()



def wph_kcgx(contents):
    # 服务名
    service = 'vipapis.inventory.InventoryService'
    # 方法名
    method = 'updateInventory'
    # 版本
    version = '1.0.0'
    # 时间参数
    # timestamp = str(time.strftime("%Y%m%d%H%M%S", time.localtime()))
    timestamp = int(time.time())
    # timestamp = '1633941962'
    # 类型
    format = 'json'
    # key
    appKey = 'e79ed1c1'
    # secret
    appSecret = '42980F87296326370A34563DA67B28AA'
    accessToken = 'B569E6BE58AEC06CEB248B836DACAECDAF3D025F'
    # 请求变量 从形参传入 ...



    # dqm_data = "appKey"+str(appKey)+"format"+str(format)+"method"+str(method)+"service"+str(service)+"timestamp"+str(
    #     timestamp)+"version"+str(version)+str(contents)

    dqm_data = "accessToken"+str(accessToken)+"appKey"+str(appKey)+"format"+str(format)+"method"+str(method)+"service"+str(
        service)+"timestamp"+str(
        timestamp)+"version"+str(version)+str(contents)

    sign_data = hmac_md5(appSecret, dqm_data).upper()
    # return sign_data

    # url = "https://vop.vipapis.com/?service="+str(service)+"&method="+str(method)+"&version="+str(version)+"" \
    #       "&timestamp="+str(timestamp)+"&format="+str(format)+"&appKey="+str(appKey)+"&sign="+str(sign_data)

    url = "https://vop.vipapis.com/?service="+str(service)+"&method="+str(method)+"&version="+str(version)+"" \
          "&timestamp="+str(timestamp)+"&format="+str(format)+"&appKey="+str(appKey)+"&sign="+str(
        sign_data)+"&accessToken="+str(accessToken)

    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                      'Chrome/81.0.4044.122 Safari/537.36',
    }

    # POST用法，url直接传str_query所以前面的url有用?&直接增加url传参，data传递post表格信息即应用请求

    response = requests.post(url=url, data=contents, headers=headers)
    data_re = json.loads(response.text)
    return data_re



def wph_kccx(contents):
    # 服务名
    service = 'vipapis.inventory.InventoryService'
    # 方法名
    method = 'getSkuStock'
    # 版本
    version = '1.0.0'
    # 时间参数
    # timestamp = str(time.strftime("%Y%m%d%H%M%S", time.localtime()))
    timestamp = int(time.time())
    # timestamp = '1633941962'
    # 类型
    format = 'json'
    # key
    appKey = 'e79ed1c1'
    # secret
    appSecret = '42980F87296326370A34563DA67B28AA'
    accessToken = 'B569E6BE58AEC06CEB248B836DACAECDAF3D025F'
    # 请求变量 从形参传入 ...



    # dqm_data = "appKey"+str(appKey)+"format"+str(format)+"method"+str(method)+"service"+str(service)+"timestamp"+str(
    #     timestamp)+"version"+str(version)+str(contents)

    dqm_data = "accessToken"+str(accessToken)+"appKey"+str(appKey)+"format"+str(format)+"method"+str(method)+"service"+str(
        service)+"timestamp"+str(
        timestamp)+"version"+str(version)+str(contents)

    sign_data = hmac_md5(appSecret, dqm_data).upper()
    # return sign_data

    # url = "https://vop.vipapis.com/?service="+str(service)+"&method="+str(method)+"&version="+str(version)+"" \
    #       "&timestamp="+str(timestamp)+"&format="+str(format)+"&appKey="+str(appKey)+"&sign="+str(sign_data)

    url = "https://vop.vipapis.com/?service="+str(service)+"&method="+str(method)+"&version="+str(version)+"" \
          "&timestamp="+str(timestamp)+"&format="+str(format)+"&appKey="+str(appKey)+"&sign="+str(
        sign_data)+"&accessToken="+str(accessToken)

    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                      'Chrome/81.0.4044.122 Safari/537.36',
    }

    # POST用法，url直接传str_query所以前面的url有用?&直接增加url传参，data传递post表格信息即应用请求

    response = requests.post(url=url, data=contents, headers=headers)
    data_re = json.loads(response.text)
    return data_re

df = pd.read_excel("wph.xlsx", sheet_name="Sheet1")
temp = []
# # print(
# #     wph_kcgx('{"request":{"vendor_id":"8394","cooperation_no":"30008042","barcode":"6959253597963","quantity":"0",'
# #              '"batch_no":"'+str(int(time.time()))+'"}}'))
a = df['69码'].to_list()
#
# for i in a :
#
#     print(
#         wph_kcgx('{"request":{"vendor_id":"8394","cooperation_no":"30008042","barcode":"'+str(i)+'","quantity":"0",'
#                  '"batch_no":"'+str(int(time.time()))+'"}}')
#     )
#     time.sleep(1)
for i in a :
    print(
    wph_kccx('{"vendor_id":"8394","barcode":"' + str(i) + '","cooperation_no":"30008042"}')['result'][0]['leaving_stock']
    )
# print(
# wph_kccx('{"vendor_id":"8394","barcode":"6959253519422","cooperation_no":"30008042"}')['result'][0]['leaving_stock']
# )


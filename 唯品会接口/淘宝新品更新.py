# -*- coding:utf-8 -*-
# 同意中文解析

# 引入文件
import time
import hashlib
import requests
import json
import xmltodict
import pandas as pd


# 函数部分
# MD5加密
def hsmd(secert):
    str = secert
    m = hashlib.md5()
    b = str.encode(encoding='utf-8')
    m.update(b)
    str_md5 = m.hexdigest()
    return str_md5



# 转换数据格式 XML-JSON
def xmlstr2jsonstr(xmlstr):
    xmlparse = xmltodict.parse(xmlstr)
    jsonstr = json.dumps(xmlparse,indent=1,ensure_ascii=False)
    return jsonstr



# 接口函数
def tbicp():

    #系统请求参数
    method = 'tmall.brand.item.upload'
    # noinspection PyUnusedLocal
    app_key = '23036663'
    # noinspection PyUnusedLocal
    sign_method = 'md5'
    timestamp = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(time.time()))
    # noinspection PyUnusedLocal
    v = '2.0'
    #应用请求参数
    item_list = '{"brand_name":"多喜爱旗舰店","channel":"OFFLINE_SHOP","channel_publish_time":"2021-10-20 00:00:00","tmall_same":"true","item_id":"657089889925","item_name":"福克斯","brand_id":"80884","channel_publish_area":"ALL"}'

    #签名附加值
    secret = '300ca3f62e9051bfbcf4550dcd98b8f1'



#待签名字符串
    # dqm_str = 'app_key23036663item_list'+str(item_list)+'methodtmall.brand.item.uploadsession6100702294147e841d7715eb8a2b55033caa6e780b31a34114141735sign_methodmd5timestamp'+str(timestamp)+'v2.0'



    dqm_str = 'app_key23036663item_list'+str(item_list)+'methodtmall.brand.item.uploadsession6100702294147e841d7715eb8a2b55033caa6e780b31a34114141735sign_methodmd5timestamp'+str(timestamp)+'v2.0'
    print(dqm_str)



    sign_str = hsmd(str(secret)+str(dqm_str)+str(secret)).upper()
    # return  sign_str
    print(sign_str)


    ### Up Data has set Sign_string ###
    ### Down having POST method Data ###


    url = "http://gw.api.taobao.com/router/rest?app_key=23036663&sign="+str(
        sign_str)+"&method="+str(method)+"&session=6100702294147e841d7715eb8a2b55033caa6e780b31a34114141735&sign_method=md5" \
                              "&timestamp="+str(
        timestamp)+"&v=2.0&item_list="'{"brand_name":"多喜爱旗舰店","channel":"OFFLINE_SHOP","channel_publish_time":"2021-10-20 00:00:00","tmall_same":"true","item_id":"657089889925","item_name":"福克斯","brand_id":"80884","channel_publish_area":"ALL"}'

    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                      'Chrome/81.0.4044.122 Safari/537.36',
        'Content-Type': 'application/json;charset=utf-8'
    }

    # response = requests.post(url=url, data=body, headers=headers)
    response = requests.post(url=url, headers=headers)
    # data = json.loads(response.text)
    data = response.text
    return data







### Main Project ###

if __name__ == '__main__':
    print(tbicp())

    # print(type(xmlstr2jsonstr(tbicp("656615951287","PERIOD_0D","80884"))))
    df = pd.read_excel("新品.xlsx", sheet_name="Sheet1")
    goods_name = []
    goods_id = []
    a = df['产品品名'].to_list()
    for i in a:
        goods_name.append(str(i))
    b = df['现货ID'].to_list()
    for m in b:
        goods_id.append(str(m))

    for i in range(len(goods_name)):
        print(tbicp({"brand_name":"多喜爱旗舰店","channel":"OFFLINE_SHOP","channel_publish_time":"2021-10-20 00:00:00","tmall_same":"true","item_id":"'+str(goods_id)[i]+'","item_name":"'+str(goods_id)[i]+'","brand_id":"80884","channel_publish_area":"ALL"}))
        # contents = eval(xmlstr2jsonstr(tbicp({"brand_name":"多喜爱旗舰店","channel":"OFFLINE_SHOP","channel_publish_time":"2021-10-20 00:00:00","tmall_same":"true","item_id":"'+str(goods_id)[i]+'","item_name":"'+str(goods_id)[i]+'","brand_id":"80884","channel_publish_area":"ALL"})))
        # print(contents['tmall.brand.item.upload'])
    #




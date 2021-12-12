# -*- coding:utf-8 -*-
# 同意中文解析

# 引入文件
import time
import hashlib
import requests
import json
import xmltodict


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
def tbicp(item_idx,protection_periodx,brand_idx):

    # noinspection PyUnusedLocal
    method = 'tmall.brand.item.coupon.protect'
    # noinspection PyUnusedLocal
    app_key = '23036663'
    # noinspection PyUnusedLocal
    sign_method = 'md5'
    # noinspection PyUnusedLocal
    # timestamp = int(time.time())
    timestamp = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(time.time()))
    v = '2.0'

    item_id = item_idx
    protection_period = protection_periodx
    brand_id = brand_idx


    # body = contents.encode("utf-8")
    secret = '300ca3f62e9051bfbcf4550dcd98b8f1'

    dqm_str = 'app_key23036663brand_id'+str(brand_idx)+'item_id'+str(item_idx)+'methodtmall.brand.item.coupon' \
                                        '.protectprotection_period'+str(protection_periodx)+'session6100702294147e841d7715eb8a2b55033caa6e780b31a34114141735sign_methodmd5timestamp'+str(timestamp)+'v2.0'
    sign_str = hsmd(str(secret)+str(dqm_str)+str(secret)).upper()
    # return  sign_str


    ### Up Data has set Sign_string ###
    ### Down having POST method Data ###


    url = "http://gw.api.taobao.com/router/rest?app_key=23036663&sign="+str(
        sign_str)+"&method="+str(method)+"&session=6100702294147e841d7715eb8a2b55033caa6e780b31a34114141735&sign_method=md5" \
                              "&timestamp="+str(
        timestamp)+"&v=2.0&item_id="+str(item_idx)+"&protection_period="+str(protection_periodx)+"&brand_id="+str(brand_idx)

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
    # print(type(xmlstr2jsonstr(tbicp("656615951287","PERIOD_0D","80884"))))

    xlist = [657857007220]
    for i in xlist:
        contents = eval(xmlstr2jsonstr(tbicp(str(i),"PERIOD_0D","80884")))
        print(contents['tmall_brand_item_coupon_protect_response'])





#-*- coding:utf-8 -*-
import requests
import json
import pandas as pd
import smtplib
from email.mime.text import MIMEText
from email.header import Header
import time

def myinterface03(tracking_number):
    new_info = []
    url = "http://39.100.94.96/e3/dohia/interfaces/return_goods.php?"

    params = {
        "temp_code":773118734979162
    }
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                      'Chrome/81.0.4044.122 Safari/537.36',
    }
    response = requests.get(url=url, params=params, headers=headers)
    data = json.loads(response.text, encoding='utf-8')
    return data






if __name__=='__main__':
    tracking_number = str(input('>>>扫入退回订单的运单号:'))
    result = myinterface03(tracking_number)
    res = json.loads(result[0].replace("'", '"').replace("'", '"'))
    print(res['return_order_id'])
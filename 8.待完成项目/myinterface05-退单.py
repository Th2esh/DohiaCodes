import requests
import json
import pandas as pd


def myinterface05():
    url = "http://39.100.94.96/e3/dohia/interfaces/return.php?"

    params = {
        'temp_code' : '75502793035553'
    }
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                      'Chrome/81.0.4044.122 Safari/537.36',
    }
    response = requests.get(url=url, params=params, headers=headers)
    # data = json.loads(response.text,encoding='utf-8')
    return response.text

# print(myinterface02())
# res = myinterface02()[0].replace("'",'"')
# res.replace("'",'"')
# json.loads(myinterface01()[0].replace("'",'"'))


print(myinterface05())
# re1 = myinterface05()[0:-1]
# re2 = re1+"]"
# re3 = eval(re2)
#
# for i in range(len(re3)):
#     print(re3[i]['return_order_id'])
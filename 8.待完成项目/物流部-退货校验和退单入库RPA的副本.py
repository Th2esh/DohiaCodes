#-*- coding:utf-8 -*-
import requests
import json
from selenium import webdriver
import datetime

import time

def myinterface():
    url = "http://39.100.94.96/e3/dohia/interfaces/return.php?"
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
    temp_code = str(input('>>>扫入退回订单的运单号:'))
    result = myinterface()
    res = result.replace("'", '"')
    res1 = json.loads(res)
    print(res1['relating_order_sn'])
    while (3 > 2):
        if str(temp_code) == str(999):
            print('>>>程序关闭!!!')
            break

        else:
            check_list = []
            id_list = []
            sn_list = []

            if (res1['goods_number']!= 1):
                for s in range(int(res1['goods_number'])):
                    check_list.append(res1['barcode'])
                    id_list.append(res1['return_order_id'])
                    sn_list.append(res1['return_order_sn'])
            else:
                check_list.append(res1['barcode'])
                id_list.append(res1['return_order_id'])
                sn_list.append(res1['return_order_sn'])
            # 处理一个退回物流单号 仅对应一个退单的情况
            print(check_list)
            if len(id_list) == 1:
                print('该运单仅包含一个退单')
                for cs in range(len(check_list)):
                    temp_goods_sn = str(input('>>>扫入包裹内的商品69码:'))
                    if (str(temp_goods_sn) != str('000')):

                        if temp_goods_sn in check_list:
                            posions = check_list.index(temp_goods_sn)
                            del check_list[posions]
                            if (len(check_list) == 0):
                                print('>>>该退单收货完成，请不要触碰鼠标键盘，等待RPA系统操作完成!!!')
                                ###RPA操作流程###
                                driver = webdriver.Chrome()
                                driver.maximize_window()
                                driver.implicitly_wait(6)
                                driver.get("http://39.100.94.96/e3/webopm/web/")

                                driver.find_element_by_xpath('//*[@id="user_name"]').send_keys('13147')
                                time.sleep(3)
                                driver.find_element_by_xpath('//*[@id="password"]').send_keys('lifei.269')
                                time.sleep(3)
                                driver.find_element_by_xpath('//*[@id="login_button"]').click()
                                time.sleep(15)
                                driver.get(
                                    "http://39.100.94.96/e3/webopm/web/?app_act=refund/refund_list/do_detail&return_order_id=" + str(
                                        res1['return_order_id']))
                                time.sleep(10)
                                driver.find_element_by_xpath('//*[@id="order_qr_' + str(res1['return_order_id']) + '"]').click()
                                time.sleep(5)
                                # noinspection PyDeprecation
                                alert = driver.switch_to_alert()
                                time.sleep(3)
                                alert.accept()
                                time.sleep(3)
                                # noinspection PyDeprecation
                                alert = driver.switch_to_alert()
                                time.sleep(3)
                                alert.accept()
                                time.sleep(3)
                                driver.find_element_by_xpath('//*[@id="order_ksrk_' + str(res1['return_order_id']) + '"]').click()
                                time.sleep(3)
                                # noinspection PyDeprecation
                                alert = driver.switch_to_alert()
                                time.sleep(3)
                                alert.accept()
                                driver.quit()
                                with open('return_goods_list.txt', 'a') as fwr:
                                    fwr.write(
                                        datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S') + '\t' + str(
                                            res1['relating_order_sn']) + '\t' + str(
                                            res1['refund_deal_code']) + '\t' + str(res1['goods_sn']) + '\t' + str(res1['goods_name']) + '\t' + str(
                                            res1['goods_number']) + '\t' + str(
                                            res1['return_shipping_name']) + '\t' + str(res1['return_shipping_sn']) + '\t' + str(res1['relating_fhck_id']) + '\n')
                        else:
                            print('收到的商品与实际不符，操作中止，日志写入中...')
                            with open('return_goods_list.txt', 'a') as fwr:
                                fwr.write(
                                    datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S') + '\t' + str(
                                        res1['relating_order_sn']) + '\t' + str(
                                        res1['refund_deal_code']) + '\t' + '商品错误，操作未完成\n')
                    else:
                        with open('return_goods_list.txt', 'a') as fwr:
                            fwr.write(
                                datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S') + '\t' + str(res1['relating_order_sn']) + '\t' + str(
                                    res1['refund_deal_code']) + '\t' + str(res1['goods_name']) + '\t该订单缺少商品，操作未完成\n')
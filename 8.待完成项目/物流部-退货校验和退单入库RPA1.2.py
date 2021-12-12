#-*- coding:utf-8 -*-
from sshtunnel import SSHTunnelForwarder
import pymysql
from selenium import webdriver
import datetime
import time

server = SSHTunnelForwarder(ssh_address_or_host=('39.100.94.96', 22), ssh_username='efast',ssh_password='51ksCg7eZ!VUgNx',remote_bind_address=('rm-vy1p7dyx917c11za2.mysql.rds.aliyuncs.com', 3306))
server.start()
db = pymysql.connect(host='127.0.0.1', port=server.local_bind_port, user='jusr2mmi49d8', passwd='uEZBjc9tQwoN',db='e3', charset='utf8')
cur = db.cursor()


temp_code = str(input('>>>扫入退回订单的运单号:'))

while(3>2):
    if str(temp_code) == str(999):
        print('>>>程序关闭!!!')
        server.close()
        break

    else:
        cur.execute("select goods_barcode.barcode,order_return_goods.goods_number,order_return.relating_order_sn,order_return.refund_deal_code,order_return_goods.goods_name,order_return.relating_fhck_id,order_return.return_shipping_name,order_return.return_shipping_sn,order_return_goods.goods_sn,order_return.return_order_id,order_return.return_order_sn from order_return,order_return_goods,goods_barcode where order_return.return_order_id = order_return_goods.return_order_id and order_return_goods.goods_id = goods_barcode.goods_id and order_return.return_shipping_sn = '"+temp_code+"'")
        results = cur.fetchall()
        check_list = []
        id_list = []
        sn_list = []
        for row in results:
            if(row[1] != 1):
                for s in range(int(row[1])):
                    check_list.append(row[0])
                id_list.append(row[9])
                sn_list.append(row[10])
            else:
                check_list.append(row[0])
                id_list.append(row[9])
                sn_list.append(row[10])
        # 处理一个退回物流单号 仅对应一个退单的情况

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
                            driver.get("http://39.100.94.96/e3/webopm/web/?app_act=refund/refund_list/do_detail&return_order_id="+str(row[9]))
                            time.sleep(10)
                            driver.find_element_by_xpath('//*[@id="order_qr_' + str(row[9]) + '"]').click()
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
                            driver.find_element_by_xpath('//*[@id="order_ksrk_' + str(row[9]) + '"]').click()
                            time.sleep(3)
                            # noinspection PyDeprecation
                            alert = driver.switch_to_alert()
                            time.sleep(3)
                            alert.accept()
                            driver.quit()
                            with open('return_goods_list.txt', 'a') as fwr:
                                fwr.write(
                                    datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S') + '\t' + str(
                                        row[2]) + '\t' + str(
                                        row[3]) + '\t' + str(row[8]) + '\t' + str(row[4]) + '\t' + str(
                                        row[1]) + '\t' + str(
                                        row[6]) + '\t' + str(row[7]) + '\t' + str(row[5]) + '\n')
                    else:
                        print('收到的商品与实际不符，操作中止，日志写入中...')
                        with open('return_goods_list.txt', 'a') as fwr:
                            fwr.write(
                                datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S') + '\t' + str(row[2]) + '\t' + str(
                                    row[3]) + '\t' + '商品错误，操作未完成\n')
                else:
                    with open('return_goods_list.txt', 'a') as fwr:
                        fwr.write(
                            datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S') + '\t' + str(row[2]) + '\t' + str(
                                row[3]) + '\t' + str(row[4]) + '\t该订单缺少商品，操作未完成\n')
        # 处理一个退回物流单号 对应多个退单的情况
        else:
            print('该退回单号包含多个退单,请随机扫描商品')
            for ids in id_list:
                cur.execute("select goods_barcode.barcode,order_return_goods.goods_number,order_return.relating_order_sn,order_return.refund_deal_code,order_return_goods.goods_name,order_return.relating_fhck_id,order_return.return_shipping_name,order_return.return_shipping_sn,order_return_goods.goods_sn,order_return.return_order_id,order_return.return_order_sn from order_return,order_return_goods,goods_barcode where order_return.return_order_id = order_return_goods.return_order_id and order_return_goods.goods_id = goods_barcode.goods_id and order_return.return_order_id = '" + str(ids) + "'")
                results2 = cur.fetchall()
                for r2 in results2:
                    temp_goods_sn = str(input('>>>扫入包裹内的商品69码:'))
                    cur.execute("select goods_barcode.barcode,order_return_goods.goods_number,order_return.relating_order_sn,order_return.refund_deal_code,order_return_goods.goods_name,order_return.relating_fhck_id,order_return.return_shipping_name,order_return.return_shipping_sn,order_return_goods.goods_sn,order_return.return_order_id,order_return.return_order_sn from order_return,order_return_goods,goods_barcode where order_return.return_order_id = order_return_goods.return_order_id and order_return_goods.goods_id = goods_barcode.goods_id and goods_barcode.barcode = '" + str(temp_goods_sn) + "' and order_return.return_shipping_sn = '"+temp_code+"'")
                    results3 = cur.fetchall()
                    for r3 in results3:
                        if (str(temp_goods_sn) != str('000')):
                            # print(r3[10])
                            ###RPA操作流程###
                            print('开始RPA操作，请等待')
                            driver = webdriver.Chrome()
                            driver.maximize_window()
                            driver.implicitly_wait(6)
                            driver.get("http://39.100.94.96/e3/webopm/web/")

                            driver.find_element_by_xpath('//*[@id="user_name"]').send_keys('13147')
                            time.sleep(3)
                            driver.find_element_by_xpath('//*[@id="password"]').send_keys('lifei.269')
                            time.sleep(3)
                            driver.find_element_by_xpath('//*[@id="login_button"]').click()
                            time.sleep(3)

                            driver.get("http://39.100.94.96/e3/webopm/web/?app_act=refund/refund_list/do_list")
                            time.sleep(10)
                            driver.find_element_by_xpath('//*[@id="search_return_shipping_sn"]').send_keys(
                                "str(temp_code)")
                            time.sleep(3)
                            driver.find_element_by_xpath('//*[@id="order_list_search"]').click()
                            time.sleep(3)
                            # 重点：这里改用link_text定位
                            driver.find_element_by_link_text(str(r3[10])).click()
                            # driver.find_element_by_xpath('//*[@id="order_list_table"]/table/tbody/tr[1]/td[2]/a').click()
                            time.sleep(3)
                            driver.switch_to.default_content()
                            driver.switch_to.frame(driver.find_element_by_xpath('//*[@id="退单详细'+str(r3[10])+'"]'))
                            time.sleep(3)
                            driver.find_element_by_xpath('//*[@id="order_qr_'+str(r3[9])+'"]').click()
                            time.sleep(3)
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
                            driver.find_element_by_xpath('//*[@id="order_ksrk_'+str(r3[9])+'"]').click()
                            time.sleep(3)
                            # noinspection PyDeprecation
                            alert = driver.switch_to_alert()
                            time.sleep(3)
                            alert.accept()
                            driver.quit()
                            with open('return_goods_list.txt', 'a') as fwr:
                                fwr.write(datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S') + '\t' + str(
                                    r3[2]) + '\t' + str(r3[3]) + '\t' + str(r3[8]) + '\t' + str(r3[4]) + '\t' + str(
                                    r3[1]) + '\t' + str(r3[6]) + '\t' + str(r3[7]) + '\t' + str(r3[5]) + '\n')
                        else:
                            with open('return_goods_list.txt', 'a') as fwr:
                                fwr.write(
                                    datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S') + '\t' + str(
                                        row[2]) + '\t' + str(
                                        row[3]) + '\t' + str(row[4]) + '\t该订单缺少商品，操作未完成\n')


    temp_code = str(input('>>>扫入退回订单的运单号:'))



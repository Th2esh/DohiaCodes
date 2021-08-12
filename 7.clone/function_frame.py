#coding: UTF-8

def write_note(problem,user,discrption):
    import datetime
    with open('wrd.txt', 'a') as wrd:
        wrd.write(datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S') + '\t' + user + '\t' + problem + '\t' + discrption + '\n')

def write_DepartmentWork(who,problem):
    import datetime
    with open('department_work_note.txt', 'a') as dwn:
        dwn.write(datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S') + '\t' + who + '\t' + problem +'\n')
def mysql_query_results(sql):
    import pandas as pd
    from sshtunnel import SSHTunnelForwarder
    import pymysql

    server = SSHTunnelForwarder(ssh_address_or_host=('39.100.94.96', 22), ssh_username='efast',
                                ssh_password='51ksCg7eZ!VUgNx',
                                remote_bind_address=('rm-vy1p7dyx917c11za2.mysql.rds.aliyuncs.com', 3306))
    server.start()
    db = pymysql.connect(host='127.0.0.1', port=server.local_bind_port, user='jusr2mmi49d8', passwd='uEZBjc9tQwoN',
                         db='e3', charset='utf8')
    cur = db.cursor()
    cur.execute(sql)
    results = cur.fetchall()
    db.commit()
    return results

    # df = pd.DataFrame(results)
    # return df
def clone_order_action2(clone_goods_sn,real_goods_sn):
    from selenium import webdriver
    import time
    import pyautogui
    from sshtunnel import SSHTunnelForwarder
    import pymysql
    import pandas as pd
    server = SSHTunnelForwarder(ssh_address_or_host=('39.100.94.96', 22), ssh_username='efast',
                                ssh_password='51ksCg7eZ!VUgNx',
                                remote_bind_address=('rm-vy1p7dyx917c11za2.mysql.rds.aliyuncs.com', 3306))
    server.start()
    db = pymysql.connect(host='127.0.0.1', port=server.local_bind_port, user='jusr2mmi49d8', passwd='uEZBjc9tQwoN',
                         db='e3', charset='utf8')
    cur = db.cursor()
    cur.execute('select order_info.order_sn as osn,order_info.order_id,order_goods.id from order_info,order_goods '
                'where '
                'order_info.order_id = order_goods.order_id and order_info.fhck_id = 24 and order_info.order_status = 0 and order_goods.goods_sn ='+str(clone_goods_sn)+' order by osn asc')
    results = cur.fetchall()
    db.commit()
    if len(results) == 0:
        print('No Order')
    else:
        df = pd.DataFrame(results)
        order_sn_list = df[0].to_list()
        order_id_list = df[1].to_list()
        order_goods_id_list = df[2].to_list()


    ## 判断库存来确定ck_id的值
        cur.execute("select sl from spkcb where sku = '"+str(real_goods_sn)+"' and ck_id = 3")
        results_pdkc = cur.fetchall()
        db.commit()
        dfr = pd.DataFrame(results_pdkc)
        xtem = dfr[0].to_list()
        if xtem[0] != 0:
            ck_id = 2
        else:
            ck_id = 4
        driver = webdriver.Chrome()
        driver.maximize_window()
        driver.implicitly_wait(6)
        driver.get("http://39.100.94.96/e3/webopm/web/")

        # Login System
        driver.find_element_by_xpath('//*[@id="user_name"]').send_keys('clone')
        time.sleep(3)
        driver.find_element_by_xpath('//*[@id="password"]').send_keys('Dohia&33')
        time.sleep(3)
        driver.find_element_by_xpath('//*[@id="login_button"]').click()
        time.sleep(3)

        js = []
        for i in range(len(order_id_list)):
            driver.switch_to.window(driver.window_handles[-1])
            pyautogui.hotkey('Ctrl', 't')
            time.sleep(3)
            driver.switch_to.window(driver.window_handles[-1])
            driver.get("http://39.100.94.96/e3/webopm/web/?app_act=order/order_list/do_detail&order_id="+str(order_id_list[i]))
            time.sleep(5)
            driver.find_element_by_xpath('//*[@id="goods_'+str(order_goods_id_list[i])+'"]/td[12]/div/a[3]').click()
            time.sleep(3)
            driver.switch_to.default_content()
            time.sleep(3)
            driver.switch_to.window(driver.window_handles[-1])
            time.sleep(3)
            driver.find_element_by_xpath('//*[@id="key_word"]').send_keys(real_goods_sn)
            time.sleep(3)
            driver.find_element_by_xpath('//*[@id="btn-search"]').click()

            ######
            cur.execute("select goods_id from goods where goods_sn ="+real_goods_sn)
            results1 = cur.fetchall()
            db.commit()
            ######
            time.sleep(3)
            driver.find_element_by_xpath('//*[@id="node-'+str(results1[0][0])+'"]/td[5]/a[2]').click()
            time.sleep(3)
            driver.switch_to.window(driver.window_handles[-1])
            time.sleep(3)
            driver.find_element_by_xpath('//*[@id="openDivContentgoods_edit_popDiv"]/div/div/input').click()
            time.sleep(3)
            driver.switch_to_alert().accept()
            time.sleep(5)
            driver.switch_to.window(driver.window_handles[-1])
            time.sleep(3)
            driver.find_element_by_xpath('//*[@id="edit_fahuo"]').click()
            time.sleep(3)
            driver.find_element_by_xpath('//*[@id="fhck_id"]/option['+str(ck_id)+']').click()
            time.sleep(3)
            driver.find_element_by_xpath('//*[@id="save_fahuo"]').click()
            time.sleep(3)
            # noinspection PyDeprecation
            driver.find_element_by_xpath('//*[@id="order_qr_'+str(order_id_list[i])+'"]').click()
            time.sleep(3)
            # noinspection PyDeprecation
            driver.switch_to_alert().accept()
            time.sleep(3)
            driver.find_element_by_xpath('//*[@id="order_syncwms_'+str(order_id_list[i])+'"]').click()
            time.sleep(3)
            driver.switch_to_alert().accept()
            time.sleep(3)

            # Close Used Tab
            time.sleep(10)
            pyautogui.hotkey('Ctrl', 'w')
            time.sleep(3)
            js.append('*')
        driver.quit()
        print(js)
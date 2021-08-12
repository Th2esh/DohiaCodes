# import socket
#
#
# def get_host_ip():
#     """
#     查询本机ip地址
#     :return: ip
#     """
#     try:
#         s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
#         s.connect(('8.8.8.8', 80))
#         ip = s.getsockname()[0]
#     finally:
#         s.close()
#         return ip
#
# if __name__ == '__main__':
#     print(get_host_ip())





from sshtunnel import SSHTunnelForwarder
import pymysql
from selenium import webdriver
import datetime
import time

driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(6)
driver.get("http://39.100.94.96/e3/webopm/web/")

driver.find_element_by_xpath('//*[@id="user_name"]').send_keys('13147')
time.sleep(3)
driver.find_element_by_xpath('//*[@id="password"]').send_keys('lifei.268')
time.sleep(3)
driver.find_element_by_xpath('//*[@id="login_button"]').click()
time.sleep(3)
driver.get("http://39.100.94.96/e3/webopm/web/?app_act=refund/refund_list/do_list")
driver.find_element_by_xpath('//*[@id="search_return_shipping_sn"]').send_keys("str(temp_code)")
time.sleep(3)
driver.find_element_by_xpath('//*[@id="order_list_search"]').click()
time.sleep(3)
driver.find_element_by_xpath('//*[@id="order_list_table"]/table/tbody/tr[1]/td[2]/a').click()
time.sleep(3)
driver.find_element_by_xpath('//*[@id="order_qr_' + str(row[9]) + '"]').click()
time.sleep(3)


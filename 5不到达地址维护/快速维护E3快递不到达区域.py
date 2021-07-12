from default_function_folder.default_function import read_file_basic
from default_function_folder.default_function import mysql_query_kd
import pandas as pd
import os

# Login Informations:
zh = read_file_basic('key.xlsx','Sheet1')['user'][0]
mm = read_file_basic('key.xlsx','Sheet1')['password'][0]
kd = read_file_basic('key.xlsx','Sheet1')['kd'][0]

del_query = "delete from out_region where shipping_id ="+str(kd)
mysql_query_kd(del_query,zh,mm)

set_region = read_file_basic('bdd.xlsx','Sheet1')['title'].to_list()
set_region_str = ",".join(str("'"+i+"'") for i in set_region)

find_query = "select region_id from region where region_name in ("+set_region_str+")"
df = pd.DataFrame(mysql_query_kd(find_query,zh,mm))
set_region_code = df[0].to_list()

for i in set_region_code:
    update_query = "insert into out_region (shipping_id,region_id,supply_shippings) values("+str(kd)+","+str(i)+",'')"
    mysql_query_kd(update_query,zh,mm)
os._exit(0)
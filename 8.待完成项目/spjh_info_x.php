<?php 


header("content-type:text/html; charset=utf8");


$conn=mysql_connect("rm-vy1p7dyx917c11za2.mysql.rds.aliyuncs.com","jusr2mmi49d8","uEZBjc9tQwoN");
	if($conn==null){
		die("Mysql connect error".mysql_error());
	}
mysql_select_db("e3");
mysql_set_charset('utf8'); #设置数据库的编码方式-
date_default_timezone_set("Asia/Shanghai");

$sql="select if(spjhd.ck_id=11,'南通仓',IF(spjhd.ck_id=3,'上海仓','长沙仓')) as rkc,FROM_UNIXTIME(spjhd.ysrq,'%H:%i:%s') as rksj,spjhdmx.goods_sn as hh,goods.goods_name as hm,spjhdmx.sl as rksl from spjhd,spjhdmx,goods where spjhd.id = spjhdmx.dj_id and spjhdmx.goods_sn = goods.goods_sn and FROM_UNIXTIME(spjhd.ysrq,'%Y-%m-%d') = DATE_FORMAT(now(),'%Y-%m-%d') and spjhd.ck_id in (3,10,11) order by hm desc";

$result=mysql_query($sql);

$temp_x = array();

while($rows=mysql_fetch_array($result)){
	$temp_x[] = '{"rkc":"'.$rows["rkc"].'","rksj":"'.$rows["rksj"].'","hh":"'.$rows["hh"].'","hm":"'.$rows["hm"].'","rksl":"'.$rows["rksl"].'"}';
}

echo urldecode(json_encode($temp_x[0]))


?>
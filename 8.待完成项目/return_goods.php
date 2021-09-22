<?php 


header("content-type:text/html; charset=utf8");

$temp_code = $_GET['temp_code'];



$conn=mysql_connect("rm-vy1p7dyx917c11za2.mysql.rds.aliyuncs.com","jusr2mmi49d8","uEZBjc9tQwoN");
	if($conn==null){
		die("Mysql connect error".mysql_error());
	}
mysql_select_db("e3");
mysql_set_charset('utf8'); #设置数据库的编码方式-
date_default_timezone_set("Asia/Shanghai");

$sql = "select return_order_id from order_return where return_shipping_sn = '".$temp_code."'";

$result=mysql_query($sql);

$temp_x = array();

// while($rows=mysql_fetch_array($result)){
// 	$temp_x[] = "{'goods_name':'".$rows['gsname']."','goods_sn':'".$rows['gsn']."','sales_volume':'".$rows['sales_volume']."'}";
// }
while($rows=mysql_fetch_array($result)){
	$temp_x[] = "{'return_order_id':'".$rows['return_order_id']."'}";
}

echo urldecode(json_encode($temp_x))


?>
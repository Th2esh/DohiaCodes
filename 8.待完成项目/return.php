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

$sql="select goods_barcode.barcode,order_return_goods.goods_number,order_return.relating_order_sn,order_return.refund_deal_code,order_return_goods.goods_name,order_return.relating_fhck_id,order_return.return_shipping_name,order_return.return_shipping_sn,order_return_goods.goods_sn,order_return.return_order_id,order_return.return_order_sn from order_return,order_return_goods,goods_barcode where order_return.return_order_id = order_return_goods.return_order_id and order_return_goods.goods_id = goods_barcode.goods_id and order_return.return_shipping_sn = '".$temp_code."'";

$result=mysql_query($sql);

$temp_x = array();

while($rows=mysql_fetch_array($result)){
	$temp_x[] = "{'barcode':'".$rows['barcode']."','goods_number':'".$rows['goods_number']."','relating_order_sn':'".$rows['relating_order_sn']."','refund_deal_code':'".$rows['refund_deal_code']."','goods_name':'".$rows['goods_name']."','relating_fhck_id':'".$rows['relating_fhck_id']."','return_shipping_name':'".$rows['return_shipping_name']."','return_shipping_sn':'".$rows['return_shipping_sn']."','goods_sn':'".$rows['goods_sn']."','return_order_id':'".$rows['return_order_id']."','return_order_sn':'".$rows['return_order_sn']."'}";
}

echo urldecode(json_encode($temp_x[0]))

?>

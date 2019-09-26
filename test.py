import pymysql.cursors

ershoufang_sql = """
CREATE TABLE `ershoufang` (
`id` INT ( 11 ) NOT NULL AUTO_INCREMENT,
`city` VARCHAR ( 255 )  NOT NULL DEFAULT '' COMMENT '城市',
`house_url` LONGTEXT  NOT NULL  COMMENT '房产url',
`img_url` LONGTEXT  NOT NULL COMMENT '图片链接',
`title` VARCHAR ( 255 )  NOT NULL DEFAULT '' COMMENT '标题',
`xiaoqu_url` text ( 255 )  NOT NULL COMMENT '小区url',
`xiaoqu_name` VARCHAR ( 255 )  NOT NULL DEFAULT '' COMMENT '小区名',
`huxing` VARCHAR ( 255 )  NOT NULL DEFAULT '' COMMENT '户型',
`position_info` VARCHAR ( 255 )  NOT NULL DEFAULT '' COMMENT '位置信息',
`position` VARCHAR ( 255 )  NOT NULL DEFAULT '' COMMENT '位置',
`position_url` VARCHAR ( 255 )  NOT NULL DEFAULT '' COMMENT '位置url',
`total_price` INT ( 11 )  NOT NULL DEFAULT 0 COMMENT '总价',
`square_price` INT ( 11 )  NOT NULL DEFAULT 0 COMMENT '每平米价格',
`crawl_time` BIGINT  NOT NULL DEFAULT 0,
PRIMARY KEY ( `id` ) 
) ENGINE = INNODB AUTO_INCREMENT = 2 DEFAULT CHARSET = utf8 ;
"""



# Connect to the database
connection = pymysql.connect(host='39.106.114.90',
                             user='root',
                             password='root',
                             db='lianjia',
                             charset='utf8',
                             cursorclass=pymysql.cursors.DictCursor)
cursor = connection.cursor()
effect_row = cursor.execute(ershoufang_sql)
# 获取剩余结果所有数据
result = cursor.fetchall()
print(result)

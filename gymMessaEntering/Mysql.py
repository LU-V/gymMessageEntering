import sqlite3
conn = sqlite3.connect('stu.db')
c = conn.cursor()
# c.execute('''DELIMITER //create PROCEDURE proc6 (in p char(50) ,out p_sno char(50),out ok char(50))begin select Sname from students where Sname=p; select Ssex into p_sno from students where Sname=p; set ok = 'okey';end// DELIMITER ;''')
# c.execute('''CREATE TABLE `course` (
# 	`Cno` INT(11) NOT NULL,
# 	`Cname` CHAR(10) NOT NULL,
# 	`Cpno` INT(11) NULL DEFAULT NULL,
# 	`Ccredit` INT(11) NOT NULL,
# 	PRIMARY KEY (`Cno`)
# )
#
# ''')
# c.execute('''
# CREATE TABLE `sc` (
# 	`Sno` CHAR(10) NOT NULL,
# 	`Cno` INT(11) NOT NULL,
# 	`Grade` INT(11) NOT NULL,
# 	PRIMARY KEY (`Sno`, `Cno`)
# )
#
#
# ''')
# c.execute('''
# CREATE TABLE `course` (
# 	`Cno` INT(11) NOT NULL,
# 	`Cname` CHAR(10) NOT NULL,
# 	`Cpno` INT(11) NULL DEFAULT NULL,
# 	`Ccredit` INT(11) NOT NULL,
# 	PRIMARY KEY (`Cno`)
# )
# ''')

# c.execute('''CREATE TABLE `students` (
# 	`Sno` CHAR(12) NOT NULL,
# 	`Sname` CHAR(12) NOT NULL,
# 	`Ssex` CHAR(12) NOT NULL,
# 	`Sage` INT(11) NOT NULL,
# 	`Sdept` CHAR(12) NOT NULL,
# 	PRIMARY KEY (`Sno`))
# 	''')
# c.execute('''insert  into students values('201215123'	,'王敏',	'女',	18	,'ma'),
#
# ('201215125',	'张立',	'男',	19	,'is'),
# ('201215122',	'刘晨'	,'女',	19,'cs'),
# ('201215121',	'李勇',	'男',	20,	'cs')
#
# ''')
# c.execute('''insert  into course values
# (1,	'数据库',	5	,4),
# (2	,'数学'	,NULL ,	2),
# (3,	'信息系统',	1,	4),
# (4	,'操作系统'	,6	,3),
# (5,	'数据结构'	,7	,4),
# (6,	'数据处理'	,NULL ,	2),
# (7	,'PASCAL语言',	6	,4)
# ''')

# c.execute('''insert  into sc values
#
# ('201215121'	,1	,92),
# ('201215121'	,2	,85),
# ('201215121'	,3	,88),
# ('201512122'	,2	,90),
# ('201512122'	,3	,80)
#
# ''')


conn.commit()
conn.close()

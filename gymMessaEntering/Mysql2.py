import pymysql
import tkinter as tk
from tkinter import ttk
import tkinter.messagebox

db= pymysql.connect(host="localhost",user="root",
    password="root",db="stu",port=3306)
c = db.cursor()
c.execute('''call proc(90)''')
results = c.fetchall()  # 获取查询的所有记录

# 遍历结果
for row in results:
    sno = row[0]
    cno = row[1]
    grade = row[2]
    print(sno, cno, grade)


db.close()





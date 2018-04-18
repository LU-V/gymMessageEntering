import tkinter
import tkinter.ttk
import tkinter.messagebox
import pymysql

# 创建tkinter应用程序窗口
root = tkinter.Tk()
# 设置窗口大小和位置
root.geometry('820x500')
# 不允许改变窗口大小
root.resizable(False, False)
# 设置窗口标题
root.title('学生信息教练统')

# 在窗口上放置标签组件和用于输入姓名的文本框组件
lbSno = tkinter.Label(root, text='会员号：')
lbSno.place(x=10, y=10, width=40, height=20)
entrySno = tkinter.Entry(root)
entrySno.place(x=60, y=10, width=150, height=20)
# 在窗口上放置标签组件和用于输入部门的文本框组件
lbName = tkinter.Label(root, text='姓名：')
lbName.place(x=220, y=10, width=40, height=20)
entryName = tkinter.Entry(root)
entryName.place(x=270, y=10, width=150, height=20)

# 在窗口上放置标签组件和用于选择性别的组合框组件
lbSex = tkinter.Label(root, text='性别：')
lbSex.place(x=220, y=50, width=40, height=20)
entrySex1 = tkinter.Entry(root)
entrySex1.place(x=270, y=50, width=150, height=20)
# 在窗口上放置标签组件和用于输入年龄的文本框组件
lbAge = tkinter.Label(root, text='年龄：')
lbAge.place(x=10, y=50, width=40, height=20)
entryAge = tkinter.Entry(root)
entryAge.place(x=60, y=50, width=150, height=20)

# 在窗口上放置标签组件和用于输入电话号码的文本框组件
lbDept = tkinter.Label(root, text='教练：')
lbDept.place(x=10, y=90, width=40, height=20)
entryDept = tkinter.Entry(root)
entryDept.place(x=60, y=90, width=150, height=20)

lbDeSno = tkinter.Label(root, text='要删除的会员号：')
lbDeSno.place(x=500, y=10, width=100, height=20)
entryDeSno = tkinter.Entry(root)
entryDeSno.place(x=600, y=10, width=150, height=20)

lbDeSno = tkinter.Label(root, text='要转教练的会员号：')
lbDeSno.place(x=500, y=40, width=100, height=20)
entryUpdateSno = tkinter.Entry(root)
entryUpdateSno.place(x=600, y=40, width=150, height=20)

lbUpdateDept = tkinter.Label(root, text='改成什么教练：')
lbUpdateDept.place(x=500, y=70, width=100, height=20)
entryUpdateDept = tkinter.Entry(root)
entryUpdateDept.place(x=600, y=70, width=150, height=20)

lbUpdateSage = tkinter.Label(root, text='改年龄的会员号：')
lbUpdateSage.place(x=500, y=100, width=100, height=20)
entryUpdateSage = tkinter.Entry(root)
entryUpdateSage.place(x=600, y=100, width=150, height=20)

# 在窗口上放置用来显示通信录信息的表格，使用Treeview组件实现
frame = tkinter.Frame(root)
frame.place(x=10, y=180, width=350, height=280)

# Treeview组件
studentList = tkinter.ttk.Treeview(frame, columns=('c1', 'c2', 'c3', 'c4', 'c5'),
                                   show="headings")
studentList.column('c1', width=100, anchor='center')
studentList.column('c2', width=80, anchor='center')
studentList.column('c3', width=40, anchor='center')
studentList.column('c4', width=40, anchor='center')
studentList.column('c5', width=50, anchor='center')
studentList.heading('c1', text='会员号')
studentList.heading('c2', text='姓名')
studentList.heading('c3', text='性别')
studentList.heading('c4', text='年龄')
studentList.heading('c5', text='教练')
studentList.pack(side=tkinter.LEFT, fill=tkinter.Y)

# 遍历结果

# 在窗口上放置用来显示通信录信息的表格，使用Treeview组件实现
frame = tkinter.Frame(root)
frame.place(x=350, y=180, width=220, height=280)

# Treeview组件
courseList = tkinter.ttk.Treeview(frame, columns=('c1', 'c2', 'c3', 'c4', 'c5'),
                                  show="headings")
courseList.column('c1', width=40, anchor='center')
courseList.column('c2', width=80, anchor='center')
courseList.column('c3', width=40, anchor='center')
courseList.column('c4', width=40, anchor='center')

courseList.heading('c1', text='课程号')
courseList.heading('c2', text='课程名')
courseList.heading('c3', text='Cpno')
courseList.heading('c4', text='Ccredit')

courseList.pack(side=tkinter.LEFT, fill=tkinter.Y)

# 遍历结果


# 在窗口上放置用来显示通信录信息的表格，使用Treeview组件实现
frame = tkinter.Frame(root)
frame.place(x=600, y=180, width=220, height=280)
# Treeview组件
scList = tkinter.ttk.Treeview(frame, columns=('c1', 'c2', 'c3'),
                              show="headings")
scList.column('c1', width=40, anchor='center')
scList.column('c2', width=80, anchor='center')
scList.column('c3', width=80, anchor='center')
scList.heading('c1', text='会员号')
scList.heading('c2', text='课程号')
scList.heading('c3', text='给教练打分')
scList.pack(side=tkinter.LEFT, fill=tkinter.Y)


def bindDataS():
    '''把数据库里的通信录记录读取出来，然后在表格中显示'''
    # 删除表格中原来的所有行
    for row in studentList.get_children():
        studentList.delete(row)
    # 读取数据

    db = pymysql.connect(host="localhost", user="root",
                         password="root", db="stu", port=3306, charset='utf8')
    c = db.cursor()
    c.execute('select * from v1')
    temp = c.fetchall()

    db.close()
    # 把数据插入表格
    for i, item in enumerate(temp):
        studentList.insert('', i, values=item[:])


# 调用函数，把数据库中的记录显示到表格中
bindDataS()


def bindDataC():
    '''把数据库里的通信录记录读取出来，然后在表格中显示'''
    # 删除表格中原来的所有行
    for row in courseList.get_children():
        courseList.delete(row)
    # 读取数据

    db = pymysql.connect(host="localhost", user="root",
                         password="root", db="stu", port=3306, charset='utf8')
    c = db.cursor()
    c.execute('select * from v2')
    temp = c.fetchall()

    db.close()
    # 把数据插入表格
    for i, item in enumerate(temp):
        courseList.insert('', i, values=item[:])


# 调用函数，把数据库中的记录显示到表格中
bindDataC()


def bindDataSC():
    '''把数据库里的通信录记录读取出来，然后在表格中显示'''
    # 删除表格中原来的所有行
    for row in scList.get_children():
        scList.delete(row)
    # 读取数据

    db = pymysql.connect(host="localhost", user="root",
                         password="root", db="stu", port=3306, charset='utf8')
    c = db.cursor()
    c.execute('select * from v3')
    temp = c.fetchall()

    db.close()
    # 把数据插入表格
    for i, item in enumerate(temp):
        scList.insert('', i, values=item[:])


# 调用函数，把数据库中的记录显示到表格中
bindDataSC()


def add():
    sno = entrySno.get().strip()
    sname = entryName.get().strip()
    ssex = entrySex1.get()
    sage = entryAge.get()
    sdept = entryDept.get()
    db = pymysql.connect(host="localhost", user="root",
                         password="root", db="stu", port=3306, charset='utf8')
    c = db.cursor()

    c.execute("INSERT INTO students (Sno, Sname,Ssex,Sage,Sdept) VALUES ('%s', '%s','%s','%s','%s')" % (
    sno, sname, ssex, sage, sdept))
    db.commit()

    bindDataS()
    db.close()


def delete():
    DeSno = entryDeSno.get().strip()

    db = pymysql.connect(host="localhost", user="root",
                         password="root", db="stu", port=3306, charset='utf8')
    c = db.cursor()

    c.execute("DELETE FROM students WHERE Sno='" + DeSno + "'")

    db.commit()

    bindDataS()
    db.close()


def update():
    UpdateSno = entryUpdateSno.get().strip()
    UpdateDept = entryUpdateDept.get().strip()
    db = pymysql.connect(host="localhost", user="root",
                         password="root", db="stu", port=3306, charset='utf8')
    c = db.cursor()
    SQL = "UPDATE students SET Sdept='%s' WHERE Sno='%s'"
    c.execute(SQL % (UpdateDept, UpdateSno))

    db.commit()

    bindDataS()
    db.close()


def ageadd():
    UpdateSage = entryUpdateSage.get()
    db = pymysql.connect(host="localhost", user="root",
                         password="root", db="stu", port=3306, charset='utf8')
    c = db.cursor()
    c.execute("update students set Sage = Sage + 1 where Sno = '%s'" % (UpdateSage))

    db.commit()

    bindDataS()
    db.close()


button3 = tkinter.Button(root, text='录入信息', command=add)  # command=buttonClick1点击时调用buttonClick1函数
button3.place(x=100, y=140, height=20, width=90)

button4 = tkinter.Button(root, text='删除信息', command=delete)  # command=buttonClick1点击时调用buttonClick1函数
button4.place(x=200, y=140, height=20, width=90)

button5 = tkinter.Button(root, text='换教练', command=update)  # command=buttonClick1点击时调用buttonClick1函数
button5.place(x=300, y=140, height=20, width=90)

button6 = tkinter.Button(root, text='年龄加1', command=ageadd)  # command=buttonClick1点击时调用buttonClick1函数
button6.place(x=400, y=140, height=20, width=90)
root.mainloop()
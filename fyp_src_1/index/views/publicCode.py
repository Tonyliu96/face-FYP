# from ..models import Employee,Role,WorkSchedule
# from datetime import date,datetime, timedelta
# currentDate = datetime.now().strftime("%Y-%m-%d")
# import schedule
# #pip install schedule
# import time
# from django.db.models import Q
import os
#
# def updateMark():
# 	UserStatus = WorkSchedule.objects.filter(StartDate__lt=currentDate)
# 	print(UserStatus)
# 	for i in UserStatus:
# 		WorksId = WorkSchedule.objects.get(WorkSchedule_id=i.WorkSchedule_id)
# 		if WorksId.Mark.lower()!='off' or WorksId.Mark.lower()!='mc':
# 			if  WorksId.InTime=='' or WorksId.InTime is None or WorksId.OutTime is None or WorksId.OutTime=='':
# 				WorksId.Mark ='Absent'
#
# 			elif WorksId.StartTime < WorksId.InTime and WorksId.EndTime > WorksId.OutTime:
# 				WorksId.Mark='Late & leave early'
#
# 			elif WorksId.StartTime >= WorksId.InTime and WorksId.EndTime > WorksId.OutTime:
# 				WorksId.Mark='leave early'
#
# 			elif WorksId.StartTime < WorksId.InTime and WorksId.EndTime <= WorksId.OutTime:
# 				WorksId.Mark='late'
#
# 			elif WorksId.StartTime >= WorksId.InTime and WorksId.EndTime <= WorksId.OutTime:
# 				WorksId.Mark = 'Present'
#
# 			else:
# 				WorksId.Mark='Pending'
# 			WorksId.save()
#
#
#
# schedule.every().hour.do(updateMark)
#
# while True:
# 	schedule.run_pending()   # 运行所有可以运行的任务
# 	time.sleep(10)

import sqlite3
import random
import string
import hashlib

conn = sqlite3.connect('/Users/TonyL/Desktop/FYP-22-S4-github/fyp_src_1/db.sqlite3')
se = conn.cursor()
print("link success")

# for row in cursor:
#    print ("ID = ", row[0])
#    print ("NAME = ", row[1])
#    print ("ADDRESS = ", row[2])
#    print ("SALARY = ", row[3]), "\n"
#
# print ("数据操作成功")
from datetime import date, timedelta

# d1 = date(2023, 1, 1)
# d2 = date(2023, 2, 20)
# delta = d2 - d1
#
# for i in range(delta.days + 1):
#     dat= d1 + timedelta(days=i)


# insertEmployee = "INSERT INTO index_employee (Employee_ID, Full_Name, Job_Title, Phone_Number, Email_Address, Password, Start_Date, Role_id, salt, Profile_Image) values(?,?,?,?,?,?,?,?,?,?)"
# d=30
InsertWork = "insert into WorkSchedule(mark, startdate, employee_id, endtime, starttime, intime, outtime) VALUES (?,?,?,?,?,?,?)"
# for i in range(100005,1000012):
#    ran_str = ''.join(random.sample(string.ascii_letters, 6))
#    ran_str=("HR"+str(i)+ran_str)
#    Phone = ''.join(random.sample(string.digits, 8))
#    se.execute(insert,[(i),(ran_str),("Admin"),(Phone),('Admin12345@gmail.com'),('ce2ffefdca67bc04f70351cc651e8bc4'),('2023-02-08'),(1),('Fyp1'),('profile_pics/default.jpg')])
from datetime import date, timedelta, datetime
import random

d1 = date(2023, 1, 1)
d2 = date(2023, 2, 28)
delta = d2 - d1

currentDate = datetime.now().strftime("%Y-%m-%d")

for i in range(delta.days + 1):
    dat = d1 + timedelta(days=i)
    if dat == datetime.today().date():
        se.execute(InsertWork, ['Pending', dat, '100017', '18:00', '10:00', '09:45', '18:00'])
    elif dat >datetime.today().date():
        if random.random() < 0.73:
            se.execute(InsertWork, ['Pending', dat, '100017', None, None, None, None])
        else:
            se.execute(InsertWork, ['Off', dat, '100017', None, None, None, None])
    else:
        if random.random() < 0.65:
            se.execute(InsertWork, ['Pending', dat, '100017', '18:00', '10:00', '09:45', '18:00'])
        elif random.random() > 0.65 <= 0.85:
            se.execute(InsertWork, ['Off', dat, '100017', None, None, None, None])
        elif random.random() > 0.85:
            se.execute(InsertWork, ['MC', dat, '100017', '18:00', '10:00', '09:45', '18:00'])
conn.commit()
print("数据操作成功")
conn.close()

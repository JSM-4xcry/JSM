from PyQt5.uic import loadUi
from PyQt5.QtWidgets import *
from datetime import *
from PySide6.QtWidgets import QApplication, QWidget 
import subprocess
import xml.etree.ElementTree as xml

def test_m(months,year):
        to=[1,3,5,7,8,10,12]
        if months in  to:
             months=31
        elif months==2:
             if  year==365 :
                months=29
             else:
                months=28
        else:
             months=30
        return months 
def lm(year_days):
    day=0
    months=0
    while year_days>0:
        for i in range(1,13):
            days=test_m(i,2024)
        if year_days>=28:
            year_days-=days
            months+=1
        else:
            day=year_days+1
            year_days=0
    return months

def ld(year_days):
    day=0
    months=0
    while year_days>0:
        for i in range(1,13):
            days=test_m(i,2024)
        if year_days>=28:
            year_days-=days
            months+=1
        else:
            day=year_days+1
            year_days=0
    return day


def yd(bd,t,bm,ty,tm):
     bmrd=((test_m(bm,ty))-bd+1)
     days=1
     for i in range(bm,12):
         days+=test_m(i,ty)
     tyld=1    
     if tm<bm :
          for k in range (1,tm):
               tyld+=test_m(k,ty)               
     s=days+bmrd+tyld+t   
     return s   
def ald(by,ty,tm,l_years,td):
    aldoy=365*l_years
    for i in range(1,tm):
        alditm=tm-1*test_m(i,ty)
    x=test_m(bm,by)-bd
    y=0
    for k in range(bm+1,13):
        y+=test_m(k,by)
    s=aldoy+alditm+td+x+y
    return s
def calculate_age():
    global bm
    global bd
    global by
    x =w.by.text()
    y =w.bm.text()
    a =w.bd.text()
    by=int(x)
    bm=int(y)
    bd=int(a)
    birthday = date(by, bm, bd) 
    if by%4==0 and year%400==0:
        year=365
    else:
        year=364
    today = date.today()

    ty=today.year 
    tm=today.month
    td=today.day  
    l_years = today.year - birthday.year  - ((today.month, today.day) < (birthday.month, birthday.day))
    year_days=yd(bd,td,bm,ty,tm)
    lived_m=lm(year_days)
    lived_d=ld(year_days)
    r_months = abs( today.month- birthday.month) 
    r_days = abs( today.day-birthday.day)
    months=((l_years*12))+tm-1
    days=0
    for i in range(1,13):
        days+=test_m(i,ty)
    days=ald(by,ty,tm,l_years,td)
    hours=days*24
    weeks=days//7
    minutes=hours*60
    w.ly.setText(str(l_years))
    w.lm.setText(str(lived_m))
    w.ld.setText(str(lived_d))
    w.r_months.setText(str(r_months))
    w.r_days.setText(str(r_days))
    w.sy.setText(str(l_years))
    w.sm.setText(str(months))
    w.sw.setText(str(weeks))
    w.sd.setText(str(days))
    w.sh.setText(str(hours))
    w.smi.setText(str(minutes))
    
app=QApplication([])
form_class, base_class=PySide6Ui('calc.ui').load()
w=base_class()
form=form_class()
w.calculer.clicked.connect(calculate_age)
w.show()
app.exec_()





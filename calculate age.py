from datetime import *
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
def ald(ty,by):
    ReferenceError
def calculate_age(birthday):
    global l_years
    global lived_m
    global lived_d
    global months
    global days
    global weeks
    global r_months
    global r_days
    global year_days
    if by%4==0 and year%400==0:
        year=365
    else:
        year=364
    today = date.today()
    all_ld=
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
    weeks=days//7
    hours=days*24
by = 2006  
bm = 9
bd =25 
dateOfBirth = date(by, bm, bd)  
calculate_age(dateOfBirth)
print(l_years,lived_m,lived_d,r_months,r_days,months) 
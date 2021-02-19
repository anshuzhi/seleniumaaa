def get_days(year,month):
  if (month == 1 or month == 3 or month == 5 or month == 7 or month == 8 or month == 10 or month == 12):
      return 31
  elif (month == 4 or month == 6 or month == 9 or month == 11 ):
      return 30
  elif month == 2 and ((year % 4==0 and year % 100!=0) or (year % 400==0)):
      return 29
  else:
      return 28


def first_month_cost(year, month, day, n):
    this_month_days=get_days(year,month)
    pay_days=this_month_days-day+1
    if pay_days<=30:
        total_price=(n//30)*pay_days
    elif pay_days>30:
        total_price = n
    return total_price


total_price1=first_month_cost(2020, 8, 18, 60)
print(total_price1)#28
total_price2=first_month_cost(2020, 8, 1, 30)
print(total_price2)#30


def get_expire_date(year, month, day, n=1):
    this_mon_days = get_days(year, month)
    if n * 30 <= this_mon_days - (day - 1):
        alldays = day + n * 30 - 1
    elif n * 30 > this_mon_days - day:
        # month = month + 1
        alldays = n * 30 - (this_mon_days - day)
        while get_days(year, month) < alldays:
            alldays = alldays - get_days(year, month)
            if month < 12:
                month = month + 1
            else:
                month = month % 12
                year = year + 1
    return year, month, alldays

c=get_expire_date(2021,1,29,1)
d=get_expire_date(2021,12,3,1)
print(c)
print(d)


import  time

tss1 = '2013-10-10 23:40:00'
def get__D(year, month, day, n):
    tss1 = f"{year}-{month}-{day} 00:00:00"
    timeArray = time.strptime(tss1, "%Y-%m-%d %H:%M:%S")
    timeStamp = int(time.mktime(timeArray))
    res_timeStamp=timeStamp+(n*30*24*60*60)
    print(timeStamp)
    print(res_timeStamp)
    timeArray = time.localtime(int(res_timeStamp-1))
    otherStyleTime = time.strftime("%Y-%m-%d %H:%M:%S", timeArray)
    print(otherStyleTime)
get__D(2021,12,3,1)

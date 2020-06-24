import time;
import calendar;

localtime = time.localtime(time.time());
print("Local Current Time",localtime,"\n");

#format the time using asctime() method
fTime=time.asctime(localtime);
print("Local Time : ",fTime, "\n");

#Calendar of the month
cal = calendar.month(2020,6);
print(cal);
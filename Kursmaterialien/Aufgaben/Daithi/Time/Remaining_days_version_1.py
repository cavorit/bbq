from dateutil.easter import*
from dateutil.relativedelta import*
from datetime import datetime

now = datetime.now()
end_date = datetime(2016,2,22,16)
time_left = relativedelta(end_date,now)
print(" Time remaining at BBQ, %d month, %d days, %d hours and %d minutes"% 
      (time_left.months,time_left.days,time_left.hours,time_left.minutes))
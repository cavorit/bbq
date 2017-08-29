def date_diff(t2, t1): 
    return time.mktime(t2)-time.mktime(t1)

def date_compare(t1, t2):
    return (time.mktime(t1)<time.mktime(t2))

def date_duration_addition(t1, s):
    return time.mktime(time.mktime(t1)+s)

def date_sort(list_of_dates):
    x = []
    while(len(list_of_dates)):
            x.append(time.mktime(list_of_dates.pop()))
    while(len(x)):
            list_of_dates.append(time.mktime(x.pop()))
    return list_of_dates

            
            

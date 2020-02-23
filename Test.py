import pandas as pd

class Load_path():
    
    ### csv_path => The path of csv data
    def __init__(self, csv_path):
        self.csv_path = csv_path
        
class Load_data():
    def __init__(self, csv_path):
        self.csv_path = csv_path
        self.original_csv_data = pd.DataFrame()
        
    def Load_data(self):
        type_dict = {
            "1": str, 
            "2": str,
            "3": str
        }
        
        name_list = ['1', '2', '3']
        
        try:
            self.original_csv_data = pd.read_csv(self.csv_path, names=name_list, skiprows = [0], low_memory=False, dtype=type_dict)
            # name_ls = ['A', 'B', 'C', 'D', 'E', 'F'], names=name_ls, usecols=[1, 2, 3, 4, 5, 6], encoding='BIG5'
        
        ### Return failure message
        except FileNotFoundError as e:
            print(e)


import datetime as dt
import pytz

#create Taipei timezone
tz = pytz.timezone('Asia/Taipei')

d = dt.datetime.now()


### string=True, string_type 1 => '2020-02-23T23:16:27.345227+08:00', string_type 2 => '2020-02-23 23:16:27.345'
### string=False, datetime.datetime(2020, 2, 23, 23, 23, 49, 688241, tzinfo=<DstTzInfo 'Asia/Taipei' CST+8:00:00 STD>)
### time => datetime type

def UTC_time(time, string_type, string=False):
    tz = pytz.timezone('Asia/Taipei')
    if string and string_type == 1:
        time = tz.localize(time)
        time = time.isoformat()
        return time
    elif string and string_type == 2:
        time = tz.localize(time)
        time = dt.datetime.strftime(time,'%Y-%m-%d %H:%M:%S.%f')[:-3]
        return time
    else:
        return tz.localize(time)
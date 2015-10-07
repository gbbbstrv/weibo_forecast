import os
from datetime import *
delimiter = "\t"

def train_date_split(weibo_train_file_path, seperate_day, begin_date,weibo_train_five_file_path,weibo_train_last_file_path):
    weibo_train_file = open(weibo_train_file_path,encoding= 'utf-8')     # 打开weibo_train_data.txt 
    ffive = open(weibo_train_five_file_path,'w',encoding= 'utf-8') 
    flast = open(weibo_train_last_file_path,'w',encoding= 'utf-8') 
    interval_days = (seperate_day-begin_date).days
    for line in weibo_train_file:
        uid, mid, time, forward_count,comment_count, like_count, content = line.split(delimiter)         
        real_date=date(*parse_date(time))
        date_delta = (real_date - begin_date).days
        if interval_days<date_delta:
            flast.write(line)
        else:
            ffive.write(line)     
# 解析日期
def parse_date(raw_date):
    # entry_date = raw_date.decode("gbk")
    entry_date = raw_date
    year, month, day = entry_date.split(" ")[0].split("-")
    return int(year), int(month), int(day)
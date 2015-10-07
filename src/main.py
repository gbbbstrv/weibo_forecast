import os
from datetime import *
import time
from sort import *
from split import *
from features import *
from predict import *
from score import *

delimiter = "\t"

def dataset_input(weibo_train_file_path,weibo_predict_file_path):
    weibo_train_file = open(weibo_train_file_path)
    dataset_train = list(weibo_train_file)
    for i in range(len(dataset_train)):
        dataset_train[i] = [float(x) for x in dataset_train[i]]
    print(dataset_train)
    return dataset_train





SEPERATEDAY =date(2015,6, 30)
BEGINDAY = date(2015, 2, 1)
path=os.path.abspath(os.path.dirname(os.path.dirname(__file__)))+'\\data'
os.chdir(path)  ## change dir to '~/files'

weibo_train_file_path = "weibo_train_data.txt"
weibo_train_sort_path="weibo_train_data_sort.txt"
weibo_predict_file_path = "weibo_predict_data.txt"
weibo_predict_sort_path = "weibo_predict_data_sort.txt"
weibo_train_five_file_path = "weibo_train_five.txt"
weibo_train_last_file_path = "weibo_train_last.txt"
uid_features_str_file_path="uid_features_str.txt"
weibo_result_file_path="weibo_result.txt"


starttime = datetime.now()
generate_sortedfile(weibo_train_file_path,weibo_train_sort_path)
print("1.Train sort has been completed") 
generate_sortedfile(weibo_predict_file_path,weibo_predict_sort_path)
print ("2.Predict sort has been completed")
train_date_split(weibo_train_sort_path, SEPERATEDAY, BEGINDAY,weibo_train_five_file_path,weibo_train_last_file_path)
print ("3.Data segmentation has been completed")
uid_features(weibo_train_five_file_path,uid_features_str_file_path)
print ("4.User feature extraction has been completed")
weibo_predict(uid_features_str_file_path, weibo_train_last_file_path,weibo_result_file_path)
print ("5.Forecast has been completed")
score=score(weibo_result_file_path,weibo_train_last_file_path)
print ("6.The whole score is "+score)
endtime = datetime.now()
print ("Total running time: %f s" % (endtime - starttime).seconds)

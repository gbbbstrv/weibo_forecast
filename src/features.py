
import math
delimiter = "\t"

def uid_features(same_uid_train_file_path,uid_features_file_path):
    same_uid_train_file = open(same_uid_train_file_path,encoding= 'utf-8')   
    uid_features_str_file = open(uid_features_file_path, 'w',encoding= 'utf-8')
    uid_features = {'uid':"",              
                    'forward_count': 0,    
                     'comment_count': 0,    
                     'like_count': 0, 
                     'uid_time_count':0, 
                     'fc_median':0, 
                     'cc_median':0,
                     'lc_median':0, 
                     'fc_variance':0, 
                     'cc_variance':0,
                     'lc_variance':0,  
                     'fc_list':[], 
                     'cc_list':[],
                     'lc_list':[], 
                     } 
    firstline=same_uid_train_file.readline()
    pre_train_uid, pre_train_mid, pre_train_time, pre_train_forward_count, pre_train_comment_count, pre_train_like_count, pre_train_content =  firstline.split(delimiter) 
    same_uid_train_file.seek(0)
    for line in same_uid_train_file:
        train_uid, train_mid, train_time, train_forward_count, train_comment_count, train_like_count, train_content = line.split(delimiter)
        if  train_uid == pre_train_uid:
            uid_features['uid'] = train_uid
            uid_features['forward_count'] += int(train_forward_count)
            uid_features['comment_count'] += int(train_comment_count)
            uid_features['like_count'] +=  int(train_like_count)
            uid_features['uid_time_count'] +=1
            uid_features['fc_list'].append(int(train_forward_count))
            uid_features['cc_list'].append(int(train_comment_count))
            uid_features['lc_list'].append(int(train_like_count))
        if not train_uid == pre_train_uid:
            uid_features['fc_median']=median(uid_features['fc_list'])
            uid_features['cc_median']=median(uid_features['cc_list'])
            uid_features['lc_median']=median(uid_features['lc_list'])
            uid_features_str_file.write(get_uid_features_str(uid_features))
            uid_feature=initial_uid_features(uid_features)
            uid_features['uid'] = train_uid
            uid_features['forward_count'] += int(train_forward_count)
            uid_features['comment_count'] += int(train_comment_count)
            uid_features['like_count'] +=  int(train_like_count)
            uid_features['uid_time_count'] +=1
            uid_features['fc_list'].append(int(train_forward_count))
            uid_features['cc_list'].append(int(train_comment_count))
            uid_features['lc_list'].append(int(train_like_count))
        pre_train_uid=train_uid
    uid_features_str_file.write(get_uid_features_str(uid_features))  

def get_uid_features_str(uid_features):
    uid_features_str = str(uid_features["uid"]) + "\t" \
                                   + str(uid_features["fc_median"])+ "," \
                                   + str(uid_features["cc_median"])+ "," \
                                   + str(uid_features["lc_median"])+"\n"
    return uid_features_str

def initial_uid_features(uid_features):
    uid_features['uid']=""    
    uid_features['forward_count']=0    
    uid_features['comment_count']=0    
    uid_features['like_count']=0      
    uid_features['uid_time_count']=0   
    uid_features['fc_median']=0
    uid_features['cc_median']=0
    uid_features['lc_median']=0
    uid_features['fc_variance']=0
    uid_features['cc_variance']=0
    uid_features['lc_variance']=0
    uid_features['fc_list']=[]
    uid_features['cc_list']=[]
    uid_features['lc_list']=[]              
    return uid_features

def median(lst):
    if not lst:
        return 
    lst=sorted(lst)
    if len(lst)%2==1:
        return int(lst[len(lst)//2])
    else:
        return  int((lst[len(lst)//2-1]+lst[len(lst)//2])/2)




    
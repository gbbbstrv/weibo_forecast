
delimiter = "\t"

def weibo_predict(uid_features_str_file_path, weibo_predict_file_path,weibo_result_file_path):
    uid_features_str_file = open(uid_features_str_file_path,encoding= 'utf-8')   
    weibo_predict_file = open(weibo_predict_file_path,encoding= 'utf-8')   
    weibo_result_file = open(weibo_result_file_path,"w",encoding= 'utf-8')   
    table={}
    for line in open(uid_features_str_file_path,encoding= 'utf-8'):
        uid,values=line.split("\t")
        table[""+uid+""]=values
    for line in open(weibo_predict_file_path,encoding= 'utf-8'):
        uid=line.split(delimiter)[0]
        mid=line.split(delimiter)[1]
        if uid in table.keys():
            weibo_result_file.write(uid+"\t"+mid+"\t"+table[""+uid+""])
        else:
            weibo_result_file.write(uid+"\t"+mid+"\t"+str(0)+ ","+str(0)+ ","+str(0)+ "\n")

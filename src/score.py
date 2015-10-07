
delimiter = "\t"

def score(weibo_result_file_path,weibo_real_file_path):
    weibo_real_file = open(weibo_real_file_path,encoding= 'utf-8') 
    weibo_result_file = open(weibo_result_file_path,encoding= 'utf-8') 
    p1=0
    p2=0
    for line in weibo_real_file:
        uid, mid, time, fr,cr, lr, content = line.split(delimiter) 
        count=int(fr)+int(cr)+int(lr)
        if count>100:
            count=100
        result_line=weibo_result_file.readline()
        value=result_line.split(delimiter)[2]
        fp,cp,lp=value.split(",")
        df=(abs(float(fp)-float(fr)))/(float(fr)+5)
        dc=(abs(float(cp)-float(cr)))/(float(cr)+3)
        lc=(abs(float(lp)-float(lr)))/(float(lr)+3)
        precision=1-0.5*df-0.25*dc-0.25*lc
        sgn = lambda x: 1 if x > 0 else 0 if x < 0 else 0
        p1=p1+(count+1)*sgn(precision-0.8)
        p2=p2+(count+1)
    return str(p1/p2)
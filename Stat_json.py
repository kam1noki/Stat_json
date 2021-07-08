import os 

def get_list(dir,filelist):
    next_dir=dir
    if(os.path.isfile(dir)):  #判断该名是否为文件
        if('_gt.json' in dir):
            filelist.append(dir)
    elif os.path.isdir(dir):   #判断是否为文件夹
        for f in os.listdir(dir):  #依次读取当前路径下所有文件名
            next_dir=os.path.join(dir,f)   #将文件名添加到当前路径后
            get_list(next_dir,filelist)   #迭代
    return filelist

if __name__=="__main__":
    start_dir=input("请输入目标路径：")
    res_list=get_list(start_dir,[])
    print(len(res_list))
    for name in res_list:
        print(name)
        
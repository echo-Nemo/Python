#汉诺塔每次只能移动一个 
count=0
def func(n,src,dst,mid):
    global count
    if n==1:
        print( "{}:{}->{}".format(1,src,dst))
        count+=1
    else:
        #汉诺塔的移动是有顺序的 
        #将上面的n-1个移到mid上
       func(n-1,src,mid,dst)
       #把第n个移到目地柱上
       print("{}:{}->{}".format(n,src,dst))  
       #将mid中的n-1个移到src上
       func(n-1,mid,dst,src)
       count+=1
print(func(3,"a","c","b"))
##print(count)
  

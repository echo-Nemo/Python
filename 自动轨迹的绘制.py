import turtle as t
#制定画布
t.title("自动轨迹的绘制")
t.color("red")
t.pensize(4)

#读取数据
a_list=list()
text=open(r'C:\Users\hp\Desktop\文本.txt')
for line in text:
    #把行尾的换行符用空格代替
    line=line.replace("\n",'')
    #把数据分割成单独的字符串a
    a_list.append(list(map(eval,line.split(","))))#不加list 那就不能构成一个二维数组
    
text.close()
#自动绘制 列表看成是一个多位的数组 a_list=[[],[],[],]
for i in range(len(a_list)):
    #绘制的图形的颜色
    t.pencolor(a_list[i][3],a_list[i][4],a_list[i][5])
    #0左转 1右转
    if a_list[i][1]==0:
        t.left(a_list[i][2])
    else:
        t.right(a_list[i][2])
    #行走    
    t.fd(a_list[i][0])
    
    


#文本.txt 为一个文本文件 第0个值为长度，1个为方向，3，4，5表示的是RGB的颜色 见该列表中的文本文件



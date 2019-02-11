import wordcloud
import matplotlib
import jieba
f=open(r'C:\Users\hp\Documents\三国演义.txt',"r",encoding="utf-8")
t=f.read()
f.close()
lc=jieba.lcut(t)
txt=" ".join(lc)#词云使用空格进行连接
###词云的形状
##mk=imread("pic.png")
w=wordcloud.WordCloud(font_path="msyh.ttc",background_color="white",max_words=10)
w.generate(txt)
w.to_file("text.jpg")#图片显示在存放代码的地方
print("success")



import turtle
import time
def drawLine(draw):#绘制数码管段
    #如果要绘制 就让海归落下 否者飞起来
    turtle.pendown()if draw else turtle.penup()
    turtle.fd(40)#一段管的长度
    drawDistance()
    turtle.right(90)
    
#每个管间有个空格
def drawDistance():
    turtle.penup()
    turtle.fd(5)
    turtle.pendown()
    
#要绘制的日期    
def drawDigit(digit):
    #7形数码管从中间开始绘制
    #数码管的下面4个管的
    #g
    drawLine(True)if digit in [2,3,4,5,6,8,9] else drawLine(False)
    #c
    drawLine(True)if digit in [0,1,3,4,5,6,7,8,9] else drawLine(False)
    #d
    drawLine(True)if digit in [0,2,3,5,6,8,9] else drawLine(False)
    #e
    drawLine(True)if digit in [0,2,6,8] else drawLine(False)
    #数码管的三面三需要转左转90 不然会重复绘制下面的四段管
    turtle.left(90)
    #f
    drawLine(True)if digit in [0,4,5,6,8,9] else drawLine(False)
    #a
    drawLine(True)if digit in [0,2,3,5,7,8,9] else drawLine(False)
    #b
    drawLine(True)if digit in [0,1,2,3,4,7,8,9] else drawLine(False)
    turtle.left(180)
    
    #drawDistance()
    #绘制下一个数码管
    turtle.penup()
    turtle.fd(40)
    
#获取时间
def  drawDate():
    #获取计算机可以处理的时间
    data=time.gmtime()
    #对日期进行格式化处理
    for i in time.strftime("%Y-%m*%d&",data):
        turtle.pensize(3)
        if i =="-":
            turtle.pencolor("red")
            turtle.write("年")
            turtle.fd(15)
        elif i=="*":
            turtle.pencolor("green")
            turtle.write("月")
            turtle.fd(15)
        elif i=="&":
            turtle.pencolor("blue")
            turtle.write("日")
            turtle.fd(15)
        else:
            drawDigit(eval(i))

        
def main():
    turtle.speed(10)
    turtle.penup()
    turtle.fd(-300)
    drawDate()
    turtle.hideturtle()
    turtle.done
    
if __name__=="__main__":
    main()
    
    
    
    

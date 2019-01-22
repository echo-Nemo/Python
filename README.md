# Python
Python中树的画法
import turtle as t
import random

def tree(LanchLen,Angle):
        if LanchLen>10:
            #树干
            t.forward(LanchLen)
            #右边的树枝
            t.right(Angle)
            #继续画直到树枝的长度小于5
            tree(LanchLen-10,Angle)

            #左边的树枝
            t.left(2*Angle)#偏转的角度 先回到开始点方位 在左转一个角度 2*Angle
            tree(LanchLen-10,Angle)

            t.rt(Angle) #转到正向上的方向

            if LanchLen<=40:
            #树叶
                t.pencolor("green")
            else:
                t.pencolor("brown")

                ##回退很重要##
                #回画 到上一层
            t.backward(LanchLen)
                          
def main(): 
        #确定开始的位置
        t.pu()
        t.left(90)#先把方向左转90
        t.backward(200)#把起点放到低端
        t.pd()
        
        #树干
        t.color("brown")
        #树枝的最大长度  偏转角度
        tree(80,30)
        
if __name__=="__main__":
    main()

    
    

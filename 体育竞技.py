from random import random

#友善的提示
def Print():
    print("该程序是模拟某种体育竞技比赛")
    print("假设选手的能力值在0-1之间")
    
#输入信息的函数
def GetImformation():
    Amax=eval(input("请输入A的能力值"))
    Bmax=eval(input("请输入B的能力值"))
    N=eval(input("请输入比赛的场数"))
    return Amax,Bmax,N
        
#判断游戏是否结束        
def GameOver(ScoreA,ScoreB):
    if ScoreA==15 or ScoreB==15:
        return True
    else:
        return False
#进行1场比赛
def SimOnegame(PowA,PowB):
        scoreA,scoreB=0,0
        #假设A发球
        Serving='A'
        #游戏没有结束的情况下
        while not GameOver(scoreA,scoreB):
                if Serving=='A':
                    if random()<PowA:# random()随机模拟B的能力值
                        scoreA+=1
                    else:
                        Serving='B'
                if Serving=='B':
                     if random()<PowB:# random()随机模拟B的能力值
                          scoreB+=1
                     else:
                        Serving='A'
        return scoreA,scoreB

#进行n场比赛
def SimNgame(N,PowA,PowB):
    #赢得场数
    winA,winB=0,0
    for i in range(N):
        #每一场的分数
        ScoreA,ScoreB=SimOnegame(PowA,PowB)
        if ScoreA>ScoreB:
            winA+=1
        else:
            winB+=1
    return winA,winB

def Summary(winA,winB):
    n=winA+winB
    print("比赛开始，共有{}场比赛".format(n))
    print("选手A获胜{}场,占比例{:0.1%}".format(winA,winA/n))
    print("选手B获胜{}场,占比例{:0.1%}".format(winB,winB/n))
    
def main():
    Print()
    a,b,n=GetImformation()
    winA,winB=SimNgame(n,a,b)
    Summary(winA,winB)
    
main()    

                
                
    

    
    
    

    

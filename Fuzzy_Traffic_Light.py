# -*- coding = utf-8 -*-
# @Time : 2022/11/17 17:22
# @Author : 决明子
# @File : justtry.py
# @Software : PyCharm


fuzzyRules = [[['minimal', 'minimal'], 'short'], [['minimal', 'light'], 'short'], [['minimal', 'average'], 'medium'],
              [['minimal', 'heavy'], 'long'], [['minimal', 'excess'], 'long'],

              [['light', 'minimal'], 'short'], [['light', 'light'], 'short'], [['light', 'average'], 'medium'],
              [['light', 'heavy'], 'medium'], [['light', 'excess'], 'long'],

              [['average', 'minimal'], 'short'], [['average', 'light'], 'medium'], [['average', 'average'], 'medium'],
              [['average', 'heavy'], 'long'], [['average', 'excess'], 'long'],

              [['heavy', 'minimal'], 'medium'], [['heavy', 'light'], 'medium'], [['heavy', 'average'], 'long'],
              [['heavy', 'heavy'], 'long'], [['heavy', 'excess'], 'long'],

              [['standstill', 'minimal'], 'medium'], [['standstill', 'light'], 'long'],
              [['standstill', 'average'], 'long'],
              [['standstill', 'heavy'], 'long'], [['standstill', 'excess'], 'long']]

import sys

def main():
    print('\nStart Program\n')
    OnComingCar = input("请输入主街车辆： ")
    WaitingCar = input("请输入侧街车辆： ")
    OnComingCar=int(OnComingCar)
    WaitingCar=int(WaitingCar)
    FuzzyControlTable=[]
    FuzzyControlTubiao=[]



    #OnComingCar的隶属度函数
    if OnComingCar>=0 and OnComingCar<=7.5:
        miuone = 1
        miutwo = 1
        FuzzyControlTable = [fuzzyRules[0], fuzzyRules[5], fuzzyRules[10], fuzzyRules[15], fuzzyRules[20]]
    if OnComingCar>=7.5 and OnComingCar<=9:
        miuone = 2*(15-OnComingCar)/15
        miutwo = 2*(15-OnComingCar)/15
        FuzzyControlTable = [fuzzyRules[0], fuzzyRules[5], fuzzyRules[10], fuzzyRules[15], fuzzyRules[20]]
    if OnComingCar>=10 and OnComingCar<=15:
        miuone=2*(15-OnComingCar)/15
        miutwo=2*(OnComingCar-10)/15
        FuzzyControlTable = [fuzzyRules[0], fuzzyRules[1], fuzzyRules[5], fuzzyRules[6], fuzzyRules[10],fuzzyRules[11], fuzzyRules[15], fuzzyRules[16], fuzzyRules[20], fuzzyRules[21]]
    if OnComingCar >= 16and OnComingCar <= 17.5:
        miuone = 2 * (OnComingCar - 10) / 15
        miutwo = 2 * (OnComingCar - 10) / 15
        FuzzyControlTable = [fuzzyRules[1], fuzzyRules[6], fuzzyRules[11], fuzzyRules[16], fuzzyRules[21]]
    if OnComingCar >= 17.5and OnComingCar <= 19:
        miuone = 2 * (25-OnComingCar) / 15
        miutwo = 2 * (25-OnComingCar) / 15
        FuzzyControlTable = [fuzzyRules[1], fuzzyRules[6], fuzzyRules[11], fuzzyRules[16], fuzzyRules[21]]
    if OnComingCar>=20 and OnComingCar<=25:
        miuone = 2 * (25 - OnComingCar) / 15
        miutwo = 2 * (OnComingCar-20) / 15
        FuzzyControlTable =[fuzzyRules[1], fuzzyRules[2], fuzzyRules[6], fuzzyRules[7], fuzzyRules[11], fuzzyRules[12], fuzzyRules[16], fuzzyRules[17], fuzzyRules[21],fuzzyRules[22]]
    if OnComingCar >= 26 and OnComingCar <= 27.5:
        miuone = 2 * (OnComingCar - 20) / 15
        miutwo = 2 * (OnComingCar - 20) / 15
        FuzzyControlTable = [fuzzyRules[2], fuzzyRules[7], fuzzyRules[12], fuzzyRules[17], fuzzyRules[22]]
    if OnComingCar >= 27.5 and OnComingCar <= 29:
        miuone = 2 * (35 - OnComingCar) / 15
        miutwo = 2 * (35 - OnComingCar) / 15
        FuzzyControlTable = [fuzzyRules[2], fuzzyRules[7], fuzzyRules[12], fuzzyRules[17], fuzzyRules[22]]
    if OnComingCar >= 30 and OnComingCar <= 35:
        miuone = 2 * (35 - OnComingCar) / 15
        miutwo = 2 * (OnComingCar - 30) / 15
        FuzzyControlTable=[fuzzyRules[2],fuzzyRules[3],fuzzyRules[7],fuzzyRules[8],fuzzyRules[12],fuzzyRules[13],fuzzyRules[17],fuzzyRules[18],fuzzyRules[22],fuzzyRules[23]]
    if OnComingCar >= 36 and OnComingCar <= 37.5:
        miuone = 2 * (OnComingCar - 30) / 15
        miutwo = 2 * (OnComingCar - 30) / 15
        FuzzyControlTable = [fuzzyRules[3], fuzzyRules[8], fuzzyRules[13], fuzzyRules[18], fuzzyRules[23]]
    if OnComingCar >= 37.5 and OnComingCar <= 39:
        miuone = 2 * (45-OnComingCar) / 15
        miutwo = 2 * (45-OnComingCar) / 15
        FuzzyControlTable = [fuzzyRules[3], fuzzyRules[8], fuzzyRules[13], fuzzyRules[18], fuzzyRules[23]]
    if OnComingCar >= 40 and OnComingCar <= 45:
        miuone = 2 * (45 - OnComingCar) / 15
        miutwo = (OnComingCar-40) / 10
        FuzzyControlTable = [fuzzyRules[3], fuzzyRules[4], fuzzyRules[8], fuzzyRules[9], fuzzyRules[13], fuzzyRules[14], fuzzyRules[18], fuzzyRules[19], fuzzyRules[23],fuzzyRules[24]]
    if OnComingCar >= 46 and OnComingCar <= 50:
        miuone = (OnComingCar - 40) / 10
        miutwo = (OnComingCar - 40) / 10
        FuzzyControlTable = [fuzzyRules[4], fuzzyRules[9], fuzzyRules[14], fuzzyRules[19], fuzzyRules[24]]
    if OnComingCar >= 50 :
        miuone = 1
        miutwo = 1
        FuzzyControlTable = [fuzzyRules[4], fuzzyRules[9], fuzzyRules[14], fuzzyRules[19], fuzzyRules[24]]



    #waitingcar的隶属度函数
    if WaitingCar >= 0 and WaitingCar <= 7.5:
        miuthree = 1
        miufour = 1
        FuzzyControlTubiao = [fuzzyRules[0], fuzzyRules[1], fuzzyRules[2], fuzzyRules[3], fuzzyRules[4]]
    if WaitingCar >= 7.5 and WaitingCar <= 9:
        miuthree = 2 * (15 - WaitingCar) / 15
        miufour = 2 * (15 - WaitingCar) / 15
        FuzzyControlTubiao = [fuzzyRules[0], fuzzyRules[1], fuzzyRules[2], fuzzyRules[3], fuzzyRules[4]]
    if WaitingCar >= 10 and WaitingCar <= 15:
        miuthree = 2 * (15 - WaitingCar) / 15
        miufour = 2 * (WaitingCar - 10) / 15
        FuzzyControlTubiao=[fuzzyRules[0],fuzzyRules[1],fuzzyRules[2],fuzzyRules[3],fuzzyRules[4],fuzzyRules[5],fuzzyRules[6],fuzzyRules[7],fuzzyRules[8],fuzzyRules[9]]
    if WaitingCar >= 16 and WaitingCar <= 17.5:
        miuthree = 2 * (WaitingCar - 10) / 15
        miufour = 2 * (WaitingCar - 10) / 15
        FuzzyControlTubiao = [fuzzyRules[5], fuzzyRules[6], fuzzyRules[7], fuzzyRules[8], fuzzyRules[9]]
    if WaitingCar >= 17.5 and WaitingCar <= 19:
        miuthree = 2 * (25 - WaitingCar) / 15
        miufour = 2 * (25 - WaitingCar) / 15
        FuzzyControlTubiao = [fuzzyRules[5], fuzzyRules[6], fuzzyRules[7], fuzzyRules[8], fuzzyRules[9]]
    if WaitingCar >= 20 and WaitingCar <= 25:
        miuthree = 2 * (25 - WaitingCar) / 15
        miufour = 2 * (WaitingCar - 20) / 15
        FuzzyControlTubiao = [fuzzyRules[5], fuzzyRules[6], fuzzyRules[7], fuzzyRules[8], fuzzyRules[9],fuzzyRules[10], fuzzyRules[11], fuzzyRules[12], fuzzyRules[13], fuzzyRules[14]]
    if WaitingCar >= 26 and WaitingCar <= 27.5:
        miuthree = 2 * (WaitingCar - 20) / 15
        miufour = 2 * (WaitingCar - 20) / 15
        FuzzyControlTubiao = [fuzzyRules[10], fuzzyRules[11], fuzzyRules[12], fuzzyRules[13], fuzzyRules[14]]
    if WaitingCar >= 27.5 and WaitingCar <= 29:
        miuthree = 2 * (35 - WaitingCar) / 15
        miufour = 2 * (35 - WaitingCar) / 15
        FuzzyControlTubiao = [fuzzyRules[10], fuzzyRules[11], fuzzyRules[12], fuzzyRules[13], fuzzyRules[14]]
    if WaitingCar >= 30 and WaitingCar <= 35:
        miuthree = 2 * (35 - WaitingCar) / 15
        miufour = 2 * (WaitingCar - 30) / 15
        FuzzyControlTubiao = [fuzzyRules[10], fuzzyRules[11], fuzzyRules[12], fuzzyRules[13], fuzzyRules[14],fuzzyRules[15], fuzzyRules[16], fuzzyRules[17], fuzzyRules[18], fuzzyRules[19]]
    if WaitingCar >= 36 and WaitingCar <= 37.5:
        miuthree = 2 * (WaitingCar - 30) / 15
        miufour = 2 * (WaitingCar - 30) / 15
        FuzzyControlTubiao = [fuzzyRules[15], fuzzyRules[16], fuzzyRules[17], fuzzyRules[18], fuzzyRules[19]]
    if WaitingCar >= 37.5 and WaitingCar <= 39:
        miuthree = 2 * (45 - WaitingCar) / 15
        miufour = 2 * (45 - WaitingCar) / 15
        FuzzyControlTubiao = [fuzzyRules[15], fuzzyRules[16], fuzzyRules[17], fuzzyRules[18], fuzzyRules[19]]
    if WaitingCar >= 40 and WaitingCar <= 45:
        miuthree = 2 * (45 - WaitingCar) / 15
        miufour = (WaitingCar - 40) / 10
        FuzzyControlTubiao = [fuzzyRules[15], fuzzyRules[16], fuzzyRules[17], fuzzyRules[18], fuzzyRules[19],fuzzyRules[20], fuzzyRules[21], fuzzyRules[22], fuzzyRules[23], fuzzyRules[24]]
    if WaitingCar >= 46 and WaitingCar <= 50:
        miuthree = (WaitingCar - 40) / 10
        miufour = (WaitingCar - 40) / 10
        FuzzyControlTubiao = [fuzzyRules[20], fuzzyRules[21], fuzzyRules[22], fuzzyRules[23], fuzzyRules[24]]
    if WaitingCar >= 50:
        miuthree = 1
        miufour = 1
        FuzzyControlTubiao = [fuzzyRules[20], fuzzyRules[21], fuzzyRules[22], fuzzyRules[23], fuzzyRules[24]]

    #根据给出的信息求出的隶属度
    miuone=round(miuone,2)
    miutwo = round(miutwo, 2)
    miuthree = round(miuthree, 2)
    miufour = round(miufour, 2)
    print("等待车辆隶属度",miuthree,miufour,"行驶车辆隶属度",miuone,miutwo)
    print("触发的规则",[x for x in FuzzyControlTubiao if x in FuzzyControlTable])



    if len([x for x in FuzzyControlTubiao if x in FuzzyControlTable]) ==4:
        Totalshuchu=[min(miuone,miuthree),min(miutwo, miuthree),min(miuone, miufour),min(miutwo, miufour)]
        print("规则匹配",flatten([x for x in FuzzyControlTubiao if x in FuzzyControlTable])[0],
              flatten([x for x in FuzzyControlTubiao if x in FuzzyControlTable])[1],
              flatten([x for x in FuzzyControlTubiao if x in FuzzyControlTable])[2],
              flatten([x for x in FuzzyControlTubiao if x in FuzzyControlTable])[3])
        print("规则前提可信度",Totalshuchu)
        if flatten([x for x in FuzzyControlTubiao if x in FuzzyControlTable])[0]==flatten([x for x in FuzzyControlTubiao if x in FuzzyControlTable])[1]:
            if flatten([x for x in FuzzyControlTubiao if x in FuzzyControlTable])[0]==flatten([x for x in FuzzyControlTubiao if x in FuzzyControlTable])[2]:
                if flatten([x for x in FuzzyControlTubiao if x in FuzzyControlTable])[0]==flatten([x for x in FuzzyControlTubiao if x in FuzzyControlTable])[3]:
                    choose='0123'
                    zuidalishu=max(Totalshuchu[0], Totalshuchu[1], Totalshuchu[2], Totalshuchu[3])
                    Timechoose=flatten([x for x in FuzzyControlTubiao if x in FuzzyControlTable])[0]
                else:
                    choose='012'
                    zuidalishu=max(Totalshuchu[0], Totalshuchu[1], Totalshuchu[2])
                    Timechoose = flatten([x for x in FuzzyControlTubiao if x in FuzzyControlTable])[0]
                    leftchooselishu = Totalshuchu[3]
                    leftchoose=flatten([x for x in FuzzyControlTubiao if x in FuzzyControlTable])[3]
            elif flatten([x for x in FuzzyControlTubiao if x in FuzzyControlTable])[0]==flatten([x for x in FuzzyControlTubiao if x in FuzzyControlTable])[3]:
                choose='013'
                zuidalishu=max(Totalshuchu[0], Totalshuchu[1], Totalshuchu[3])
                Timechoose = flatten([x for x in FuzzyControlTubiao if x in FuzzyControlTable])[0]
                leftchooselishu = Totalshuchu[2]
                leftchoose = flatten([x for x in FuzzyControlTubiao if x in FuzzyControlTable])[2]
            else:
                choose='01'
                zuidalishu=max(Totalshuchu[0], Totalshuchu[1])
                Timechoose = flatten([x for x in FuzzyControlTubiao if x in FuzzyControlTable])[0]
        elif flatten([x for x in FuzzyControlTubiao if x in FuzzyControlTable])[0]==flatten([x for x in FuzzyControlTubiao if x in FuzzyControlTable])[2]:
            if flatten([x for x in FuzzyControlTubiao if x in FuzzyControlTable])[0]==flatten([x for x in FuzzyControlTubiao if x in FuzzyControlTable])[3]:
                choose='023'
                zuidalishu=max(Totalshuchu[0], Totalshuchu[2], Totalshuchu[3])
                Timechoose = flatten([x for x in FuzzyControlTubiao if x in FuzzyControlTable])[0]
                leftchooselishu = Totalshuchu[1]
                leftchoose = flatten([x for x in FuzzyControlTubiao if x in FuzzyControlTable])[1]
            else:
                choose='02'
                zuidalishuone=Totalshuchu[0]
                zuidalishutwo=Totalshuchu[1]
                Timechooseone = flatten([x for x in FuzzyControlTubiao if x in FuzzyControlTable])[0]
                Timechoosetwo = flatten([x for x in FuzzyControlTubiao if x in FuzzyControlTable])[1]
                leftchooseone = flatten([x for x in FuzzyControlTubiao if x in FuzzyControlTable])[1]
                leftchoosetwo = flatten([x for x in FuzzyControlTubiao if x in FuzzyControlTable])[3]
                leftchooselishuone = Totalshuchu[1]
                leftchooselishutwo = Totalshuchu[3]
        elif flatten([x for x in FuzzyControlTubiao if x in FuzzyControlTable])[0]==flatten([x for x in FuzzyControlTubiao if x in FuzzyControlTable])[3]:
            choose='03'
            zuidalishu=max(Totalshuchu[0], Totalshuchu[3])
            Timechoose = flatten([x for x in FuzzyControlTubiao if x in FuzzyControlTable])[0]
        elif flatten([x for x in FuzzyControlTubiao if x in FuzzyControlTable])[1]==flatten([x for x in FuzzyControlTubiao if x in FuzzyControlTable])[2]:
            if flatten([x for x in FuzzyControlTubiao if x in FuzzyControlTable])[1]==flatten([x for x in FuzzyControlTubiao if x in FuzzyControlTable])[3]:
                choose='123'
                zuidalishu=max(Totalshuchu[1], Totalshuchu[2], Totalshuchu[3])
                Timechoose = flatten([x for x in FuzzyControlTubiao if x in FuzzyControlTable])[1]
                leftchooselishu = Totalshuchu[0]
                leftchoose = flatten([x for x in FuzzyControlTubiao if x in FuzzyControlTable])[0]
            else:
                choose='12'
                zuidalishu=max(Totalshuchu[1], Totalshuchu[2])
                Timechoose = flatten([x for x in FuzzyControlTubiao if x in FuzzyControlTable])[1]
        elif flatten([x for x in FuzzyControlTubiao if x in FuzzyControlTable])[1]==flatten([x for x in FuzzyControlTubiao if x in FuzzyControlTable])[3]:
            choose='13'
            zuidalishu=max(Totalshuchu[1], Totalshuchu[3])
            Timechoose = flatten([x for x in FuzzyControlTubiao if x in FuzzyControlTable])[1]
        elif flatten([x for x in FuzzyControlTubiao if x in FuzzyControlTable])[2]==flatten([x for x in FuzzyControlTubiao if x in FuzzyControlTable])[3]:
            choose='23'
            zuidalishu=max(Totalshuchu[2], Totalshuchu[3])
            Timechoose = flatten([x for x in FuzzyControlTubiao if x in FuzzyControlTable])[2]
        else:
            choose='none'

        if len(choose)==3:
            print("绿灯时间1",Outputfan(Timechoose, zuidalishu))
            print("绿灯时间2",Outputfan(leftchoose,leftchooselishu))
            print('最终结果',(Outputfan(Timechoose,zuidalishu)+Outputfan(leftchoose,leftchooselishu))/2)
        elif len(choose)==2:
            print("绿灯时间1",Outputfan(Timechooseone, zuidalishuone))
            print("绿灯时间2",Outputfan(leftchooseone, leftchooselishuone))
            print('最终结果', (Outputfan(Timechooseone, zuidalishuone) + Outputfan(Timechoosetwo, zuidalishutwo)+Outputfan(leftchooseone, leftchooselishuone)+Outputfan(leftchoosetwo, leftchooselishutwo)) / 4)


    if len([x for x in FuzzyControlTubiao if x in FuzzyControlTable]) ==1:
        Totalshuchu = [min(miuone, miuthree)]
        print("规则匹配",flatten([x for x in FuzzyControlTubiao if x in FuzzyControlTable])[0])
        print("规则前提可信度", Totalshuchu)
        zuidalishu=Totalshuchu[0]
        Timechoose = flatten([x for x in FuzzyControlTubiao if x in FuzzyControlTable])[0]
        print('最终结果',Outputfan(Timechoose,zuidalishu))
    if len([x for x in FuzzyControlTubiao if x in FuzzyControlTable]) ==2:
        Totalshuchu=[min(miuone,miuthree),min(miutwo, miufour)]
        print("规则匹配",flatten([x for x in FuzzyControlTubiao if x in FuzzyControlTable])[0],
              flatten([x for x in FuzzyControlTubiao if x in FuzzyControlTable])[1])
        print("规则前提可信度", Totalshuchu)
        if flatten([x for x in FuzzyControlTubiao if x in FuzzyControlTable])[0]==flatten([x for x in FuzzyControlTubiao if x in FuzzyControlTable])[1]:
            zuidalishu=max(Totalshuchu[0],Totalshuchu[1])
            Timechoose=flatten([x for x in FuzzyControlTubiao if x in FuzzyControlTable])[0]
            print('最终结果',Outputfan(Timechoose,zuidalishu))
        else:
            zuidalishuone = Totalshuchu[0]
            zuidalishutwo = Totalshuchu[1]
            Timechooseone = flatten([x for x in FuzzyControlTubiao if x in FuzzyControlTable])[0]
            Timechoosetwo = flatten([x for x in FuzzyControlTubiao if x in FuzzyControlTable])[1]
            print('最终结果',((Outputfan(Timechooseone,zuidalishuone)+Outputfan(Timechoosetwo,zuidalishutwo))/2))


def Outputfan(canshusan,miumiu):
    miumiuone=int()
    miumiutwo = int()
    if canshusan=='short':
        miumiuone=75-25*miumiu
        miumiutwo = 75 - 25 * miumiu
    elif canshusan=='medium':
        miumiuone = miumiu * 37.5 + 50
        miumiutwo = 125 - 37.5 * miumiu
    elif canshusan=='long':
        miumiuone= 50 * miumiu + 100
        miumiutwo = 50 * miumiu + 100
    zuida = max(miumiuone, miumiutwo)
    return zuida


def yingsheone(canshuone):
    canshuA=[]
    if canshuone>=0and canshuone<=9:
        canshuA=['minimal']
    if canshuone>=10and canshuone<=15:
        canshuA = ['minimal','light']
    if canshuone>=16and canshuone<=19:
        canshuA = ['light']
    if canshuone>=20and canshuone<=25:
        canshuA = ['light','average']
    if canshuone>=26and canshuone<=29:
        canshuA = ['average']
    if canshuone>=30and canshuone<=35:
        canshuA = ['average','heavy']
    if canshuone>=36and canshuone<=39:
        canshuA = ['heavy']
    if canshuone>=40and canshuone<=45:
        canshuA = ['heavy','standstill']
    if canshuone>=46:
        canshuA = ['standstill']
    return canshuA

def yingshetwo(canshutwo):
    canshuB = []
    if canshutwo >= 0 and canshutwo <= 9:
        canshuB = ['minimal']
    if canshutwo >= 10 and canshutwo <= 15:
        canshuB = ['minimal', 'light']
    if canshutwo >= 16 and canshutwo <= 19:
        canshuB = ['light']
    if canshutwo >= 20 and canshutwo <= 25:
        canshuB = ['light', 'average']
    if canshutwo >= 26 and canshutwo <= 29:
        canshuB = ['average']
    if canshutwo >= 30 and canshutwo <= 35:
        canshuB = ['average', 'heavy']
    if canshutwo >= 36 and canshutwo <= 39:
        canshuB = ['heavy']
    if canshutwo >= 40 and canshutwo <= 45:
        canshuB = ['heavy', 'excess']
    if canshutwo >= 46:
        canshuB = ['excess']
    return canshuB

def flatten(lst):
    result = []
    while True:
        temp_lst = []
        finish_flag = True
        for i in lst:
            if isinstance(i, list):
                finish_flag = False
                temp_lst.extend(i)
            else:
                result.append(i)
        if finish_flag:
            break
        lst = temp_lst
    return result


if __name__ == '__main__':
    main()
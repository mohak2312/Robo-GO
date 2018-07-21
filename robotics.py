import math
import positions as p
import ir3_base as ir
import time
import copy


filepath="c:/Users/Asus/Documents/Prolog/data.txt"
board=[]
b=1
lastboard=['-' for i in range(25)]
ir.open_port()
#pos={'0':p.pos0(),'1':p.pos1(),'2':p.pos2(),'3':p.pos3(),'4':p.pos4(),'5':p.pos5(),'6':p.pos6(),'7':p.pos7(),'8':p.pos8(),'9':p.pos9(),'10':p.pos10(),'11':p.pos11(),'12':p.pos12(),'13':p.pos13(),'14':p.pos14(),'15':p.pos15(),'16':p.pos16(),'17':p.pos17(),'18':p.pos18(),'19':p.pos19(),'20':p.pos20(),'21':p.pos21(),'22':p.pos22(),'23':p.pos23(),'24':p.pos24()}


p.start_pos_1()
#time.sleep(1)
p.start_pos_2()
#print(len(lastboard))
print(lastboard)
robot_1=[]
robot_2=[]
i=0

'''
ir.two(5)
p.pickup_b2()
time.sleep(1)
ir.two(5)
p.pos24()
#time.sleep(1)
ir.five(56.5)
#ir.seven(-20)
time.sleep(1)
'''


def goto(i):
    if(i==0):p.pos0()
    if(i==1):p.pos1()
    if(i==2):p.pos2()
    if(i==3):p.pos3()
    if(i==4):p.pos4()
    if(i==5):p.pos5()
    if(i==6):p.pos6()
    if(i==7):p.pos7()
    if(i==8):p.pos8()
    if(i==9):p.pos9()
    if(i==10):p.pos10()
    if(i==11):p.pos11()
    if(i==12):p.pos12()
    if(i==13):p.pos13()
    if(i==14):p.pos14()
    if(i==15):p.pos15()
    if(i==16):p.pos16()
    if(i==17):p.pos17()
    if(i==18):p.pos18()
    if(i==19):p.pos19()
    if(i==20):p.pos20()
    if(i==21):p.pos21()
    if(i==22):p.pos22()
    if(i==23):p.pos23()
    if(i==24):p.pos24()

while(1):
    with open(filepath) as f:
        lines = f.read()
        print('new board',lines)
        for char in lines:
            if(char=='x' or char=='o' or char=='-'):
                board.append(char)
                if(char != lastboard[i]):
                    if(i<15):
                        
                        robot_1.append(i)
                        if(char=='x' and lastboard[i]=='-'):
                            ir.seven(-20)
                            p.pickup_w1()
                            time.sleep(0.5)
                            ir.seven(-20)
                            goto(i)
                            #time.sleep(1)
                            ir.ten(-73.3)
                            #ir.seven(-20)
                            #time.sleep(0.5)
                            p.start_pos_1()
                        if(char=='o' and lastboard[i]=='-'):
                            ir.seven(-20)
                            p.pickup_b1()
                            ir.seven(-20)
                            goto(i)
                            ir.ten(-73.3)
                            #time.sleep(0.5)
                            p.start_pos_1()
                            
                        if(char=='-' and lastboard[i]=='x'):
                            ir.seven(-20)
                            ir.ten(-73)
                            goto(i)
                            ir.ten(-98)
                            ir.seven(-20)
                            p.place_b1()
                            #time.sleep(0.5)
                            p.start_pos_1()
                        if(char=='-' and lastboard[i]=='o'):
                            ir.seven(-20)
                            ir.ten(-73)
                            goto(i)
                            ir.ten(-98)
                            ir.seven(-20)
                            p.place_w1()
                            #time.sleep(0.5)
                            p.start_pos_1()
                    else:
                        robot_2.append(i)
                        if(char=='x' and lastboard[i]=='-'):
                            ir.two(-5)
                            p.pickup_b2()
                            #time.sleep(0.3)
                            ir.two(5)
                            goto(i)
                            #time.sleep(1)
                            ir.five(56.5)
                            #ir.seven(-20)
                            #time.sleep(0.5)
                            p.start_pos_2()
                        if(char=='o' and lastboard[i]=='-'):
                            ir.two(-5)
                            p.pickup_w2()
                            #time.sleep(0.3)
                            ir.two(5)
                            goto(i)
                            ir.five(56.5)
                            #time.sleep(0.5)
                            p.start_pos_2()
                        if(char=='-' and lastboard[i]=='x'):
                            ir.two(-5)
                            ir.five(56.5)
                            goto(i)
                            ir.five(91.3)
                            #time.sleep(0.3)
                            ir.two(5)
                            p.place_b2()
                            p.start_pos_2()
                            #time.sleep(0.5)
                        if(char=='-' and lastboard[i]=='o'):
                            ir.two(-5)
                            ir.five(56.5)
                            goto(i)
                            ir.five(91.5)
                            #time.sleep(0.3)
                            ir.two(5)
                            p.place_w2()
                            #time.sleep(0.5)
                            p.start_pos_2()
                        #p.start_pos_2()
                        #p.start_pos_1()
                i=i+1         
    

    #p.start_pos_1()
    #p.start_pos_2()
    lastboard=[]
    print(lastboard)
    lastboard=board
    board=[]
    i=0
    print("lastboard :",lastboard)

ir.close_port()

#for i in range(counter):
    
  

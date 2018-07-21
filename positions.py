import ir3_base as ir
import time


def int_pos_1():
    ir.seven(-10)
    ir.six(-93.1)
    ir.seven(6.3)
    ir.eight(-35)
    ir.nine(-41.5)
    ir.ten(-73.3)

def start_pos_1():
    ir.seven(-39.1)
    ir.six(-2.3)
    ir.eight(-55.9)
    ir.nine(-51.5)
    ir.ten(-73.3)

def pickup_b1():
    ir.nine(-59.7)
    ir.six(-69.1)
    ir.eight(-0.4)
    ir.seven(23.0)
    ir.ten(-98)

def pickup_w1():
    ir.nine(-59.4)
    ir.six(67.3)
    ir.eight(1.3)
    ir.seven(25.7)
    ir.ten(-98)


def place_b1():
    ir.six(82.6)
    ir.nine(-61.4)
    ir.eight(-6.9)
    
    
    ir.seven(23.9)
    ir.ten(-73)

def place_w1():
    ir.nine(-60.9)
    ir.eight(-6.9)
    ir.six(-84.6)
   
    ir.seven(23.9)
    ir.ten(-73)

############

def int_pos_2():
    ir.two(22.4)
    ir.one(91.9)
    ir.three(95.2)
    ir.four(61.4)
    ir.five(56.5)


def start_pos_2():
    ir.two(-21.8)
    ir.one(-1.6)
    ir.three(112.2)
    ir.four(73.2)
    ir.five(56.5)




def pickup_b2():
    ir.four(84.3)
    
    ir.one(-70.8)
    ir.three(22.1)
    ir.two(69.4)
    ir.five(91.3)

def pickup_w2():
    ir.four(84.3)
    
    ir.one(68.8)
    ir.three(22.1)
    ir.two(67.9)
    ir.five(91.3)


def place_b2():
    ir.four(81.4)
    
    ir.one(-91.1)
    ir.three(32.4)
    ir.two(64.7)
    ir.five(56.5)

def place_w2():
    ir.four(78.4)
    
    ir.one(87)
    ir.three(38)
    ir.two(58.5)
    ir.five(56.5)



def pos0():
    ir.six(-73.5)
    ir.eight(-36.5)
    ir.nine(-43.8)
    ir.seven(2.2)
    #ir.ten(-73.3)
    
    

def pos1():
    ir.six(-62.6)
    ir.eight(-63.2)
    ir.nine(-44.4)
    ir.seven(-17.7)

    
    
def pos2():
    ir.six(-2.8)
    ir.nine(-50.2)
    ir.seven(-39.1)
    ir.eight(-81.7)
    
    

def pos3():
    ir.six(58.5)
    
    ir.eight(-64.4)
    ir.nine(-45.3)
    #ir.ten(-111.3)
    ir.seven(-18.9)
def pos4():
    ir.six(72.9)
    
    ir.eight(-34.8)
    ir.nine(-45.6)
    #ir.ten(-111.3)
    ir.seven(4)

def pos5():
    ir.six(-52.3)
    
    ir.eight(-11.3)
    ir.nine(-60.6)
    ir.seven(19.2)
    #ir.ten(-111.3)
    
def pos6():
    ir.six(-34.5)
    
    ir.eight(-42.1)
    ir.nine(-44.4)
    ir.seven(-1.6)
    #ir.ten(-111.3)

def pos7():
    ir.six(-1.6)
    
    ir.eight(-48.2)
    ir.nine(-50.5)
    ir.seven(-4.5)
    #ir.ten(-111.3)

def pos8():
    ir.six(30.6)
    
    ir.eight(-39.7)
    ir.nine(-50)
    ir.seven(1.3)
    #ir.ten(-111.3)

def pos9():
    ir.six(50.0)
    
    ir.eight(-8.4)
    ir.nine(-62.9)
    ir.seven(20.7)
    #ir.ten(-111.3)
    
def pos10():
    ir.six(-40.9)
    
    ir.eight(30.1)
    ir.nine(-77)
    ir.seven(40.3)
    #ir.ten(-111.3)

def pos11():
    ir.six(-24.2)
    
    ir.eight(-3.1)
    ir.nine(-59.4)
    ir.seven(22.4)
    #ir.ten(-111.3)

def pos12():
    ir.six(-2.2)
    
    ir.eight(-12.2)
    ir.nine(-58.5)
    ir.seven(18.3)
    #ir.ten(-111.3)

def pos13():
    ir.six(18.9)
    
    ir.eight(0.1)
    ir.nine(-63.2)
    ir.seven(24.8)

def pos14():
    ir.six(36.5)
    
    ir.eight(35.9)
    ir.nine(-79.3)
    ir.seven(43.5)
    #ir.five(109.8)

def pos15():
    ir.one(50.9)
    
    ir.three(56.2)
    ir.four(68.8)
    ir.two(48.2)
    #ir.five(109.8)

def pos16():
    ir.one(30.9)
    
    ir.three(106.0)
    ir.four(53.5)
    ir.two(11.6)
    #ir.five(109.8)
    

def pos17():
    ir.one(-2.2)
    
    ir.three(113.3)
    ir.four(58.2)
    ir.two(4.8)
    #ir.five(109.8)

def pos18():
    ir.one(-35.6)
    
    ir.three(107.8)
    ir.four(55)
    ir.two(8.4)
    #ir.five(109.8)

def pos19():
    ir.one(-55)
    
    ir.three(65.2)
    ir.four(68.2)
    ir.two(39.1)
    #ir.five(109.8)

def pos20():
    ir.one(71.7)
    
    ir.three(76.7)
    ir.four(68.5)
    ir.two(36.5)
   # ir.five(109.8)


def pos21():
    ir.one(58.8)
    
    ir.three(128.0)
    ir.four(60.3)
    ir.two(-7.2)
    #ir.five(109.8)

def pos22():
    ir.one(-2.8)
    ir.four(69.4)
    
    ir.three(147.1)
    ir.two(-37.8)
    
    #ir.five(109.8)

def pos23():
    ir.one(-63.8)
    
    ir.three(135.3)
    ir.four(62.3)
    ir.two(-20.4)
    #ir.five(109.8)

def pos24():
    ir.one(-77)
    
    ir.three(87)
    ir.four(65.7)
    ir.two(26.2)
    #ir.five(109.8)

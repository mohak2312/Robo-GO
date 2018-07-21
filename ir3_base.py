from pyax12.connection import Connection
from scipy.interpolate import interp1d

import time

speed = 120
sleep_time = 1
global serial_connection 

def open_port():
    global serial_connection 
    # Connect to the serial port
    serial_connection = Connection(port="COM3", baudrate=1000000)
    
def close_port():
    # Close the serial connection
    serial_connection.close()
    
def set_speed(val):
    global speed    
    speed = val

def set_sleep(val):
        global sleep_time
        sleep_time = val

def send_pos(mid, deg):
    global serial_connection 
    serial_connection.goto(mid, deg, speed, degrees=True)
    time.sleep(sleep_time)    #` Wait 1 second

def get_pos(mid):
    global serial_connection 
    return serial_connection.get_present_position(mid,True) 
'''
def initall():
    global serial_connection 
    for dynamixel_id in range(1, 11) :
        serial_connection.goto(dynamixel_id, 0, speed, degrees=True)
        time.sleep(sleep_time)    # Wait 1 second
'''
def one(deg):
    send_pos(1,deg)
        
def two(deg):
    send_pos(2,deg)    

def three(deg):
    send_pos(3,deg)    

def four(deg):
    send_pos(4,deg)    

def five(deg):
    send_pos(5,deg)
def six(deg):
    send_pos(6,deg)
def seven(deg):
    send_pos(7,deg)
def eight(deg):
    send_pos(8,deg)
def nine(deg):
    send_pos(9,deg)

def ten(deg):
    send_pos(10,deg)

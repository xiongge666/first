
from ast import While
from yc_pyvisa import *
from yc_tools  import *
import pyvisa
import os
import xlwt
from datetime import datetime

import openpyxl
from openpyxl.utils import get_column_letter
import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import minimize
from sklearn.linear_model import LinearRegression
import serial
import time


from PIL import ImageGrab
import pytesseract


def get_cmd_result(cmd):
    result = os.popen(cmd)
    res = result.read()
    for line in res.splitlines():
        print (line)
    time.sleep(0.1)
    return res



data_cnt1 = []
data_cnt2 = []
data_cnt3 = []
buff = []
sum = 0

if __name__ == "__main__":
    ############################## 测试控制板程序开始 #####################################################

    # port = "COM104"    # 修改为你使用的串口
    # baudrate = 921600  # 修改为你的波特率
    # ser = serial.Serial(port, baudrate, timeout=1)

	# 要执行的逻辑 ...
    # 获取当前时间
    current_time = datetime.now()
    # 将当前时间转换为字符串
    time_str = current_time.strftime("%Y-%m-%d_%H_%M_%S")
    print(time_str)


    power1 = Agilent_E3649A('GPIB0::4::INSTR')
    meter = Agilent_34410A('GPIB0::6::INSTR')


    power1._set_outputOnOff('ON')
    power1.setVoltage(5,1)
    power1.write(f'CURR {0.3}')
    power1.setVoltage(3.6,2)
    power1.write(f'CURR {0.3}')
    time.sleep(2)
    power1.setVoltage(5,1)
    meter.Read_Curr()
    time.sleep(3)


    vol = 0
    for i in range(0,359):
        power1.setVoltage(3.6-vol,2)
        lpm_current = meter.Read_Curr()
        data_cnt1.append(3.6-vol)
        lpm_current = lpm_current*1000000
        formatted_number = f"{lpm_current:.2f}"
        data_cnt3.append(formatted_number)
        vol=vol+0.01

    xw_columnToExcel(data_cnt1,"lpm_currrent"+time_str+".xlsx")
    xw_columnToExcel(data_cnt3,"lpm_currrent"+time_str+".xlsx")

    data_cnt1.clear()






    os.system("pause")
    print('line')


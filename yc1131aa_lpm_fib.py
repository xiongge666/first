
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
    time.sleep(0.02)
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

    ser = ZLG2014('ASRL8::INSTR')
    # ser.write(":TIMebase:SCALe 100ns")
    ser.Set_Timebase("500us")
    ser.write(":CHANnel1:SCALe 0.5V")
    ser.write(":CHANnel1:DISPlay OFF")
    ser.write(":CHANnel1:DISPlay ON")
    ser.write(":MEASure:VAVG DISPlay,CHANnel1")


    power1 = Agilent_E3649A('GPIB0::4::INSTR')
    meter = Agilent_34410A('GPIB0::6::INSTR')

    power1._set_outputOnOff('ON')
    power1.setVoltage(4.2,1)
    power1.write(f'CURR {0.3}')
    power1.setVoltage(3.3,2)
    power1.write(f'CURR {0.3}')
    # power1.setVoltage(3.3,2)
    meter.Read_Curr()
    os.system("pause")

    time.sleep(1)
    vol = 0

    for k in range(0,7):
        get_cmd_result("e fa860 "+str(k))
        time.sleep(0.3)
        # lpm_voltagle = ser.Get_Vol(1)
        data_cnt1.append(k)
        data = 0
        for i in range(0,10 ):
            time.sleep(0.2)
            get_cmd_result("e p")
            get_cmd_result("e p")
            get_cmd_result("e p")
            get_cmd_result("e p")
            get_cmd_result("e p")
            get_cmd_result("e p")
            get_cmd_result("e d0eed 00")
            get_cmd_result("e 26000 11111111")
            get_cmd_result("e 28000 22222222")
            get_cmd_result("e 30000 33333333")
            get_cmd_result("e 38000 44444444")
            get_cmd_result("e 40000 55555555")
            get_cmd_result("e 48000 66666666")
            get_cmd_result("e 50000 77777777")
            get_cmd_result("e 58000 88888888")
            get_cmd_result("e 60000 99999999")
            get_cmd_result("e 68000 11111111")
            get_cmd_result("e 26000l")
            get_cmd_result("e 28000l")
            get_cmd_result("e 30000l")
            get_cmd_result("e 38000l")
            get_cmd_result("e 40000l")
            get_cmd_result("e 48000l")
            get_cmd_result("e 50000l")
            get_cmd_result("e 58000l")
            get_cmd_result("e 60000l")
            get_cmd_result("e 68000l")

            get_cmd_result("e faaa0 55")
            get_cmd_result("e faaa0 aa")
            get_cmd_result("e faaa0 17")
            get_cmd_result("e faaa4 1")
            get_cmd_result("e faa80 1")

            get_cmd_result("e fa852 01")
            get_cmd_result("e fa852l")
            data = data + (1<<i)
            get_cmd_result("e fa864 "+str(hex(data)[2:]))
            get_cmd_result("e fa866 0000")
            get_cmd_result("e fa860l ")
            get_cmd_result("e faa18 03")
            get_cmd_result("e faa20 5a")

            time.sleep(0.1)
            current = meter.Read_Curr()
            data_cnt1.append(current*1000000)
            power1.setVoltage(0,2)
            power1.setVoltage(3.3,2)
            time.sleep(0.1)
            get_cmd_result("e p")
            get_cmd_result("e p")
            get_cmd_result("e p")
            get_cmd_result("e p")
            get_cmd_result("e p")
            get_cmd_result("e p")
            get_cmd_result("e p")
            get_cmd_result("e p")
            get_cmd_result("e p")
            get_cmd_result("e p")
            get_cmd_result("e p")
            get_cmd_result("e p")
            get_cmd_result("e d0eed 00")
            get_cmd_result("e 26000l")
            get_cmd_result("e 28000l")
            get_cmd_result("e 30000l")
            get_cmd_result("e 38000l")
            get_cmd_result("e 40000l")
            get_cmd_result("e 48000l")
            get_cmd_result("e 50000l")
            get_cmd_result("e 58000l")
            get_cmd_result("e 60000l")
            get_cmd_result("e 68000l")
        print('line')
        xw_columnToExcel(data_cnt1,"lpm_currrent"+time_str+".xlsx")
        data_cnt1.clear()






    os.system("pause")
    print('line')
    print('line222')


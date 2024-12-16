
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


    ser = ZLG2014('ASRL8::INSTR')
    ser.write(":TIMebase:SCALe 100ns")
    ser.Set_Timebase("500us")
    ser.write(":CHANnel1:SCALe 0.5V")
    ser.write(":CHANnel1:DISPlay OFF")
    ser.write(":CHANnel1:DISPlay ON")
    ser.write(":MEASure:VAVG DISPlay,CHANnel1")
    # print(ser.Get_Vol(1))

    # os.system("pause")


    power1 = Agilent_E3649A('GPIB0::4::INSTR')
    meter = Agilent_34410A('GPIB0::6::INSTR')

    power1._set_outputOnOff('OFF')
    time.sleep(1)
    power1._set_outputOnOff('ON')
    power1.setVoltage(5,1)

    meter.Read_Curr()
    time.sleep(1)
    get_cmd_result("bpu.bat")
    data_cnt1.append("0xfa840")
    data_cnt2.append("vddlpm(V)")
    data_cnt3.append("vbut(uA)")
    for i in range(0,6):
        power1._set_outputOnOff('ON')
        time.sleep(1)
        get_cmd_result("e p")
        get_cmd_result("e p")
        get_cmd_result("e p")
        get_cmd_result("e p")
        get_cmd_result("e p")
        get_cmd_result("e p")
        get_cmd_result("bpu.bat")

        get_cmd_result("e fa840 " + str(i))
        get_cmd_result("e fa840 " + str(i))
        get_cmd_result("e fa840 " + str(i))
        get_cmd_result("e fa840 " + str(i))
        get_cmd_result("e fa840 " + str(i))
        get_cmd_result("e fa840 " + str(i))
        get_cmd_result("e fa840l ")
        time.sleep(0.1)
        power1._set_outputOnOff('OFF')
        time.sleep(20)
        # ser.write(":CHANnel1:DISPlay OFF")
        time.sleep(0.1)
        ser.write(":CHANnel1:DISPlay ON")
        ser.write(":MEASure:VAVG DISPlay,CHANnel1")
        time.sleep(1)
        lpm_voltagle = ser.Get_Vol(1)
        lpm_current = meter.Read_Curr()
        data_cnt1.append(i)
        data_cnt2.append(lpm_voltagle)
        lpm_current = lpm_current*1000000
        formatted_number = f"{lpm_current:.2f}"
        data_cnt3.append(formatted_number)
    xw_columnToExcel(data_cnt1,"lpm_currrent"+time_str+".xlsx")
    xw_columnToExcel(data_cnt2,"lpm_currrent"+time_str+".xlsx")
    xw_columnToExcel(data_cnt3,"lpm_currrent"+time_str+".xlsx")

    data_cnt1.clear()






    os.system("pause")
    print('line')


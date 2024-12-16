
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
    time.sleep(0.01)
    return res




def is_data_fluctuating(data_sequence, threshold):
    """
    检查一个数据序列是否出现跳动。

    :param data_sequence: 一个列表，包含任意类型的可比较元素。
    :param threshold: 判断跳动的变化次数阈值。
    :return: 如果数据在跳动，返回 True；否则返回 False。
    """
    if len(data_sequence) < 2:
        return False

    # 计算相邻元素之间的变化次数
    changes = sum(1 for i in range(1, len(data_sequence)) if data_sequence[i] != data_sequence[i-1])

    return changes > threshold


data_cnt1 = []
data_cnt2 = []
data_cnt3 = []
reg_cnt = []
buff = []
mysum = 0

if __name__ == "__main__":
    ############################## 测试控制板程序开始 #####################################################

    # port = "COM104"    # 修改为你使用的串口
    # baudrate = 921600  # 修改为你的波特率
    # ser = serial.Serial(port, baudrate, timeout=1)
    # 示例测试

	# 要执行的逻辑 ...
    # 获取当前时间
    current_time = datetime.now()
    # 将当前时间转换为字符串
    time_str = current_time.strftime("%Y-%m-%d_%H_%M_%S")
    print(time_str)


    power1 = Agilent_E3649A('GPIB0::4::INSTR')
    meter = Agilent_34410A('GPIB0::6::INSTR')


    power1._set_outputOnOff('ON')
    power1.setVoltage(4.2,1)
    power1.write(f'CURR {0.3}')

    meter.Read_Curr()
    time.sleep(1)


    get_cmd_result("e k")
    time.sleep(1)
    get_cmd_result("e p")
    get_cmd_result("e p")
    get_cmd_result("e p")



    get_cmd_result("e fb264 00")
    get_cmd_result("e fb265 00")
    get_cmd_result("e fb266 00")
    get_cmd_result("e fb267 00")
    get_cmd_result("e fb260l")
    for i in range(0,128):
        data = i+128
        data_cnt1.append(hex(data)[2:])
        get_cmd_result("e fb264 "+str(hex(data)[2:]))
        get_cmd_result("e fb260l")

        time.sleep(0.1)
        lpm_current = meter.Read_Curr()
        # data_cnt2.append(3.0)
        lpm_current = lpm_current*1000000
        formatted_number = f"{lpm_current:.2f}"
        data_cnt3.append(formatted_number)
        for i in range(0,20):
            buff = get_cmd_result("e f852al1").split()
            rng_reg = (int(buff[18],16))
            reg_cnt.append(hex(rng_reg))
        if is_data_fluctuating(reg_cnt, 3):
            print("Data is fluctuating.")
            data_cnt2.append("fluctuating")
        else:
            print("Data is stable.")
            data_cnt2.append("stable")
        reg_cnt.clear()
    xw_columnToExcel(data_cnt1,"lpm_currrent"+time_str+".xlsx")
    # xw_columnToExcel(data_cnt2,"lpm_currrent"+time_str+".xlsx")
    xw_columnToExcel(data_cnt3,"lpm_currrent"+time_str+".xlsx")
    xw_columnToExcel(data_cnt2,"lpm_currrent"+time_str+".xlsx")

    data_cnt1.clear()






    os.system("pause")
    print('line')


# -*- coding: utf-8 -*-
"""
Created on Thu Sep 15 09:44:07 2022

@author: Ke
"""

class CRC:
    """
    parameters
    info : list
    crc_n : int, default: 32
    p : list
    q : list
        crc results
    check_code : list
        crc reminder = check code
    code : list
    """
    def __init__(self, info, crc_n=8):
        self.info = info
        loc = [32, 26, 23, 22, 16, 12, 11, 10, 8, 7, 5, 2, 1, 0] #CRC8 check code
        if crc_n == 8:
            loc = [8, 2, 1, 0]
        elif crc_n == 16:
            loc = [16, 15, 2, 0]
        p = [0 for i in range(crc_n + 1)]
        for i in loc:
            p[i] = 1

        info = self.info.copy()
        times = len(info)
        n = crc_n + 1
        for i in range(crc_n):
            info.append(0)
        q = []
        for i in range(times):
            if info[i] == 1:
                q.append(1)
                for j in range(n):
                    info[j + i] = info[j + i] ^ p[j]
            else:
                q.append(0)
        check_code = info[-crc_n::]
        code = self.info.copy()
        for i in check_code:
            code.append(i)

        self.crc_n = crc_n
        self.p = p
        self.q = q
        self.check_code = check_code
        self.code = code
    def print_format(self):
        """output"""
        print('{:10}\t{}'.format('message：', self.info))
        print('{:10}\t{}'.format('polynomial:', self.p))
        print('{:10}\t{}'.format('divisor：', self.q))
        print('{:10}\t{}'.format('reminder:', self.check_code))
        """final output: crc communication code"""
        print('{:10}\t{}'.format('encode:', self.code))
        
        
import numpy as np
import time
import xlrd
import openpyxl
import pandas as pd
import matplotlib.pyplot as plt
import ast
import math
import os
from openpyxl import load_workbook
import matplotlib.image as mpimg

os.chdir('D:\Project\DOE')

time_start = time.time()
"""input: original trajectory"""
workbook = xlrd.open_workbook(filename=r'D:\Project\DOE\J00.xls')
table = workbook.sheets()[0]
velocity = table.col_values(colx=0, start_rowx=0, end_rowx=None)
x = np.linspace(0,20,num = 250)
parameters = np.polyfit(x, velocity, 4)

"""polynomial parameters"""
P0 = np.poly1d(parameters) # velocity equation
print(P0)
yvals=P0(x)


"""figure"""
plot1 = plt.plot(x, velocity, '*',label='original velocity')
plot2 = plt.plot(x, yvals, label='fitting velocity')
plt.show()





#p = [1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0]

"""draw figure"""

plt.plot(x, velocity, '*', label='original velocity')


"""binary transfer"""
 
accuracy = 8 #  accuracy
def dtb(num):
    if num == int(num):
       
        integer = '{:08b}'.format(int(num)) 
        return integer
    else:
        #interl
        integer = int(num)
        #float
        flo = num - integer
        integercom = '{:08b}'.format(integer)
        tem = flo
        tmpflo = []
        for i in range(accuracy):
            tem *= 2
            tmpflo += str(int(tem))
            tem -= int(tem)
        flocom = tmpflo
        return integercom + '.' + ''.join(flocom)



#para_1 = int(ast.literal_eval(dtb(abs(P0[0])))*(10**(accuracy)))
#para_2 = int(ast.literal_eval(dtb(abs(P0[1])))*(10**(accuracy)))
#para_3 = int(ast.literal_eval(dtb(abs(P0[2])))*(10**(accuracy)))
#para_4 = int(ast.literal_eval(dtb(abs(P0[3])))*(10**(accuracy)))   

#p1 = [int(x1) for x1 in str(para_1)]
#p2 = [int(x1) for x1 in str(para_2)]
#p3 = [int(x1) for x1 in str(para_3)]
#p4 = [int(x1) for x1 in str(para_4)]

p1 = [1,1,0]
#m = np.random.randint(0, 2, 10)

crc_p1 = CRC(p1, 8)
#crc_p2 = CRC(p2, 8)
#crc_p3 = CRC(p3, 8)
#crc_p4 = CRC(p4, 8)

crc_p1.print_format()
#crc_p2.print_format()
#crc_p3.print_format()
#crc_p4.print_format()

time_end = time.time() 
time_c= time_end - time_start   #time calculating functions

print('time cost', time_c, 's')
code = [1, 1, 0, 1, 1, 0, 0, 0, 1, 0, 1]
check = [1, 1, 0, 0, 0, 1, 0, 1]

str_code = [str(x) for x in code]
str_check = [str(x) for x in check]

str1 = ''.join(str_code)
str2 = ''.join(str_check)

int_str1 = int(str1,2);
int_str2 = int(str2,2);

int(str1,2)
int(str(code),2)

I = mpimg.imread('D:/Project/DOE/ped.png')

if int_str1 == 1733 & int_str2==197:
    plt.imshow(I)
    plt.axis('off')







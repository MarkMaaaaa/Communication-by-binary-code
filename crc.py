"""Python 3.9, import numpy"""

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
    def __init__(self, info, crc_n=32):
        self.info = info
        loc = [32, 26, 23, 22, 16, 12, 11, 10, 8, 7, 5, 2, 1, 0]
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

"""input (m): polynomial parameters"""
p1 = list(np.random.randint(0,2,35))
p2 = list(np.random.randint(0,2,35))
p3 = list(np.random.randint(0,2,35))
p4 = list(np.random.randint(0,2,35))

p = [1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0]

time_start = time.time()
#m = np.random.randint(0, 2, 10)

crc_p1 = CRC(p, 32)
#crc_p2 = CRC(p2, 32)
#crc_p3 = CRC(p3, 32)
#crc_p4 = CRC(p4, 32)

crc_p1.print_format()
#crc_p2.print_format()
#crc_p3.print_format()
#crc_p4.print_format()

time_end = time.time() 
time_c= time_end - time_start   #time calculating functions

print('time cost', time_c, 's')


    







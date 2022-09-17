# -*- coding: utf-8 -*-
"""
Created on Fri Sep 16 22:12:44 2022

@author: Ke
"""

"""Detect the panel pixels, and obtain the message information (including p1 p2....)"""

polynomial = 	[1, 1, 1, 0, 0, 0, 0, 0, 1]

if message/polynomial == 0:
    print("Accept")
else:
    print("Reject")

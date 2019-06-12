import binascii

import sys

import time

import os

import random

import math

def divide(data)

    d = open(data,"r")
    i = 0
    a = ''
    z = []

    while(1):
        data1 = d.read(8) #read(8) means it reads 8 bytes from the file d
        if not data1:
            d.close()
            os.remove(data) #this removes the path; here it is data
            break
        z.append(data1)
    return z

def convert(temp):
    i = 0
    a = ''
    while(len(temp)<8):
        temp = temp + " "
    while(i<=7):
        data1 = temp[i]
        bindata1 = bin(data1) 
        if(len(bindata1)<8):
            j = 0
            z = len(bindata1)
            while(j<8-z):
                bindata1 = '0'+bindata1
                j = j+1
            a = bindata1+a
            i = i+1

            return int(a,2)

def convertbinarytodata(a):

    i = 0
    mask = 0b1111111
    text = ""
    while(i<8):
        text = text+chr(mask&a)
        a = a>>8
        i = i+1
   
def initialpermutation(a):
    binarydata = bin(a)
    binarydata = binarydata[2:]
    if(len(binarydata)<64):
        j = 0
        z = len(binarydata)
        while(j<64-z):
            binarydata = "0"+binarydata
            j = j+1

        IP1 = [[58,50,42,34,26,18,10,2],

           [60,52,44,36,28,20,12,4],

           [62,54,46,38,30,22,14,6],

           [64,56,48,40,32,24,16,8],

           [57,49,41,33,25,17,9,1],

           [59,51,43,35,27,19,11,3],

           [61,53,45,37,29,21,13,5],

           [63,55,47,39,31,23,15,7]]

    i = 0

    j = 0

    temp = ''

    while(i<8):

        j=0

        while(j<8):

            z = IP1[i][j]-1

            temp = binarydata[63-z]+temp

            j = j+1

        i = i+1

    binary = temp

    return int(binary,2)

def inversepermutation(a):
    binarydata = bin(a)
    binarydata = binarydata[2:]
    if(len(binary)<64):

        j=0

        z = len(binarydata)

        while(j<64-z):

            binarydata = "0"+binarydata

            j = j+1

            InvIP1 = [[40,8,48,16,56,24,64,32],

            [39,7,47,15,55,23,63,31],

            [38,6,46,14,54,22,62,30],

            [37,5,45,13,53,21,61,29],

            [36,4,44,12,52,20,60,28],

            [35,3,43,11,51,19,59,27],

            [34,2,42,10,50,18,58,26],

            [33,1,41,9,49,17,57,25]]

    i = 0

    j = 0

    temp =''

    while(i<8):

        j = 0

        while(j<8):
    
             z = InvIP1[i][j]-1
             temp = binarydata[63-z]+temp

            j = j+1

        i = i+1

    binarydata = temp
    return int(binarydata,2)

def PCI(key):

    rd = key

    rdbin = bin(rd)

    rdbin = rdbin[2:]
    if(len(rdbin)<64):

        j=0

        z = len(rdbin)

        while(j<64-z):

            rdbin = '0'+rdbin

            j = j+1

        PCI1 = [[57,49,41,33,25,17,9],

            [1,58,50,42,34,26,18],

            [10,2,59,51,43,35,27],

            [19,11,3,60,52,44,36],

            [63,55,47,39,31,23,15],

            [7,62,54,46,38,30,22],

            [14,6,61,53,45,37,29],

            [21,13,5,28,20,12,4]]

    i = 0

    j = 0

    temp = ''

    while(i<8):

        j = 0

        while(j<7):

            z = pci1[i][j]-1

            temp = rdbin[63-z]+temp

            j = j+1

        i = i+1

    binarydata = temp
    return int(binarydata, 2)

def leftshiftdata(a):
    binarydata = bin(a)
    binarydata = binarydata[2:]
    if(len(binarydata)<56):

        j = 0

        z = len(binarydata)

        while(j<56-z):

            binarydata = '0'+binarydata

            j = j+1

            lbinary = binarydata[:28]

            rbinary = binarydat[28:]
            temp = lbinary[0]

            lbinary = lbinary[1:28]+temp
            temp = rbinary[0]

            rbinary = rbinary[1:28]+temp
            binary = lbinary + rbinary
            return int(binary,2)

def PCII(a):
    binarydata = bin(a)
    binarydata = binarydata[2:]
    if(len(binarydata)<56):

        j = 0

        z = len(binarydata)

        while(j<56-z):

            binarydata = '0'+binarydata

            j = j+1
    
    pcii1 = [[14,17,11,24,1,5,3,28],

             [15,6,21,10,23,19,12,4],

             [26,8,16,7,27,20,13,2],

             [41,52,31,37,47,55,30,40],

             [51,45,33,48,44,49,39,56],

             [34,53,46,42,50,36,29,32]]

    i =0

    j =0

    temp = ''
    while(i<6):

        j=0

        while(j<8):

            z = pcii1[i][j]-1

            temp = binarydata[55-z]+temp

            j = j+1

        i = i+1

    binarydata = temp

    return int(binarydata,2)

def expansiondata(a):

    binarydata = bin(a)

    binarydata = binarydata[2:]

    if(len(binarydata)<32):

        j = 0

        z = len(binarydata)

        while(j<32-z):

            binarydata = '0'+binarydata

            j = j+1

            EXP1 = [[32,1,2,3,4,5],

            [4,5,6,7,8,9],

            [8,9,10,11,12,13],

            [12,13,14,15,16,17],

            [16,17,18,19,20,21],

            [20,21,22,23,24,25],

            [24,25,26,27,28,29],

            [28,29,30,31,32,1]]

    i = 0

    j = 0

    temp = ''

    while(i<8):

        j = 0

        while(j<6):

            z = EXP1[i][j]-1
            temp = binarydata[31-z]+temp

            j = j+1

        i = i+1

    binarydata = temp

    #print binary

    #print len(binary)

    return int(binarydata , 2)



#Code for permutation function

def permfunct(a):

    binarydata = bin(a)

    binarydata = binarydata[2:]

    j = 0

    z = len(binarydata)

    while(j<32-z):

        binarydata = '0'+binarydata

        j = j+1

        PERM = [[16,7,20,21,29,12,28,17],

              [1,15,23,26,5,18,31,10],

              [2,8,24,14,32,27,3,9],

              [19,13,30,6,22,11,4,25]]

    i =0

    j = 0

    per = ''

    while(i<4):

        j = 0

        while(j<8):

            z = permut[i][j]-1

            per = binary[31-z] + per

            j = j+1

        i = i+1
        return int(per,2)

def sbox(a):

    mask = 0b111111

    s8 = mask&a

    a = a>>6

    s7 = mask&a

    a = a>>6

    s6 = mask&a

    a = a>>6

    s5 = mask&a

    a = a>>6

    s4 = mask&a

    a = a>>6

    #print bin(a)

    s3 = mask&a

    a = a>>6

    #print bin(a)

    s2 = mask&a

    a = a>>6

    #print bin(a)

    s1 = mask&a

    i = ((s1&0b100000)>>4)|(s1&0b1)

    j = ((s1&0b011110)>>1)

    S1 = [[14, 4, 13, 1, 2, 15, 11, 8, 3, 10, 6, 12, 5, 9, 0, 7],

          [0, 15, 7, 4, 14, 2, 13, 1, 10, 6, 12, 11, 9, 5, 3, 8],

          [4, 1, 14, 8, 13, 6, 2, 11, 15, 12, 9, 7, 3, 10, 5, 0],

          [15, 12, 8, 2, 4, 9, 1, 7, 5, 11, 3, 14, 10, 0, 6, 13]]

    s1 = S1[i][j]

    #print s1

    i = ((s2&0b100000)>>4)|(s2&0b1)

    j = ((s2&0b011110)>>1)

    #print "i",i

    #print "j",j

    S2 = [[15, 1, 8, 14, 6, 11, 3, 4, 9, 7, 2, 13, 12, 0, 5, 10],

          [3, 13, 4, 7, 15, 2, 8, 14, 12, 0, 1, 10, 6, 9, 11, 5],

          [0, 14, 7, 11, 10, 4, 13, 1, 5, 8, 12, 6, 9, 3, 2, 15],

          [13, 8, 10, 1, 3, 15, 4, 2, 11, 6, 7, 12, 0, 5, 14, 9]]

    s2 = S2[i][j]

    #print s2

    i = ((s3&0b100000)>>4)|(s3&0b1)

    j = ((s3&0b011110)>>1)

    #print "i",i

    #print "j",j

    S3 = [[10, 0, 9, 14, 6, 3, 15, 5, 1, 13, 12, 7, 11, 4, 2, 8],

          [13, 7, 0, 9, 3, 4, 6, 10, 2, 8, 5, 14, 12, 11, 15, 1],

          [13, 6, 4, 9, 8, 15, 3, 0, 11, 1, 2, 12, 5, 10, 14, 7],

          [1, 10, 13, 0, 6, 9, 8, 7, 4, 15, 14, 3, 11, 5, 2, 12]]

    s3 = S3[i][j]

    #print s3

    i = ((s4&0b100000)>>4)|(s4&0b1)

    j = ((s4&0b011110)>>1)

    #print "i",i

    #print "j",j

    S4 = [[7, 13, 14, 3, 0, 6, 9, 10, 1, 2, 8, 5, 11, 12, 4, 15],

          [13, 8, 11, 5, 6, 15, 0, 3, 4, 7, 2, 12, 1, 10, 14, 9],

          [10, 6, 9, 0, 12, 11, 7, 13, 15, 1, 3, 14, 5, 2, 8, 4],

          [3, 15, 0, 6, 10, 1, 13, 8, 9, 4, 5, 11, 12, 7, 2, 14]]

    s4 = S4[i][j]

    #print s4

    i = ((s5&0b100000)>>4)|(s5&0b1)

    j = ((s5&0b011110)>>1)

    #print "i",i

    #print "j",j

    S5 = [[2, 12, 4, 1, 7, 10, 11, 6, 8, 5, 3, 15, 13, 0, 14, 9],

          [14, 11, 2, 12, 4, 7, 13, 1, 5, 0, 15, 10, 3, 9, 8, 6],

          [4, 2, 1, 11, 10, 13, 7, 8, 15, 9, 12, 5, 6, 3, 0, 14],

          [11, 8, 12, 7, 1, 14, 2, 13, 6, 15, 0, 9, 10, 4, 5, 3]]

    s5 = S5[i][j]

    #print s5

    i = ((s6&0b100000)>>4)|(s6&0b1)

    j = ((s6&0b011110)>>1)

    #print "i",i

    #print "j",j

    S6 = [[12, 1, 10, 15, 9, 2, 6, 8, 0, 13, 3, 4, 14, 7, 5, 11],

          [10, 15, 4, 2, 7, 12, 9, 5, 6, 1, 13, 14, 0, 11, 3, 8],

          [9, 14, 15, 5, 2, 8, 12, 3, 7, 0, 4, 10, 1, 13, 11, 6],

          [4, 3, 2, 12, 9, 5, 15, 10, 11, 14, 1, 7, 6, 0, 8, 13]]

    s6 = S6[i][j]

    #print s6

    i = ((s7&0b100000)>>4)|(s7&0b1)

    j = ((s7&0b011110)>>1)

    #print "i",i

    #print "j",j

    S7 = [[4, 11, 2, 14, 15, 0, 8, 13, 3, 12, 9, 7, 5, 10, 6, 1],

          [13, 0, 11, 7, 4, 9, 1, 10, 14, 3, 5, 12, 2, 15, 8, 6],

          [1, 4, 11, 13, 12, 3, 7, 14, 10, 15, 6, 8, 0, 5, 9, 2],

          [6, 11, 13, 8, 1, 4, 10, 7, 9, 5, 0, 15, 14, 2, 3, 12]]

    s7 = S7[i][j]

    #print s7

    i = ((s8&0b100000)>>4)|(s8&0b1)

    j = ((s8&0b011110)>>1)

    #print "i",i

    #print "j",j

    S8 = [[13, 2, 8, 4, 6, 15, 11, 1, 10, 9, 3, 14, 5, 0, 12, 7],

          [1, 15, 13, 8, 10, 3, 7, 4, 12, 5, 6, 11, 0, 14, 9, 2],

          [7, 11, 4, 1, 9, 12, 14, 2, 0, 6, 10, 13, 15, 3, 5, 8],

          [2, 1, 14, 7, 4, 10, 8, 13, 15, 12, 9, 0, 3, 5, 6, 11]]

    s8 = S8[i][j]

    #print s8

    

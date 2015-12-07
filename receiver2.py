#!/usr/bin/python

import time
import sys
import math

#time.sleep(5) #give sender time to establish baseline

def operation():
    for i in range (0, 100000):
        math.sqrt(2)

timeInterval = 1
l = []

#for i in range(0, 10):
    #operation()

#print "Told sender I'm started"

baseline = 0
#print 'establishing baseline...'
baselineStartingTime = time.time()
counter = 0
while time.time() - baselineStartingTime < 2:
    counter += 1
    start = time.time()
    operation()
    interval = time.time() - start
    baseline += interval

#print time.time() - baselineStartingTime

baseline /= counter
#print 'counter: ', counter
threshold = baseline * 1.35
#print 'receiver baseline: ', baseline
#print 'threshold', threshold

time.sleep(0.22)
#print 'start receiving'

def otherRunning():
    start = time.time()
    operation()
    interval = time.time() - start
    if interval > threshold:
        return True
    else:
        return False

def receive():
    b = 0
    if otherRunning():
        #print 'receiving 1'
        b = 1
    else:
        #print 'receiving 0'
        b = 0
    l.append(b)

for i in range (0, 56):
    started = time.time()
    receive()
    now = time.time()
    time.sleep(timeInterval - (now - started))

def bitArray2String(arrBits):
    strResult = [];
    # To DO:
    # 1. Insert a leading zero
    # 2.  convert every 8 bits into an integer
    # 3. Obttain characters from the integers
    # 4. Concatenate the characters into a string

    # Inserting leading Zeros
    for i in range(0,8):
        if(i==0):
            arrBits.insert(i,0)
        else:
            arrBits.insert((i*7)+i,0)
    
    
    #2 convert every 8 bits into integer
    arrIntegers = [];
    result = 0;
    for i in range(0,8):
        char = arrBits[i*8:(i+1)*8];#char has the 8 bits required
        shiftIndex = 7;
        for j in char:
            result = result | j<<shiftIndex;
            shiftIndex = shiftIndex-1;
        arrIntegers.append(result);
        result = 0;


    #3. Obtain characters from the string
    arrChar = [];
    
    for i in arrIntegers:
        arrChar.append(chr(i));

    #4. Concatenaate
    print(''.join(arrChar));
    print >> sys.stderr, "Receiving", ''.join(arrChar)

bitArray2String(l)
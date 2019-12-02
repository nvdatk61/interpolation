#!/usr/bin/python

import threading
import time
# import newton
from newton import Newton

# Define a function for the thread
class MultiThread:
   def print_time( threadName, delay1):
      count = 0
      while count < 5:
         time.sleep(delay1)
         count += 1
      # t=time.ctime(time.time())
      # print(t)
         print ("%s: %s" % ( threadName, time.ctime(time.time()) ))

   def delaynewton(threadName,delay2):
      count =0
      while count <5:
          # d=2
          obj=Newton()
          time.sleep(delay2)
          count +=1
          # print("%s: %s" % (threadName,))
          print(obj.calculate())

# Create two threads as follows
   try:
      obj = Newton()
      # obj.calculate()
      t1= threading.Thread( target=print_time, args=("Show Interpolation Newton", 5, ))
      t2= threading.Thread( target=delaynewton, args=("ok cuong",5, ))
      t1.start()
      t2.start()
      t1.join()
      t2.join()
      # a=Newton.calculate()
      # print(a)
      print("okok")
   except:
      print( "Error: unable to start thread")

   while 1:
      pass
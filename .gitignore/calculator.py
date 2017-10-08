# area calculator
from math import pi
from time import sleep
from datetime import datetime
now = datetime.now()
print"Calculator is setting-up !"
print now
sleep(1)
hint = "Don't forget to include the correct units! \nExiting..."
option = raw_input("Enter C for Circle or T for Triangle: ")
option = option.upper()
if option == "C" :
  radius = float(raw_input("enter the value of radius of circle: "))
  area = pi * radius ** 2
  print "The pie is baking..."
  sleep(1)
  print "area of circle with radius %f is %.2f" % (radius,area)
elif option == "T":
  base = float(raw_input("enter the valuse of base of tringle : "))
  height = float(raw_input("enter the valuse of height of tringle: "))
  area = base * height *0.5
  print("Uni Bi Tri...")
  print("area of the trinagle with base %f and height %f is %.2f") % (base,height,area)
else:
  print "enter valid option"
  
  
 

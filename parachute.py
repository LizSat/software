#!/usr/bin/env python
"""
CPCMC
3/11/2017
based on J.R. Brohm's "The Mathematics of Flat Parachutes"
http://www.psc473.org/howto/MathofParachutes.pdf
"""

import math
from sys import platform

class color:
  if platform == "linux" or platform == "linux2":
    PURPLE = '\033[95m'
    CYAN = '\033[96m'
    DARKCYAN = '\033[36m'
    BLUE = '\033[94m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    END = '\033[0m'
  else:
    PURPLE, CYAN, DARKCYAN, BLUE, GREEN, RED, BOLD, UNDERLINE, END = ''

earth_radius = 6371.009 #km
g_reference = 9.80665 #m/s^2 #g(sea-level)

mode = raw_input(color.BOLD + "Mode:\n(1) Default Values\n(2) Custom Values\n:" + color.END)

# h:height from which the cansat is thrown
if mode == "2":
  h = float(raw_input(color.BOLD + "\nHeight(m):" + color.END)) #m
  h = float(h) / 1000 if (h == "") else 1000
  h = h if (h != 0) else 1000
  h_km = h / 1000 #km
else:
  h = 1000 #m
  h_km = h / 1000 #km
  print color.BOLD + "\nHeight:" + color.END, h, "m"

# g:the acceleration due to gravity
g = g_reference * ((earth_radius / (earth_radius + h_km))**2) #m/s^2
# g(height=1000m)=99.99996860781%*g(sea-level)

# m:mass of the cansat
if mode == "2":
  m = raw_input(color.BOLD + "Mass(g):" + color.END) #kg
  m = float(m) / 1000 if (m == "") else ((300 + 350) / 2) / 1000
  m = m if (m != 0) else ((300 + 350) / 2) / 1000
  print m
else:
  m = ((300 + 350) / 2)
  print color.BOLD + "Mass:" + color.END, m, "g"

# Density of air at sea level
air_dens = 1.225 #kg/m^3

# Coefficient of drag of the parachute
dragc = 0.75 #(estimated value for a round canopy)
             #0.80??

# Terminal velocity of the cansat
if mode == "2":
  v_term = float(raw_input(color.BOLD + "Desired terminal velocity(m/s):" + color.END)) #m/s
  v_term = float(v_term) if (v_term == "") else 10
  v_term = v_term if (v_term != 0) else 10
else:
  v_term = ((8+11) / 2) #m/s
  print color.BOLD + "Desired terminal velocity(m/s):" + color.END, v_term, " m/s"

a_wo_parachute = g
tf_wo_parachute = math.sqrt( h / (0.5*g))
v_wo_parachute = g * tf_wo_parachute #m/s
print color.BOLD + "\nTime of flight without parachute:" + color.END, tf_wo_parachute, "s"
print color.BOLD + "Impact velocity without parachute:" + color.END, v_wo_parachute, "m/s"

# Required parachute area
area_parachute= (2 * g * m) / (air_dens * dragc * (v_term**2)) #m^2
area_parachute_cm2 = area_parachute * (10**4)
print color.BOLD + "\nFor the parachute:" + color.END
print color.BOLD + "Area(m^2):" + color.END, area_parachute, "m^2"
print color.BOLD + "Area(cm^2):" + color.END, area_parachute_cm2, "cm^2"

# Type of parachute
type = raw_input(color.BOLD + "\nType of parachute:\n(1) N-sided-polygon-shaped parachute\n(2) Cross-shaped parachute\n: " + color.END)

if type == "1":
  subtype = raw_input(color.BOLD + "( ) Without hole\n(2) With hole\n: " + color.END)
  if subtype == "2":
    hole_diameter = float(raw_input(color.BOLD + "Hole diameter(cm): " + color.END)) #cm
    hole_diameter = float(hole_diameter) if (hole_diameter == "") else 5
    hole_diameter = hole_diameter if (hole_diameter != 0) else 5
    hole_diameter_m = hole_diameter / (10**2) #m
    hole_radius = hole_diameter_m / 2 #m
    area_hole = math.pi * (hole_radius**2) #m^2
    area_parachute_needed = area_parachute + area_hole #m^2
  else:
    area_parachute_needed = area_parachute
  
  # Number of sides
  sides = raw_input(color.BOLD + "\nNumber of Sides (>=5):" + color.END)
  sides = int(sides) if (sides == "") else 5
  sides = sides if (sides != 0) else 5
  angle_degrees = 360 / sides
  angle_radians = math.radians(angle_degrees)
  sin_angle = math.sin(angle_radians)
  
  # Diameter
  diameter =2 * math.sqrt((2 * area_parachute_needed) / (sides * sin_angle)) #m
  diameter_cm = diameter * (10**2)
  print color.BOLD + "Diameter:" + color.END, diameter_cm, "cm"
  
  # Radius
  radius= diameter / 2 #m
  radius_cm = radius * (10**2)
  print color.BOLD + "Radius:" + color.END, radius_cm, " cm"
  
  # Side
  angle2_degrees = 180 / sides
  angle2_radians = math.radians(angle2_degrees)
  sin_angle2 = math.sin(angle2_radians)
  side_lenght = diameter * sin_angle2 #m
  side_lenght_cm = side_lenght * (10**2)
  print color.BOLD + "Side:" + color.END, side_lenght_cm, "cm"
  
  # For each triangle:
  print(color.BOLD + "\nFor each triangle:\n")
  if subtype == "2":
    print "          ^\n         /|\ \n        / | \ \n       /  |  \ \n      /   |   \ \nside /\   |   /\ \n    /  '-_|_-'  \ \n   /      |      \ \n  /       |apothem\ \n /        |        \ \n -------------------\n         base"
  else:
    print "          ^\n         /|\ \n        / | \ \n       /  |  \ \n      /   |   \ \nside /    |    \ \n    /     |     \ \n   /      |      \ \n  /       |apothem\ \n /        |        \ \n -------------------\n         base" + color.END 
    
  area_triangle = area_parachute_needed / sides #m^2
  area_triangle_cm2 = area_triangle * (10**4)
  #area_triangle_cm2_str = str(area_triangle_cm2)
  print color.BOLD + "\nArea:" + color.END, area_triangle_cm2, "cm^2"
  print color.BOLD + "Sides:" + color.END, radius_cm, "cm"
  print color.BOLD + "Base:" + color.END, side_lenght_cm, "cm"
  
  angle3_degrees = (180 / sides)
  angle3_radians = math.radians(angle3_degrees)
  cos_angle3 = math.cos(angle3_radians)
  height = radius * cos_angle3 #m
  height_cm = height * (10**2)
  print color.BOLD + "Height:" + color.END, height_cm, "cm"

elif type == "2":
  span = 3 * math.sqrt((area_parachute/5)) #m
  span_cm = span * (10**2) #cm
  print color.BOLD + "Span:" + color.END + span_cm + "cm"
  
  # For each square:
  print color.BOLD + "\nFor each square:"
  print "\n____________________\n|                  |\n|                  |\n|                  |\n|                  |\n|                  |\n|                  |\n|                  |\n''''''''''''''''''''\n        side" + color.END
  
  area_square = area_parachute / 5 #m^2
  area_square_cm2 = area_square * (10**4) #cm^2
  print color.BOLD + "\nArea:" + color.END, area_square_cm2, " cm^2"
  
  side_square = math.sqrt(area_square) #m
  side_square_cm = side_square * (10**2) #cm
  print color.BOLD + "Side:" + color.END, side_square_cm, "cm"

# Trials
print color.BOLD + "\n\nTrials:"
print "\n       O ---\n          |\n          |\n          |\n          |\n          |\n          |\n          |\n       y  V" + color.END

# drag=0.5 * dragc * air_dens * area_parachute * (v**2)
# drag=kv^2
# k=0.5 * dragc * air_dens * area_parachute
k = 0.5 * dragc * air_dens * area_parachute
# k=0.035309263699054606
# a = g - ((k*v^2)/mass)
# a~= 9.8 - ((0.0353/v^2)/mass) #m/s^2
v_net = 0
time_keeper = 0 #s
v_t__dic = {}
v_t__list = []

if mode != "2":
  fraction = 95 #%
  fraction_0_to_1 = fraction/100
  step = 0.1 #S
  step_lenght = 1
  print color.BOLD + "\nFraction of terminal velocity(%):" + color.END, fraction
  print color.BOLD + "Step:" + color.END, step, " s"
else:
  fraction = raw_input(color.BOLD + "\nFraction of terminal velocity(%): " + color.END)
  fraction = int(fraction) if (fraction == "") else 95
  fraction = fraction if (fraction != 0) else 95
  fraction_0_to_1 = fraction/100
  fraction_str = str(fraction)
  step = raw_input(color.BOLD + "Step(s): " + color.END)
  step = float(step) if (step == "") else 0.01
  step = step if (step != 0.0) else 0.01
  step_str = str(step)
  step_lenght = step_str[::-1].find('.')

for i in range(0, fraction, 1):
  while v_net < (fraction_0_to_1 * v_term):
    v_net += step * (g - ( k * v_net * v_net) / m)
    v_t__dic[time_keeper] = v_net #add exact values to dic
    list_int1 = [str(round(time_keeper, step_lenght)), str(round(v_net, 3))] #add round values to list
    v_t__list.append(list_int1)
    time_keeper += step

elapsed_time = round(time_keeper - step, 3)

distance_travelled = 0 #m
y_t__dic = {}
y_t__list = []
for t,v in v_t__dic.items():
  distance_travelled += step * v
  y_t__dic[t] = distance_travelled #add exact values to dic
  list_int2 = [str(round(t, step_lenght)), str(round(distance_travelled, 3))] #add round values to list
  y_t__list.append(list_int2)
  
#distance_travelled_str = str(round(distance_travelled, 3))
distance_travelled = round(distance_travelled, 3)

# Print trial results
print color.BOLD + "\nTime of flight until" + str(fraction) + "% of terminal velocity is reached:" + color.END, elapsed_time, "s" #time
print color.BOLD + "\nDistance travelled until" + str(fraction) + "% of terminal velocity is reached:" + color.END, distance_travelled, "m" #distance

# Graph

answer = raw_input(color.BOLD + "\nPretty graph? (Y/n): " + color.END)

if answer == "Y" or answer == "y" or answer == "":
  # Printing v_t
  print "\n" 
  print color.BOLD + "Elapsed Time(s):     Velocity(m/s):" + color.END
  for row in v_t__list:
    msg = ""
    for word in row:
      msg += word.ljust(21)
    print msg
    #print "".join(word.ljust(21) for word in row)
  # Printing y_t
  print "\n"
  print color.BOLD + "Elapsed Time(s):     Distance travelled(m):" + color.END
  for row in y_t__list:
    msg = ""
    for word in row:
      print word
      msg += word.ljust(21)
    print msg
    #print "".join(word.ljust(21) for word in row)
    
else:
  sys.exit(0)

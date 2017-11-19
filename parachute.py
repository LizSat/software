"""
CPCMC
3/11/2017
based on J.R. Brohm's "The Mathematics of Flat Parachutes"
http://www.psc473.org/howto/MathofParachutes.pdf
"""
import math

earth_radius= 6371.009 #km
g_reference=9.80665 #m/s^2 #g(sea-level)

mode=(input("Mode:\n(1) Default Values\n(2) Custom Values\n:"))

#h:height from which the cansat is thrown
if mode != "2":
  h=1000 #m
  h_km=(h)/1000 #km
  h_str=str(h)
  print(("\nHeight: " + h_str + " m"))

elif mode == "2":
  h=float(input("\nHeight(m):")) #m
  h_km=(h)/1000 #km

#g:the acceleration due to gravity
g=g_reference * ((earth_radius/(earth_radius+h_km))**2) #m/s^2
#g(height=1000m)=99.99996860781%*g(sea-level)

#m:mass of the cansat
if mode != "2":
  m=((300+350)/2)/1000 #kg
  m_g=m*(10**3)
  m_g_str=str(m_g)
  print(("Mass: " + m_g_str + "g"))

elif mode == "2":
  m=float(input("Mass(g):"))/1000 #kg

#the density of air at sea level
air_dens=1.225 #kg/m^3

#the coefficient of drag of the parachute
dragc=0.75 #(estimated value for a round canopy)
           #0.80??

#terminal velocity of the cansat
if mode != "2":
  v_term=((8+11)/2) #m/s
  v_term_str=str(v_term)
  print(("Desired terminal velocity(m/s): " + v_term_str + " m/s"))
  
if mode == "2":
  v_term=float(input("Desired terminal velocity(m/s):")) #m/s

a_wo_parachute=g
tf_wo_parachute=math.sqrt(h/(0.5*g))
tf_wo_parachute_str=str(tf_wo_parachute)
v_wo_parachute=g*tf_wo_parachute #m/s
v_wo_parachute_str=str(v_wo_parachute)
print("\nTime of flight without parachute: " + tf_wo_parachute_str + " s")
print("Impact velocity without parachute: " + v_wo_parachute_str + " m/s")

#required parachute area
area_parachute=(2 * g * m)/(air_dens * dragc * (v_term**2)) #m^2
area_parachute_str=str(area_parachute)
area_parachute_cm2=area_parachute * (10**4)
area_parachute_cm2_str=str(area_parachute_cm2)
print("\nFor the parachute:")
print("Area(m^2): " + area_parachute_str + " m^2")
print("Area(cm^2): " + area_parachute_cm2_str + " cm^2")

#type of parachute
type=input("\nType of parachute:\n(1) N-sided-polygon-shaped parachute\n(2) Cross-shaped parachute\n: " )

if type == "1":
  subtype=input("( ) Without hole\n(2) With hole\n: ")
  if subtype == "2":
    hole_diameter=float(input("Hole diameter(cm): ")) #cm
    hole_diameter_m=hole_diameter/(10**2) #m
    hole_radius=hole_diameter_m/2 #m
    area_hole=math.pi*((hole_radius)**2) #m^2
    area_parachute_needed=area_parachute + area_hole #m^2
  elif subtype != "2":
    area_parachute_needed=area_parachute
  
  #number of sides
  sides=int(input("\nNumber of Sides (>=5):"))
  angle_degrees=(360 / sides)
  angle_radians=math.radians(angle_degrees)
  sin_angle=math.sin(angle_radians)
  
  #diameter
  diameter=2 * math.sqrt((2 * area_parachute_needed)/(sides * sin_angle)) #m
  diameter_cm=diameter*(10**2)
  diameter_cm_str=str(diameter_cm)
  print("Diameter: " + diameter_cm_str + " cm")
  
  #radius
  radius=(diameter/2) #m
  radius_cm=radius*(10**2)
  radius_cm_str=str(radius_cm)
  print("Radius: " + radius_cm_str + " cm")
  
  #side
  angle2_degrees=(180 / sides)
  angle2_radians=math.radians(angle2_degrees)
  sin_angle2=math.sin(angle2_radians)
  side_lenght=diameter*sin_angle2 #m
  side_lenght_cm=side_lenght*(10**2)
  side_lenght_cm_str=str(side_lenght_cm)
  print("Side: " + side_lenght_cm_str + " cm")
  
  #For each triangle:
  print("\nFor each triangle:\n")
  if subtype == "2":
    print("          ^\n         /|\ \n        / | \ \n       /  |  \ \n      /   |   \ \nside /\   |   /\ \n    /  '-_|_-'  \ \n   /      |      \ \n  /       |apothem\ \n /        |        \ \n -------------------\n         base")
  elif subtype != "2":
    print("          ^\n         /|\ \n        / | \ \n       /  |  \ \n      /   |   \ \nside /    |    \ \n    /     |     \ \n   /      |      \ \n  /       |apothem\ \n /        |        \ \n -------------------\n         base")
    
  area_triangle=area_parachute_needed/sides #m^2
  area_triangle_cm2=area_triangle*(10**4)
  area_triangle_cm2_str=str(area_triangle_cm2)
  print("\nArea: " + area_triangle_cm2_str + " cm^2")
  print("Sides: " + radius_cm_str + " cm")
  print("Base: " + side_lenght_cm_str + " cm")
  
  angle3_degrees=(180 / sides)
  angle3_radians=math.radians(angle3_degrees)
  cos_angle3=math.cos(angle3_radians)
  height=radius*cos_angle3 #m
  height_cm=height*(10**2)
  height_cm_str=str(height_cm)
  print("Height: " + height_cm_str + " cm")

elif type == "2":
  span=3* math.sqrt((area_parachute/5)) #m
  span_cm=span*(10**2) #cm
  span_cm_str=str(span_cm)
  print("Span: " + span_cm_str + " cm")
  
  #For each square:
  print("\nFor each square:")
  print("\n____________________\n|                  |\n|                  |\n|                  |\n|                  |\n|                  |\n|                  |\n|                  |\n''''''''''''''''''''\n        side")
  area_square=area_parachute/5 #m^2
  area_square_cm2=area_square*(10**4) #cm^2
  area_square_cm2_str=str(area_square_cm2)
  print("\nArea: " + area_square_cm2_str + " cm^2")
  
  side_square=math.sqrt(area_square) #m
  side_square_cm=side_square*(10**2) #cm
  side_square_cm_str=str(side_square_cm)
  print("Side: " + side_square_cm_str + " cm")

#Trials
print("\n\nTrials:")
print("\n       O ---\n          |\n          |\n          |\n          |\n          |\n          |\n          |\n       y  V")

#drag=0.5 * dragc * air_dens * area_parachute * (v**2)
#drag=kv^2
#k=0.5 * dragc * air_dens * area_parachute
k=0.5*dragc*air_dens*area_parachute
#k=0.035309263699054606
#a = g - ((k*v^2)/mass)
#a~= 9.8 - ((0.0353/v^2)/mass) #m/s^2
v_net=0
time_keeper=0 #s
v_t__dic={}
v_t__list=[]

if mode != "2":
  fraction=95 #%
  fraction_0_to_1=fraction/100
  fraction_str=str(fraction)
  step=0.1 #S
  step_str=str(step)
  step_lenght=1
  print("\nFraction of terminal velocity(%): " + fraction_str)
  print("Step: " + step_str + " s")
  
if mode == "2":
  fraction=int(input("\nFraction of terminal velocity(%): "))
  fraction_0_to_1=fraction/100
  fraction_str=str(fraction)
  step=float(input("Step(s): "))
  step_str=str(step)
  step_lenght=step_str[::-1].find('.')

for i in range(0, fraction, 1):
  while v_net < ((fraction_0_to_1)*v_term):
    v_net+=step*((g-((k*v_net*v_net)/m)))
    v_t__dic[time_keeper]=v_net #add exact values to dic
    list_int1=[str(round(time_keeper, step_lenght)), str(round(v_net, 3))] #add round values to list
    v_t__list.append(list_int1)
    time_keeper+=step
elapsed_time_str=str(round(time_keeper - step, 3))

distance_travelled=0 #m
y_t__dic={}
y_t__list=[]
for t,v in v_t__dic.items():
  distance_travelled+=step*v
  y_t__dic[t]=distance_travelled #add exact values to dic
  list_int2=[str(round(t, step_lenght)), str(round(distance_travelled, 3))] #add round values to list
  y_t__list.append(list_int2)
  
distance_travelled_str=str(round(distance_travelled, 3))

#PRINTING TRIAL RESULTS:
print("\nTime of flight until " + fraction_str + " % of terminal velocity is reached: " + elapsed_time_str + " s") #time
print("\nDistance travelled until " + fraction_str + " % of terminal velocity is reached: " + distance_travelled_str + " m") #distance

#GRAPH
answer=input("\nPretty graph? (Y/n): ")

if answer == "Y" or answer == "y":
  #printing v_t
  print("\n")
  print("Elapsed Time(s):     Velocity(m/s):")
  for row in v_t__list:
    print("".join(word.ljust(21) for word in row))
  #printing y_t
  print("\n")  
  print("Elapsed Time(s):     Distance travelled(m):")
  for row in y_t__list:
    print("".join(word.ljust(21) for word in row))
    
elif answer != "Y" and answer != "y":
  quit()
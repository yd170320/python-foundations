#Task 1
temp_celsius = float(input("Enter temperature:"))
radiation_level = int(input("Enter radiation level:"))
if temp_celsius<-60.0 and radiation_level>100:
    print("MARS ALERT:EXTREME HAZARD!EVACUATE ROVER")
elif temp_celsius<-60.0 or radiation_level>100:
    print("MARS ALERT:SINGLE HAZARD DETECTED ")
else:
    print("safe mission")
#Task 2
attacker_pos = float(input("Enter attacker's position:"))
defender_pos = float(input("Enter defender's position:"))
ball_realeased = True
if attacker_pos<defender_pos and ball_realeased:
    print('onside')
elif attacker_pos>defender_pos and ball_realeased:
    print("offside")
#Task 3
current_temperature = float(input("Enter current temperature:"))
is_occupied = bool(input("is room occupied by people:"))
if current_temperature>22.0 and not is_occupied:
    print("turn on AC(comfort mode)")
elif current_temperature>22.0 or is_occupied:
    print("turn on AC(eco mode)")
else:
    print("climate nominal.AC off") 

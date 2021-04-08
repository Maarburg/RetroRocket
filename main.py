# This is a re-make of "Rocket by 'Creative Computing' "

tab = str('   ')
time = 0
height = 500
velocity = 50
fuel = 120
burn = 0

print(tab*6+"ROCKET")
print(tab*2+"CREATIVE COMPUTING MORRISTOWN, NEW JERSEY\n")
print("LUNAR LANDING SIMULATION")
print("----- ------- ----------")

instructions = input("DO YOU WANT INSTRUCTION (YES OR NO): ")
if instructions.upper() == "YES":
    print("YOU ARE LANDING ON THE MOON AND HAVE TAKEN OVER MANUAL")
    print("CONTROL 500 FEET ABOVE A GOOD LANDING SPOT. YOU HAVE A")
    print("DOWNWARD VELOCITY OF 50 FT/SEC. 120 UNITS OF FUEL REMAIN.]n")
    print("HERE ARE THE RULES THAT GOVERN YOUR SPACE VEHICLE:")
    print("(1) AFTER EACH SECOND, THE HEIGHT, VELOCITY, AND REMAINING")
    print("    FUEL WILL BE REPORTED.")
    print("(2) AFTER THE REPORT A '?' WILL BE TYPED. ENTER THE")
    print("    NUMBER OF UNITS OF FUEL YOU WISH TO BURN DURING THE")
    print("    NEXT SECOND. EACH UNIT OF FUEL WILL SLOW YOUR DESCENT")
    print(" BY 1 FT/SEC.")
    print("(3) THE MAXIMUM THRUST OF YUR ENGINE IS 30 FT/SEC/SEC OR")
    print("    30 UNITS OF FUEL PER SECOND.")
    print("(4) WHEN YOU CONTACT THE LUNAR SURFACE, YOUR DESCENT ENGINE")
    print("    WILL AUTOMATICALLY CUT OFF AND YOU WILL BE GIVEN A")
    print("    REPORT OF YOUR LANDING SPEED AND REMAINING FUEL.")
    print("(5) IF YOU RUN OUT FO FUEL, THE '?' WILL NO LONGER APPEAR,")
    print("    BUT YOR SECOND-BY-SECOND REPORT WILL CONTINUE UNTIL")
    print("    YOU CONTACT THE LUNAR SURFACE.\n")
else:
    print("BEGINNING LANDING PROCEDURE.......\n")
    print("G O O D   L U C K ! ! !")
print("SEC"+tab+"FEET"+tab+"SPEED"+tab+"FUEL"+tab+"PLOT OF DISTANCE")
print(str(time)+"  "+tab+str(height)+tab+" "+str(velocity)+2*tab+str(fuel)+tab+"I"+(tab*(int(height/50))+"*"))
while height > 0:
    burn = int(input("?"))
    if fuel >0:  #TODO: Need to write the else
        if burn > 30:
            burn = 30
        velocity1 = velocity - burn + 5
        fuel2 = (fuel - burn)
        fuel = fuel2
        height = height - .5 * (velocity + velocity1)
        time += 1
        velocity = velocity1
    print(str(time) + "  " + tab + str(height) + tab + " " + str(velocity) + 2 * tab + str(fuel) + tab + "I" + (tab * (int(height / 50)) + "*"))

    if height <= 0:
        print("***** CONTACT *****")




# INPUT B               Get Burn
# IF B<0 THEN 650       If burn is less then 0 make burn 0
# IF B>30 THEN B=30     if burn is more than 30 make burn 30
# IF B>F THEN B=F       if burn is greater than fuel burn equals fuel
# V1=V-B+5              new velocity = velocity - burn + 5
# F=F-B                 fuel = fuel -burn
# H=H-.5*(V+v1)         height = height minus half of velocity + new velocity
# IF H<=0 THEN 670      if height <= 0 then "CONTACT"
# T=T+1                 time = time + 1
# V=V1                  velocity = new velocity
# IF F>0 THEN 490       if fuel greater then 0  print stat line
# IF B=0 THEN 640       if burn is 0 then print stat line

# PRINT "**** OUT OF FUEL****"
# B=0
# GOTO 540
# PRINT "**** CONTACT ****":PRINT
# H=H+.5*(V+V1)
# IF B=5 THEN 720
# GOTO 730
# D=H/V
# V1=V+(5-B)*D
# PRINT "TOUCHDOWN AT ";T+D;" SECONDS."
# PRINT "LANDING VELOCITY = ";V1;" FEET/SEC."
# PRINT F;" UNITS OF FUEL REMAINING."
# IF V1<>0 THEN 810
# PRINT "CONGRATULATIONS!   A PERFECT LANDING!"
# IF ABS(V1)<2 THEN 840
# PRINT "**** SORRY, BUT YOU BLEW IT!!!!":PRINT
# PRINT "APPROPRIATE CONDOLENCES WILL BE SENT TO YOUR NEXT OF KIN."
# PRINT: PRINT: PRINT
# INPUT "ANOTHER MISSION ";A$
# IF A$="YES" THEN 390
# PRINT: PRINT "CONTROL OUT.": PRINT

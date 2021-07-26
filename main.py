import Functions

# Propeller
Pitch = 4.5  #inch
Diameter = 9 #inch

# Motor
AmpRate = 24.2 / 1.180    #I/kg

# Battery
Cap = 2200/1000   #Ah

Eff=0.8

# Drone Weight
Weight = 0.86  #kg




Fg = Weight * 9.8
K = Functions.LiftCoefficient(Pitch,Diameter)

#Hovering State
print("Hovering State")
AmpDraw = Functions.Motion(AmpRate,Fg,K,Weight,0)
Functions.FlightTime(AmpDraw,Cap,Eff)

# Motion at angle 30 degrees at constant altitude
print("\n\nMotion at angle 30 degrees at constant altitude")
AmpDraw = Functions.Motion(AmpRate,Fg,K,Weight,30)

# Upward movement at 1m/s^2
print("\n\nUpward movement at 1m/s^2")
Fz = Weight*(9.8+1)
AmpDraw = Functions.Motion(AmpRate,Fz,K,Weight,0)

# Motion at Acceleration 2.6m/s^2 horizontally
print("\n\nMotion at Acceleration 2.6m/s^2 horizontally")
AmpDraw = Functions.Motion2(AmpRate,Fg,2.6,K,Weight)

# Motion at Acceleration 2.6m/s^2 horizontally and 1m/s^2 vertically
print("\n\nMotion at Acceleration 2.6m/s^2 horizontally and 1m/s^2 vertically")
Fz=Weight*(9.8+1)
AmpDraw = Functions.Motion2(AmpRate,Fz,2.6,K,Weight)


Functions.Graph1(AmpRate,K,Weight)
Functions.Graph2(AmpRate,K,Weight)
Functions.Graph3(AmpRate,Fz,K,Weight)
Functions.Graph4(AmpRate,K,Weight)




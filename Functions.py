import math
from matplotlib import pyplot as plt

def LiftCoefficient(p,d): 
    a=4.392399*(math.pow(10,-8))
    d1=(math.pow(d,3.5))
    p1=(math.pow(p,0.5))
    k = a*(d1/p1)*(4.23333*(math.pow(10,-4))*p)
    return k

def Motion(AmpRate,Fg,K,Weight,a):
    angle = math.radians(a)
    Fz = Fg
    Ft = Fz / (math.cos(angle))
    w = math.pow((Ft / (4 * K)), 0.5)
    print("Rpm of each Rotor = ",w)
    Fx = Ft * (math.sin(angle))
    Ax = Fx / Weight
    print("Acceleration along X axis = ",Ax)
    EffectiveWeight=Ft/9.8
    AmpDraw=AmpRate*EffectiveWeight
    print("Average Ampere Draw of each motor =",(AmpDraw/4))
    return AmpDraw


def Motion2(AmpRate,Fg,Ax,K,Weight):
    Fx=Ax*Weight
    Fz=Fg
    angle = math.atan(Fx/Fz)
    print("Angle Of Attack =",math.degrees(angle))
    Ft = Fz / (math.cos(angle))
    w = math.pow((Ft / (4 * K)), 0.5)
    print("Rpm of each Rotor = ", w)
    EffectiveWeight = Ft / 9.8
    AmpDraw = AmpRate * EffectiveWeight
    print("Average Ampere Draw of each motor =", (AmpDraw / 4))
    return AmpDraw

def FlightTime(AD,Cap,Eff):
    Ft=(Cap/AD)*Eff*3600
    print("Flight Time = ",Ft," = ",(Ft/60))


def Graph3(AmpRate,Fg,K,Weight):
    AX=[0,0.5,1,1.5,2,2.5,3,3.5,4,4.5,5]
    AD = []
    for i in AX:
        Fx = i * Weight
        Fz = Fg
        angle = math.atan(Fx / Fz)
        Ft = Fz / (math.cos(angle))
        EffectiveWeight = Ft / Fg * Weight
        AmpDraw = AmpRate * EffectiveWeight
        AD.append(AmpDraw)
    plt.plot(AX, AD)
    plt.title("AmpDraw Vs Horizontal Acceleration")
    plt.ylabel('Ampdraw in A')
    plt.xlabel("Acceleration in m/s^2")
    plt.show()

def Graph4(AmpRate,K,Weight):
    AZ=[0,0.5,1,1.5,2,2.5,3,3.5,4,4.5,5]
    AD = []
    for i in AZ:
        Fx = 0 * Weight
        EffectiveWeight = ((9.8+i)/9.8)*Weight
        AmpDraw = AmpRate * EffectiveWeight
        AD.append(AmpDraw)
    plt.plot(AZ, AD)
    plt.title("AmpDraw Vs Vertical Acceleration")
    plt.ylabel('Ampdraw in A')
    plt.xlabel("Acceleration in m/s^2")
    plt.show()


def Graph1(AmpRate, K, Weight):
    AZ = [0, 0.5, 1, 1.5, 2, 2.5, 3, 3.5, 4, 4.5, 5]
    AD = []
    FT=[]
    for i in AZ:
        Ft = i*3
        EffectiveWeight = Ft/9.8
        AmpDraw = AmpRate * EffectiveWeight
        AD.append(AmpDraw)
        FT.append(Ft)
    plt.plot(FT, AD)
    plt.title("AmpDraw Vs Thrust Force")
    plt.ylabel('Ampdraw in A')
    plt.xlabel("Thrust in N")
    plt.show()

def Graph2(AmpRate, K, Weight):
    AZ = [0, 0.5, 1, 1.5, 2, 2.5, 3, 3.5, 4, 4.5, 5]
    AD = []
    W = []
    for i in AZ:
        Ft = i * 3
        w = math.pow((Ft / (4 * K)), 0.5)
        EffectiveWeight = Ft / 9.8
        AmpDraw = AmpRate * EffectiveWeight
        AD.append(AmpDraw)
        W.append(w)
    plt.plot(AD,W)
    plt.title("Rpm Vs AmpDraw")
    plt.xlabel('Ampdraw in A')
    plt.ylabel("Rpm of propeller")
    plt.show()
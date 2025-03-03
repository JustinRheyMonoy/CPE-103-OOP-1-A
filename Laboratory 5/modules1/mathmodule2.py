import math

def angle_demo(): 
    angle = math.sin(math.pi/2) # the default input is in radians 
    # angle sin(90)=1 in degrees == sin(pi/2)=1 in radians
    print(angle)
    # to make it convenient, convert to radians
    angle = math.sin(math.radians (90))
    print(angle)
    # this is also similar for cosine and other trigonometric and #hyperbolic functions
    #hyperbolic functions
    
angle_demo()
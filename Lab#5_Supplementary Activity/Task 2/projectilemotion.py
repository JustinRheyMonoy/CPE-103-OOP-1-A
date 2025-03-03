import math

def projectilemotion_solver(velocity, angle):
    g = 9.8
    
    angle_rad = math.radians(angle)
      
    range_distance = (velocity ** 2 * math.sin(2 * angle_rad)) / g
    
    max_height = (velocity ** 2 * (math.sin(angle_rad) ** 2)) / (2 * g)
    
    return range_distance, max_height

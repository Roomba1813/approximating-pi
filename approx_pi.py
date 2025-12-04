import random
import math

def circumference_pi(n):
    circum = 0

    for i in range(n-1):
        theta = i*(math.pi/2)/(n-1)
        theta_next = (i+1)*(math.pi/2)/(n-1)
        x = math.cos(theta)
        y = math.sin(theta)
        x_plus_1 = math.cos(theta_next)
        y_plus_1 = math.sin(theta_next)

        dist_x = x-x_plus_1
        dist_y = y-y_plus_1
        dist = math.sqrt(dist_x**2+dist_y**2)

        circum+=dist
    circum_pi = 2*circum
    return circum_pi

def calc_dartboard_pi(n):
    in_circle = 0
    total = n
    for i in range(n):

        x = random.uniform(-1, 1)
        y = random.uniform(-1, 1)
        dist_square = x**2+y**2
        if dist_square <= 1:
            in_circle += 1
    
    dartboard_pi = 4*in_circle/total
    return dartboard_pi

def calc_basel_pi(n):

    basel_sum = 0
    for i in range(n):
        basel_sum+=1/((i+1)**2)

    basel_pi = math.sqrt(6*basel_sum)
    return basel_pi

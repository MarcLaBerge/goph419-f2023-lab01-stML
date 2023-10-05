

import numpy as np

#Testing arcsin function
from launch import arcsin
x = 0.5
y = arcsin(x)
print("Arcsin Test")
print(y)
expected = 0.5235
print(expected)



#Testing to see if my Launch angle works
from launch import launch_angle
ve_v0 = 2
alpha = 0.25
y = launch_angle(ve_v0,alpha)
print("\n\nlaunch angle test")
print(y)
expected = 0.5931997761
print(expected)

#Testing the launch angle range
from launch import launch_angle_range
ve_v0 = 2
alpha = 0.25
tol_alpha = 0.02

y = launch_angle_range(ve_v0,alpha,tol_alpha)
print("\n\nLaunch angle range test")
print(y)
expected = 0.5740889, 0.61185996
print(expected)


from tests import test
ve_v0 = 2
alpha = 0.25
print("\n\ntest Test")
y = test(ve_v0,alpha)
print(y)

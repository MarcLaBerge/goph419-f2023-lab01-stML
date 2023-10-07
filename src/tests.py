"""A function that test the launch_angle script so sensible 
errors are raised when errors occur. This then limits the output
of the launch_angle_range script when extreem values are entered


Parameters
----------
Ration of escape velocity to termonal velocity
    ve_v0 : float 

    Ratio of the target altitude relative to the Earth's radius
    alpha : float
Return
------



"""
import numpy as np


def test(ve_v0, alpha):
    from launch import launch_angle

    #Check that the q is positive
    x = 1.0 - (alpha / (1.0 + alpha)) * ve_v0**2
    if x < 0.0:
        print("Test Failed, value calculated,"(1.0 - (alpha / (1.0 + alpha)) * ve_v0**2), "Should be positive")
    else:
        print(f"Test Passed, for values of alpha = {alpha} and ve_v0 = {ve_v0}")

    #Check that sin(x) is less than or equal to 1, arcsin(x>1) is out of domain
    x = (1.0 + alpha)*np.sqrt(x)
    if (1.0 + alpha)*np.sqrt(x) > 1.0:
        print("Test Failed, value calculated,",(1.0 + alpha)*np.sqrt(x),"Should be less than or equal to 1")
    else:
        print(f"Test Passed, for values of alpha = {alpha} and ve_v0 = {ve_v0}")


    #if tests are passed
    y = launch_angle(ve_v0,alpha)

    return y


#Testing functions and values


#Testing arcsin function
from launch import arcsin
x = 0.5
y = arcsin(x)
print("Arcsin Test")
print(y)
expected = 0.5235
print(expected)

    #Arcsin when x is negative
x = -0.5
y = arcsin(x)
print("Arcsin Test (negative)")
expected = -0.52359
print(y)
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

    #Extreme values
print("\n\nlaunch angle extreme ve_v0 test")
ve_v0 = 20
alpha = 0.25
y = launch_angle(ve_v0,alpha)
print(y)
expected = "nan"
print(expected)

#Testing the launch angle range
from launch import launch_angle_range
ve_v0 = 2
alpha = 0.25
tol_alpha = 0.02
print("\n\nLaunch angle range test")
y = launch_angle_range(ve_v0,alpha,tol_alpha)
print(y)
expected = 0.5740889, 0.61185996
print(expected)


ve_v0 = 2
alpha = 0.25
print("\n\ntest Test")
y = test(ve_v0,alpha)
print(y)
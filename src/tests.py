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

    #sqrt < 1
    q = 1.0 - (alpha / (1.0 + alpha)) * ve_v0**2
    if q < 0.0:
        print("Values give negative in sqrt")
    else:
        print(f"Test Passed, for values of alpha = {alpha} and ve_v0 = {ve_v0}")

    #sin > 1.0
    #x = (1.0 + alpha)*np.sqrt(q)
        if (1.0 + alpha)*np.sqrt(q) > 1.0:
            print("Test Failed, value calculated,",(1.0 + alpha)*np.sqrt(q),"Should be less than 1")
        else:
            print(f"Test Passed, for values of alpha = {alpha} and ve_v0 = {ve_v0}")


    #if tests are passed
    y = launch_angle(ve_v0,alpha)

    return y


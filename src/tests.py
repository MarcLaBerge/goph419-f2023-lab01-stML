"""Testing perameters





"""
import numpy as np


#testing the launch angle range
alpha = 2.0
ve_v0 = 2
tol_alpha = 0.02

def test(ve_v0, alpha, tol_alpha):
    from launch import launch_angle_range

    #sqrt < 1
    q = 1.0 - (alpha / (1.0 + alpha)) * ve_v0**2
    if q < 0.0:
        print("Values give negative in sqrt")
    else:
        print(f"Test passed for values of alpha = {alpha} and ve_v0 = {ve_v0}")

    #sin(x) > 1.0
    x = (1.0 + alpha)*np.sqrt(q)
    if x > 1.0:
        print("Outside of range")
    else:
        print(f"Test passed for values of alpha = {alpha} and ve_v0 = {ve_v0}")


#if tests are passed
    y = launch_angle_range(ve_v0,alpha,tol_alpha)
    return y

    
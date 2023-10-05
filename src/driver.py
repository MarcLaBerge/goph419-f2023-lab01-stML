"""Driver script for Assignment #1.

See Also
--------
- Assignment description for mathematical and physics background.
- launch.py for documentation of variables and functions.
"""
import numpy as np
import matplotlib.pyplot as plt

from launch import (
        min_altitude_ratio,
        max_altitude_ratio,
        min_velocity_ratio,
        max_velocity_ratio,
        launch_angle_range,
)


def main():
    """Plot launch angle ranges given
    values for ve_v0, alpha, and tol_alpha.
    """
    

    #holding the velocity ratio and the tol_alpha constant
    ve_v0 = 2
    tol_alpha = 0.04

    min_alpha_angle = []
    max_alpha_angle = []
    #set the range of acceptable alphas calculated from setting the boundary conditions and rearanging for max alpha
    alpha_range = np.arange(0, max_altitude_ratio(ve_v0), 0.05)                   #Look at the code for the min --- should equal 0 when ve_v0 is 2
    for i in alpha_range:
        y = launch_angle_range(ve_v0, i, tol_alpha)
        min_alpha_angle.append(y[0])
        max_alpha_angle.append(y[1])
    
    print("Maximum angles: ", max_alpha_angle)
    print("Minimum angles: ", min_alpha_angle)

    figure, axis = plt.subplots(1, figsize=(10, 10))
    plt.plot(alpha_range, min_alpha_angle, label = "Minimum Launch Angle")
    plt.plot(alpha_range, max_alpha_angle, label = "Maximum Launch Angle")
    plt.xlabel("Alpha")
    plt.ylabel("Launch Angle")
    plt.title("The Minimum and Maximum Launch Angles for a fixed ve_v0 and tol_alpha against Alpha")
    plt.legend()
    plt.show()
    #plt.savefig("Graphs of Launch Angle vs constant Alpha and ve_v0 respectively")
    
    #holding alpha and tol_alpha constant
    alpha = 0.25
    tol_alpha = 0.04

    min_ve_v0_angle = []
    max_ve_v0_angle = []

    ve_v0_range = np.arange(1.34,2.24, 0.025) #Look at the coded functions, they give these numbers but don't go through the code
    for i in ve_v0_range:
        y = launch_angle_range(i, alpha, tol_alpha)
        min_ve_v0_angle.append(y[0])
        max_ve_v0_angle.append(y[1])

    print("Maximum angles: ", max_ve_v0_angle)
    print("Minimum angles: ", min_ve_v0_angle)

    figure, axis = plt.subplots(2, figsize=(10, 10))
    plt.plot(ve_v0_range, min_ve_v0_angle, label = "Minimum Launch Angle")
    plt.plot(ve_v0_range, max_ve_v0_angle, label = "Maximum Launch Angle")
    plt.xlabel("ve_v0")
    plt.ylabel("Launch Angle")
    plt.title("The Minimum and Maximum Launch Angles for a fixed alpha and tol_alpha against ve_v0")
    plt.legend()
    plt.show()
    
        


    



    # plot launch angle range for a fixed target altitude
    

if __name__ == "__main__":
    main()
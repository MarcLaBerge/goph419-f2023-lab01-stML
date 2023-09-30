"""Functions for GOPH 419 Lab Assignment #1."""

import numpy as np


def arcsin(x):
    """Compute the inverse sine of x on the range [-pi/2, pi/2]. 
    Perameters
    ----------
    x: float
        The argument of the arcsin function.
    Returns
    -------
    float
        The resultant value of the arcsin function.
    """
    #Check that x is negative and make it positive if it is
    sign = 1.0
    if x < 0.0:
        sign = -1.0
        x = np.abs(x) #Don't have to worry about the negative(for the sqrt) if we take it away and bring it back later
    if x >1.0:
        raise ValueError(f"input abs({sign * x}) > 1.0 is out of range")
    
    eps_s = 0.5e-5 #exponent it the amount of decimal place of percition we want
    if x < eps_s:
        return sign * x 
    
    #starting values
    two_x = 2.0 * x 
    k = 0
    max_k = 50 
    fact_k = 1 #Not 0 or could cause problems
    fact_2k = 1 #Not 0 or could cause problems
    result = 0.0 #Result starts at 0
    eps_a = 1.0 #Approx relative error starts at 1
    #taylor series continues
    while eps_a > eps_s and k < max_k: #Breaking it down 
        k += 1
        two_k = 2.0* k
        fact_k *= k
        fact_2k *= two_k * (two_k - 1)

        term = 0.5 * (two_x ** two_k) / (k ** 2 * fact_2k / fact_k)
        result += term

        eps_a = term / result #term is the difference between the sum and 

    return np.sqrt(result) * sign



######################################################################################
def launch_angle(ve_v0, alpha):
    """Calculate the launch angle from vertical given
    velocity ratio and target altitude ratio.
    Perameters
    ----------
    Ration of escape velocity to termonal velocity
    ve_v0 : float 

    Ratio of the target altitude relative to the Earth's radius
    alpha : float

    Returns
    -------
    float 
        Launch angle from vetical in radians
    """
    #Value what don't work
    #relative velocities
    if ve_v0 > 1.0: 
        raise ValueError(f"invalid value ve_v0 = {ve_v0} > 1.0") #if we start with less velocity than needed, we can't escape
    
    #break up equation 17
    q = 1.0 - (alpha / (1.0 + alpha)) * ve_v0**2

    x = (1.0 + alpha)*np.sqrt(q)

    y = arcsin(x)

    return y



######################################################################################
def launch_angle_range(ve_v0, alpha, tol_alpha):
    """Calculate the range of launch angles for a given
    velocity ratio, target altitude ratio, and tolerance.
    Perameters
    ----------
    Ration of escape velocity to termonal velocity
    ve_v0 : float 

    Ratio of the target altitude relative to the Earth's radius
    alpha : float

    Tolerance for Alpha 
    tol_alpha : float

    Returns
    -------
    float:
        launch angle range will be given in radians
    """
    max_altitude = (1 + tol_alpha) * alpha
    min_altitude = (1 - tol_alpha) * alpha

    #min launch angle from max altitude
    min_angle = launch_angle(ve_v0,max_altitude)
                                                      #launch angle uses arcsin (implementation of equation 17 and 18)
    #max launch angle from min altitude
    max_angle = launch_angle(ve_v0,min_altitude)
    
    phi_range = np.array(min_angle,max_angle)
    
    return phi_range



#############################################################################################
def min_altitude_ratio(ve_v0):
    """Utility function for computing minimum possible peak altitude ratio
    for a given velocity ratio.
    Perameters
    ----------
    sin(x) = 1 (x=pi/2)
        Angle when leaving is horizontal

    Reterns
    -------
    float :
        min_altitude_ratio will be given in ratio no units
    """
    alpha_min = (-(ve_v0) ** 2 + 2) / ((ve_v0) ** 2 - 1)

    #ve_v0  cannot be 0 (0 escape velocity?) and cannot be 1
    return alpha_min



##############################################################################################
def max_altitude_ratio(ve_v0):
    """Utility function for computing maximum possible peak altitude ratio
    for a given velocity ratio.
    Perameters
    ----------
    sin(x) = 0
        Angle when leaving is vertical
    Reterns
    -------
    float:
        max_altitude_ratio will be given in ratio no units

    """
    alpha_max = 1 / ((ve_v0) ** 2 - 1)
    #ve_v0 cannot be 1
    return alpha_max


def min_velocity_ratio(alpha):
    """Utility function for computing minimum possible velocity ratio
    for a given target peak altitude ratio.
    Perameters
    ----------
    sin(x) = pi/2
        At this angle we will need the more initial velocity  

    """
    p = (((1 + alpha) ** 2) - 1) / (alpha + (alpha ** 2))
    ve_v0_min = np.sqrt(p)

    return ve_v0_min


def max_velocity_ratio(alpha):
    """Utility function for computing maximum possible velocity ratio
    for a given target peak altitude ratio.
    Perameters
    ----------
    sin(x) = 0
        Least amount of initial velocity to get far

    """
    o = (1 + alpha) / alpha
    ve_v0_max = np.sqrt(o)

    return ve_v0_max
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
        x = np.abs(x) 
    
    #Check that 
    if x > 1:
        raise ValueError(f"input abs({sign * x}) > 1.0 is out of range")
    #exponent it the amount of decimal place of percition we want
    eps_s = 0.5e-5
    if x < eps_s:
        return sign * x 
    
    #starting values
    two_x = 2.0 * x 
    k = 0
    max_k = 100
    fact_k = 1 
    fact_2k = 1 
    result = 0.0 
    eps_a = 1.0 

    #taylor series continues
    while eps_a > eps_s and k < max_k: 
        k += 1
        two_k = 2.0 * k
        fact_k *= k
        fact_2k *= two_k * (two_k - 1)

        term = 0.5 * (two_x ** two_k) / ((k ** 2) * fact_2k / (fact_k ** 2))
        result += term

        eps_a = term / result 

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
    
    #break up equation 17
    q = 1.0 - (alpha / (1.0 + alpha)) * ve_v0**2
    if q < 0:
        print("Test Failed, value calculated in square root should be positive")
        
    
    x = (1.0 + alpha)*np.sqrt(q)
    y = arcsin(x)
        
    #use arcsin function to get angle
    

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
    phi_range as an array to store minimum and maximum launch angles
    """
    #import the function "tests" to check the launch angle range
    from tests import test
    y = test(ve_v0,alpha)

    #defining the max and min altitudes
    max_altitude = (1 + tol_alpha) * alpha
    min_altitude = (1 - tol_alpha) * alpha

    #creating an array for the values
    phi_range = []


####launch angle uses arcsin (implementation of equation 17 and 18)
    #min launch angle from max altitude
    min_angle = launch_angle(ve_v0, max_altitude)

        #add to array
    phi_range.append(min_angle)
    

    #max launch angle from min altitude
    max_angle = launch_angle(ve_v0, min_altitude)

        #add to array
    phi_range.append(max_angle)
    
    
    return phi_range



#############################################################################################
def min_altitude_ratio(ve_v0):
    """Utility function for computing minimum possible peak altitude ratio
    for a given velocity ratio.
    Perameters
    ----------
    sin(x) = 1 (x=pi/2)
        Angle when launch is horizontal

    Reterns
    -------
    float :
        min_altitude_ratio will be given in ratio no units
    """
    #in equation 17, solve for alpha when sin(phi) = 0 
        #the smallest alpha = 0
    alpha_min = 0

    return alpha_min



##############################################################################################
def max_altitude_ratio(ve_v0):
    """Utility function for computing maximum possible peak altitude ratio
    for a given velocity ratio.
    Perameters
    ----------
    sin(x) = 0 (x=0)
        Angle when leaving is vertical
        In the sin function created earlier, I use x, x = phi
    Reterns
    -------
    float:
        max_altitude_ratio will be given in ratio no units

    """
    #in equation 17, solve for alpha when sin(phi) = 1
    alpha_max = - (1 / (1 - (ve_v0) ** 2))
   
    return alpha_max

##################################################################################
def min_velocity_ratio(alpha):
    """Utility function for computing minimum possible velocity ratio
    for a given target peak altitude ratio.
    Perameters
    ----------
    sin(x) = 1 (x=pi/2)
        At this angle we will need the more initial velocity which gives a smaller ratio 
        In the sin function created earlier, I use x, x = phi
    Return
    ------
    float:
        min_velocity_ratio will be given with no units

    """
    #in equation 17, solve for ve_v0 when sin(phi) = 1
    p = ((alpha + 2) / (alpha + 1))
    ve_v0_min = np.sqrt(p)

    return ve_v0_min

##################################################################################
def max_velocity_ratio(alpha):
    """Utility function for computing maximum possible velocity ratio
    for a given target peak altitude ratio.
    Perameters
    ----------
    sin(x) = 0 (x=0)
        At this angle we will need less initial velocity which gives a bigger ratio
        In the sin function created earlier, I use x, x = phi

    Return
    ------
    float:
        max_velocity_ratio will be given with no units

    """
    #in equation 17, solve for ve_v0 when sin(phi) = 0
    o = ((1 + alpha) / alpha )
    ve_v0_max = np.sqrt(o)

    return ve_v0_max


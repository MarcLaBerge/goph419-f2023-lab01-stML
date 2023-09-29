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
    
    eps_s = 0.5e-5 #exponent it the amount of decimal place
    if x < eps_s:
        return sign * x 
    
    #starting values
    two_x = 2.0 * x 
    n = 0
    max_n = 50 
    fact_n = 1 #Not 0 or could cause problems
    fact_2n = 1 #Not 0 or could cause problems
    result = 0.0 #Result starts at 0
    eps_a = 1.0 #Approx relative error starts at 1
    #taylor series continues
    while eps_a > eps_s and n < max_n: #Breaking it down 
        n += 1
        two_n = 2.0* n
        fact_n *= n
        fact_2n *= two_n * (two_n - 1)

        term = 0.5 * (two_x ** two_n) / (n**2 * fact_2n / fact_n)
        result += term

        eps_a = term / result 

    return np.sqrt(result) * sign


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
    
    Raises
    ------
    ValueError
        If invalid combination of ve_v0 and alpha is resulted

    **ve_v0 < 1.0 (this is means that we have started with more than enough velocity)

    **alpha has to be <= 1/ (ve_v0**2 - 1)
    ---> ValueError if this is not the case
    """
    if ve_v0 > 1.0: 
        raise ValueError(f"invalid value ve_v0 = {ve_v0} > 1.0") #if we start with less velocity than needed, we can't escape
    d = 1.0 - (alpha / (1.0 + alpha)) * ve_v0**2
    if d < 0.0: #we can't go back into the earth/d can't be negative be of sqrt
        alpha_max = 1.0 / (ve_v0**2 - 1)
        raise ValueError(f"invalid value alpha = {alpha} > {alpha_max}")
    x = (1.0 + alpha)*np.sqrt(d)

    return arcsin(x)


def launch_angle_range(ve_v0, alpha, tol_alpha):
    """Calculate the range of launch angles for a given
    velocity ratio, target altitude ratio, and tolerance.
    Perameters
    ----------
    
    Returns
    -------
    float:
        launch angle range will be given in radians
    Raises
    ------
    ve_v0 >= 1.0 
        To escape we need atleast the escape velocity 
    alpha <= 1/(ve_v0**2 - 1)
    """
    
    phi_range = 5
    return phi_range


def min_altitude_ratio(ve_v0):
    """Utility function for computing minimum possible peak altitude ratio
    for a given velocity ratio.
    Perameters
    ----------
    ve_v0 = 1.0
        The minimum required velocity to escape
    R = 6378100 (in meters)
    Reterns
    -------
    float :
        min_altitude_ratio will be given in meters
    Raises
    ------
    d < R
        Then the ratio is now into the ground lol
    ve_v0 < 1
        No longer the min altitude

    """
    R = 6378100
    d = 1 + 1/(ve_v0**2-1)
    if d < 6378100:
        raise ValueError(f"invalid value {ve_v0}<1")
    dmin_R = d / R

    return ...


def max_altitude_ratio(ve_v0):
    """Utility function for computing maximum possible peak altitude ratio
    for a given velocity ratio.
    Perameters
    ----------
    ve_v0 = 0.0
        We have more initial velocity than needed to escape
    Reterns
    -------
    float:
        max_altitude_ratio will be given in (m)

    Raises
    ------
    ve_v0 > 0
        anything bigger than 0 will not give the max altitude
    """
    R = 6378100
    d = 1 + 1/(ve_v0**2-1)
    if d > 0:
        raise ValueError(f"invalid value {ve_v0} > 0")
    dmax_R = d/R

    return ...


def min_velocity_ratio(alpha):
    """Utility function for computing minimum possible velocity ratio
    for a given target peak altitude ratio.
    Perameters
    ----------
    alpha = 0
        You'll get the smallest escape velocity if the object is leaving horizontally

    """
    #add your code here

    return ...


def max_velocity_ratio(alpha):
    """Utility function for computing maximum possible velocity ratio
    for a given target peak altitude ratio.
    Perameters
    ----------
    alpha = pi/2

    """
    #add your code here

    return ...
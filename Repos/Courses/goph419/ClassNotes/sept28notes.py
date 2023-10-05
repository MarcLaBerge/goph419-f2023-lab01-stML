#Hopefully helpful with the lab 1:)
#Exponential
def exp(x):
    """Compute the values of the exponential function for real valued scalar input.
    Perameters
    ----------
    x : float_like
        The argument of theexponential function
    Returns
    -------
    float
        The value of the exponential function at x
    """
    x = float(x) #using a premade function so we don't have to go through all the if statements
    tol = 1e-16
    eps_a = 2 #could be anything so that the loop runs atleast once
    sum = 0.0
    k = 0
    fact_k = 1

    while eps_a > tol: #tol starts for error tolarance - eps_s
        term = x ** k / fact_k
        sum += term
        eps_a = abs(term/sum) #term = change in the sum already current - previous
        k += 1
        fact_k *= k
    return sum

def sin(x):
    """Compute values of the sine function for real-value scalar input.
    Perameters
    ----------
    x : float_like
        The argument of theexponential function
    Returns
    -------
    float
        The value of the exponential function at x
    """
    x = float(x) #using a premade function so we don't have to go through all the if statements
    tol = 1e-16
    eps_a = 2 #could be anything so that the loop runs atleast once
    sum = 0.0
    k = 0
    fact_k = 1

    while eps_a > tol: #tol starts for error tolarance - eps_s
        term = (-1) ** k * x ** (2 * k + 1)/fact_k
        sum += term
        eps_a = abs(term/sum) #term = change in the sum already current - previous
        k += 1
        fact_k *= (2 * k) * (2 * k + 1)
    return sum

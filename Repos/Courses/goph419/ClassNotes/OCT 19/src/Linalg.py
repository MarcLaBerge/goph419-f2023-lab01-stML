import numpy as np
#DONT RUN UNTIL VIRTUAL ENVIRONMENT HAS BEEN INPLEMENTED

def solve(a, B):
    """(docstring) Solve a linear system using Gauss elimination.

    Parameters
    ----------
    a : numpy.ndarray, shape = (M, M)
        The coefficient Matrix
    b : numpy.ndarray, shape = (M,)
        The dependant variable values
    
    Retunrs
    -------
    numpy.ndarray, shape=(M,)
        the solution vector
    
    """
    #ensures that the coef matrix and rhs vector are ndarrays
    a = np.array(a, dtype = float)
    B = np.array(B, dtype = float)
    #make sure that the coef matrix is square
    m = len(a)#returns number of rows
    ndim = len(a.shape)
    if ndim != 2:#has to be a 2d array
        raise ValueError(f"A has {ndim} dimensions" + ", should be 2")
    
    if a.shape[1] != m:
        raise ValueError(f"A has {m} rows and {a.shape[1]} cols" + ", should be square")
    
    #making sure b is one dimensional(right hand side)
    ndimb = len(B.shape)
    if ndimb != 1:
        raise ValueError(f"b has {ndimb} dimensions" + ", should be 1D")
    
    #make sure the amount of right hand side values matches the nuber of equations
    if len(B) != m:
        raise ValueError(f"A has {m} rows, B has {len(B)} values" + ", dimensions incompatible")
    
    aug = np.hstack([a, np.reshape(B, (m,1))]) #stacking B agains A Horizontally, can also do vetically vstack (Augmented matrix) -> [A|B]






    #solve by the Gauss Elimination algorithm
        #k is the pivot row
    for k in range(m): #stopping point

        # Perform Partical Poviting -> incase the pivot is 0
        piv = np.abs(aug[k,k])
        kpiv = k
        for k1 in range(k+1,m):
            piv1 = np.abs(aug[k1,k])
            if piv1 > piv:
                kpiv = k1
                piv = piv1
        #Swaping the 2 rows

        aug[k, :], aug[kpiv, :] = np.array(aug[kpiv, :]), np.array(aug[k, :])
        #np.array makes sure that we are passing the values and not the references -> "Deep Copy"



    #calculate the elimination coefficients
    #slice = start(:stop(:step)) - another way of lookin at it #starting at starting row, ending not including the final row
    #leaving the start or stop blank means, using all the rows, from the start or till the end
        aug[k+1:, k] = aug[k+1:, k] / aug[k,k] #could write aug[k+1:, k] /= aug[k,k]

    #eliminate below pivot
    #we are at pivot row 0, so we are starting in row 1
    #won't include m but the index of a m x m matrix is m-1 anyways
        for j in range(k+1,m):
        #start from 1 after the pivot column (0) and go to the b matrix
            aug[j, k+1:] -= aug[j, k] * aug[k, k+1:] #1: must be the same for both sides


    #Perform backward subsitution
    #   index is m-1 even if it's an mxm matrix 
    for k in range(m-1,-1,-1): #can also write range(-1,-(m+1),-1): -> more confusing
        #could also use m not -1... we want to stop at m
        aug[k, -1] = (aug[k, -1]-np.dot(aug[k, k+1:m], aug[k+1:, -1]))/aug[k, k]
    
    #return the solution
        #: means all the values in the dimention - rows in this example
    return aug[:, -1]

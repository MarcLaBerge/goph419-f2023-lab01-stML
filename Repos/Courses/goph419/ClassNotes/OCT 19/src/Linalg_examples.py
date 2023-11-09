import numpy as np
#DON"T RUN UNTIL VIRTUAL ENVIRONMENT IS ON
#would need to make a Goph virtual environment for this code to run in the evironment
def main():
    A = np.array(
        [
            [15, -10, 0],
            [-10, 25, -15],
            [0, -15, 15],
        ]
        dtype = float, #you could use int as well
    )
    print(f"A.shape = {A.shape}")
    # prints out (3,3) because it is a 3x3 matrix
    print(A) #you can see the matrix

    B = np.array([5.0,4.0,2.0]) #.0 will also make sure that it is a float
    B = np.reshape(B, (len(B), 1)) #This will make it a 3,1 matrix
    print(f"B.shape = {B.shape}")
    # prints out (3,) because it is a 3x1 matrix
    print(B)#you can see the matrix

    
    
    aug = np.hstack([A,B])
    print(f"aug.shape = {aug.shape}") #will print a 3x4
    print(aug)

    x = np.linalg.solve(A, B)
    print(f"x.shape = {x.shape}")


if __name__ == "__main__":
    main()
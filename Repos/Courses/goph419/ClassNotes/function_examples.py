import numpy as np

from sept28notes import ( 
    exp,
    )

def main ():
    x = 1.0
    expected = np.exp(x)
    result = exp(x)
    eps = (result - expected)/ expected
    print(f"testing exp({x:0.16e})")
    print(f"expected: {expected:0.16e}") #print with 16 digits of percision, 0 is the field width (fill change to fit the number, can specify if u want)
    print(f"result:   {result: 0.16e}")
    print(f"error:    {eps:0.16e}")

    x = 0.0 #would give a problem if used for sin
    expected = 1.0
    result = exp(x)
    eps = (result - expected)/ expected
    print(f"testing exp({x:0.16e})")
    print(f"expected: {expected:0.16e}") #print with 16 digits of percision, 0 is the field width (fill change to fit the number, can specify if u want)
    print(f"result:   {result:0.16e}")
    print(f"error:    {eps:0.16e}")

    x = 8.5
    expected = np.exp(x)
    result = exp(x)
    eps = (result - expected)/ expected
    print(f"testing exp({x:0.16e})")
    print(f"expected: {expected:0.16e}") #print with 16 digits of percision, 0 is the field width (fill change to fit the number, can specify if u want)
    print(f"result:   {result:0.16e}")
    print(f"error:    {eps:0.16e}")

    x = -12.0
    expected = np.exp(x)
    result = exp(x)
    eps = (result - expected)/ expected
    print(f"testing exp({x:0.16e})")
    print(f"expected: {expected:0.16e}") #print with 16 digits of percision, 0 is the field width (fill change to fit the number, can specify if u want)
    print(f"result:   {result:0.16e}")
    print(f"error:    {eps:0.16e}")

if __name__ == "__main__":
    main()


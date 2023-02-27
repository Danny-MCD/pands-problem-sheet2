# Creating a function to find the square root of a float number
# Author: Daniel Mc Donagh



def square_root(n, l) :
    # N is the floating number and l is the tolerance in accuracy
    x = n
    count = 0
 
    while (1) :
        count += 1
 
        # Formula from netwons method of approximating square roots
        root = 0.5 * (x + (n / x))
 
        # Checking for closeness
        if (abs(root - x) < l) :
            break
 
        x = root
 
    return root
 
# Main programme
if __name__ == "__main__" :
 
    n = float(input("Please enter a positive number: "))
    l = 0.00001
 
    print(f"The square root of {n} is {square_root(n, l)}")
 

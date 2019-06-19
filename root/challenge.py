""" Twig Coding Challenge - Grouping Array Elements

The following function is used to divide an array into N 
sub-arrays. It uses a for loop to append a chunk of the array 
into another array. 

Includes a helper function to print the array returned.

Note: Avoided list comprehensions for easy understanding
"""

__author__ = 'Jesus Vera'
__project__ = 'Grouping Array Elements'

def groupArrayElements(a, n):
    # Check if n is type integer and positive
    if not  isinstance(n, int) or n < 0:
        print("The array must be divided by a positive integer value")
        exit()

    # This function returns the quotient and remainder from a division.
    # The quotient (q) will tell us the minimum number of values of the arrays
    # and the remainder (r) if we need to add more values to some arrays.
    q, r = divmod(len(a), n)

    array = []
    for i in range(n):
        # Function "min" will check for the minimum value between the remainder
        # and the current loop value (i) or next loop value (i + 1). 
        # With this we will make sure that regardless of the position 
        # we will always get an added remainder if there is still any.
        # It is also a simplied way to avoid using IFs and other conditionals.
        array.append(a[i * q + min(i, r):(i + 1) * q + min(i + 1, r)])

    return array

""" Helper function for printing the grouped array """
def helperPrintArray(a, n):
    print(list(groupArrayElements(a, n)))
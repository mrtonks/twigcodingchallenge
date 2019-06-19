""" Twig Coding Challenge - Grouping Array Elements

The groupArrayElements function is used to divide an array into N 
sub-arrays. It uses a for-loop to append chunks of the array 
into another array. 

Uses the "divmod" function to get the quotient (q) and remainder (r) 
of the division between the array length and the number of desired arrays N. 
The quotient will tell us the minimum number of values of the sub-arrays
and the remainder if we need to add more values to some sub-arrays.

The function "min" inside the for-loop will check for the minimum 
value between the remainder and the current loop value (i) or 
next loop value (i + 1). With this we will make sure that regardless 
of the position we will always get an added remainder if there is 
still any. It is also a simplied way to avoid using IFs and other 
conditionals.

Includes a helper function to print the array returned.

Note: Avoided list comprehensions for easy explanation and understanding.
"""

__author__ = 'Jesus Vera'
__project__ = 'Grouping Array Elements'

""" Function for diving and array into N arrays """
def groupArrayElements(a, n):
    # Check if n is type integer and positive
    if not  isinstance(n, int) or n < 0:
        print("The array must be divided by a positive integer value")
        exit()

    # This function returns the quotient and remainder from diving
    # the array length by N
    q, r = divmod(len(a), n)

    array = []
    for i in range(n):
        # Create a sub-array from the original array using the previously
        # obtained q and r and a "min" function. The "min" function will 
        # let us know if we have a remainder to add to that sub-array
        array.append(a[i * q + min(i, r):(i + 1) * q + min(i + 1, r)])

    return array

""" Helper function for printing the grouped array """
def helperPrintArray(a, n):
    print(list(groupArrayElements(a, n)))
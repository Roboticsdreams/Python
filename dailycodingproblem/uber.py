import math

class Uber:
    """"
    Given an array of integers, return a new array such that each element at index i of the new array is the product of all the numbers in the original array except the one at i.
    For example, if our input was [1, 2, 3, 4, 5], the expected output would be [120, 60, 40, 30, 24].
    If our input was [3, 2, 1], the expected output would be [2, 3, 6].
    Follow-up: what if you can't use division?
    """

    def productArray(self, alist):
        prod = 1
        arr = []
        length = len(alist)
        for counter in range(0, length):
            prod *= alist[counter]
        for i in range(0, length):
            arr.append(int(prod* math.pow(alist[i],-1)))
        return arr

def ubermain():
    uber = Uber()
    print(uber.productArray([1, 2, 3, 4, 5]))
    return 1
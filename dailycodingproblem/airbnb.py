class Airbnb:
    """
    Given a list of integers, write a function that returns the largest sum of non-adjacent numbers. Numbers can be 0 or negative.
    For example,
    [2, 4, 6, 2, 5] should return 13, since we pick 2, 6, and 5.
    [5, 1, 1, 5] should return 10, since we pick 5 and 5.
    Follow-up: Can you do this in O(N) time and constant space?
    """

    def maxSum(self, list):
        prev_prev_sum = 0
        prev_sum = list[0]
        for i in range(len(list)):
            current_sum = prev_prev_sum + list[i]
            if prev_prev_sum > prev_sum:
                prev_prev_sum = prev_prev_sum
            else:
                prev_prev_sum = prev_sum
            prev_sum = current_sum

        if prev_prev_sum > prev_sum:
            return prev_prev_sum
        else:
            return prev_sum

def airbnbmain():
    air = Airbnb()
    print(air.maxSum([2, 4, 6, 2, 5]))
    return 1

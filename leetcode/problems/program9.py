class PalindromeNumber:
    """
    Palindrome Number [Easy]

    Given an integer x, return true if x is palindrome integer.
    An integer is a palindrome when it reads the same backward as forward.
    For example, 121 is a palindrome while 123 is not.

    Example 1:
    Input: x = 121
    Output: true
    Explanation: 121 reads as 121 from left to right and from right to left.

    Example 2:
    Input: x = -121
    Output: false
    Explanation: From left to right, it reads -121. From right to left, it becomes 121-. Therefore it is not a palindrome.

    Example 3:
    Input: x = 10
    Output: false
    Explanation: Reads 01 from right to left. Therefore it is not a palindrome.

    Constraints:
    ------------
    -231 <= x <= 231 - 1

    Follow up: Could you solve it without converting the integer to a string?
    """
    def isPalindrome(self, x: int) -> bool:
        originalstr = str(x)
        strlen = len(originalstr) - 1
        reversestr = ""
        for i in range(strlen, -1, -1):
            reversestr = reversestr + originalstr[i]

        if originalstr == reversestr:
            return True
        else:
            return False
def palindromenumber_main():
    p9 = PalindromeNumber()
    return p9.isPalindrome(121)
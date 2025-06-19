'''
Given an integer x, return true if x is a palindrome(Means: Read same left to right than right to left) and false otherwise.

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
'''
import tracemalloc

def isPalindrome(x):
    """
        :type x: int
        :rtype: bool
    """
    import sys
    # If negative it become impossible
    if x < 0:
        return False

    x= str(x)
    for i in range((len(x)//2)):
        if x[i] != x[(i)*(-1) - 1]:
            return False
    return True

x = -121
print(isPalindrome(x))

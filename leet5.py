'''
5. Longest Palindromic Substring

Given a string s, return the longest palindromic(reads same in reverse) substring in s.

Example 1:
Input: s = "babad"
Output: "bab"
Explanation: "aba" is also a valid answer.

Example 2:
Input: s = "cbbd"
Output: "bb"
Constraints:

1 <= s.length <= 1000
s consist of only digits and English letters.
'''

def longestPalindrome(s):
    """
    :type s: str
    :rtype: str
    """
    max_list = s[0]   # since s.length >= 1 that means 1
    curr_str = ''
    z = len(s)
    for x in range(z):
        for y in range(-1, -(z - x), -1):
            if s[x] == s[y]:
                    if s[x: z+y+1] == s[y:-z + x - 1:-1]:
                        curr_str = s[x: z+y+1]
                        if len(curr_str) >= len(max_list):
                            max_list = curr_str
                            break
    return max_list

s = "a"
print(longestPalindrome(s))
'''
14. Longest Common Prefix
Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".

Example 1:
Input: strs = ["flower","flow","flight"]
Output: "fl"

Example 2:
Input: strs = ["dog","racecar","car"]
Output: ""
Explanation: There is no common prefix among the input strings.
 

Constraints:
1 <= strs.length <= 200
0 <= strs[i].length <= 200
strs[i] consists of only lowercase English letters if it is non-empty.
'''
def longestCommonPrefix(strs):
    """
        :type strs: List[str]
        :rtype: str
    """
    answ = ''
    minstring = min(strs, key=len)
    for i in range(len(minstring)):
        for x in range(len(strs) - 1):
            if strs[x][i] != strs[x + 1][i]:
                if i != 0:
                    answ = minstring[:i]
                    return answ
                else:
                    return answ
    return minstring
                

strs = ["dog","racecar","car"]
print(longestCommonPrefix(strs))
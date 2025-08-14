class Solution:
    def generateParenthesis(self, n: int) -> list[str]:
        cach = []
        ans = "("
        backer(cach, ans, n)
        cach = list(set(cach))
        return cach
        

def backer(cache, ans , n):
    if (2*n) == len(ans):
        cache.append(ans)
        return True

    if ans.count("(") < n:
        ans2 = ans[:]
        ans2+="("
        backer(cache, ans2, n)
        if ans.count("(") > ans.count(")"):
            ans+=")"
            backer(cache, ans, n)
    
    if ans.count("(") == n:
        ans += ")"
        backer(cache, ans, n)


print(Solution().generateParenthesis(n=3))
class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        i, j = len(s) - 1, len(p) - 1
        return self.backtrack({}, s, p, i, j)

    def backtrack(self, cache, s, p, i, j): #cache will be global so substings can find easy access
        key = (i, j)
        if key in cache:
            return cache[key]

        #reached the start of s, means need no more pattern.
        if i == -1 and j == -1:
            cache[key] = True
            return True
        
        if i == -1 and p[j] == '*':
            k = j
            while k != -1 and p[k] == '*':
                k -= 2
            
            if k == -1:
                cache[key] = True
                return cache[key]
            
            cache[key] = False
            return cache[key]
        
        if i == -1 and p[j] != '*':
            cache[key] = False
            return cache[key]
        
        # reached the start of pattern so obviously false
        if i != -1 and j == -1:
            cache[key] = False
            return cache[key]
        
        if p[j] == '*':
            if self.backtrack(cache, s, p, i, j - 2): #in between now we see a "*". We try to ignore it to see if it works
                cache[key] = True
                return cache[key]
            
            if p[j - 1] == s[i] or p[j - 1] == '.': #we use "*" soi -= 1 but j stays
                if self.backtrack(cache, s, p, i - 1, j):
                    cache[key] = True
                    return cache[key]
        
        if p[j] == '.' or s[i] == p[j]: #simple if matches we go for the substring
            if self.backtrack(cache, s, p, i - 1, j - 1):
                cache[key] = True
                return cache[key]

        cache[key] = False
        return cache[key]


s = "aab"
p = "c*a*b"

sol = Solution()
print(sol.isMatch(s, p))
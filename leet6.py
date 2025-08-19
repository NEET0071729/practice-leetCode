class Solution:
    def convert(self, s: str, numRows: int) -> str:
        place = 0
        ans = ""
        edge = True
        if (numRows >= len(s)) or (numRows == 1):
            return s
        for row in range(numRows):
            place = row
            num = 0
            while (place - 2*row) < len(s):
                if (row == 0) or (row == (numRows - 1)):
                    edge = True
                else:
                    edge = False
                if place < len(s):
                    if edge:
                        ans += s[place]
                    else:
                        if place == row:
                            ans += s[place]
                        else:
                            ans += s[place - 2*row] + s[place] 
                else:
                    if  not (edge):
                        ans += s[place - 2*row]
                num += 1
                place = row + (2*numRows - 2) * num
        return ans

s = "AB"
numRows = 4
print(Solution().convert(s, numRows))
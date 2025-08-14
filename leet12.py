class Solution:
    def intToRoman(self, num: int) -> str:
        ans = ""
        num_list = numbreaker(num)
        while num_list:
            if num_list[0] == 0:
                num_list = num_list[1:]
                continue
            elif (str(num_list[0]))[0] not in ["4" , "9"]:
                ans = romanAdd(num_list[0]) + ans
                num_list.pop(0)
            else:
                ans = romanSub(num_list[0]) + ans
                num_list.pop(0)
        return ans



def romanAdd(num: int) -> str:
    value = [1, 1, 1, 5, 10, 10, 10, 50, 100, 100, 100, 500, 1000, 1000, 1000]
    symbol = {1: "I", 5: "V", 10: "X", 50: "L", 100: "C", 500: "D", 1000: "M"}
    ans = ""
    value = value[::-1]
    val = 0
    while num:
        if value[val] == num:
            ans += symbol[num] 
            return ans
        elif value[val] < num:
            ans += symbol[value[val]]
            num -= value[val]
            value.pop(val)
            val = -1
        val += 1

    return ans
    

def romanSub(num: int) -> str:
    value = [1, 5, 10, 50, 100, 500, 1000]
    symbol = {1: "I", 5: "V", 10: "X", 50: "L", 100: "C", 500: "D", 1000: "M"}
    val = 0
    ans = "" 
    while num:
        if value[val] == num:
            ans = symbol[num] + ans
            return ans
        elif value[val] > num:
            ans += symbol[value[val]]
            num = value[val] - num
            val = -1
        val += 1






def numbreaker(num: int) -> list[str]:
    num = str(num)
    num_list = []
    while num:
        num_list.append(int(num[-1]))
        num = num[:-1]
    for numin in range(len(num_list)):
        num_list[numin] = (num_list[numin]) * pow(10, numin)
    return num_list




num = 3749
print(Solution().intToRoman(num))
#print(romanSub(num))
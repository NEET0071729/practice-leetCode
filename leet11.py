class Solution:
    def maxArea(self, height: list[int]) -> int:
        maximum = 0
        left = 0
        right = len(height) - 1
        while left < right:
            if height[left] < height[right]:
                num = (right - left) * height[left]
                if num > maximum:
                    maximum = num
                left += 1
            else:
                num = (right - left) * height[right]
                if num > maximum:
                    maximum = num
                right -= 1
        return maximum
#         if len(height) == 1:
#             return 0
        
#         max = AreaTwoPoints(height)
#         a = self.maxArea(height[1:])
#         b = self.maxArea(height[:-1])

#         if (max >= a) and (max >= b):
#             return max
#         elif (a >= max) and (a >= b):
#             return a
#         else:
#             return b
        
# def AreaTwoPoints(height):
#     if height[0] <= height[-1]:
#         return ((len(height)-1) * height[0])
#     else:
#         return ((len(height)-1) * height[-1])


height = [1,8,6,2,5,4,8,3,7]
# height = [76,155,15,188,180,154,84,34,187,142,22,5,27,183,111,128,50,58,2,112,179,2,100,111,115,76,134,120,118,103,31,146,58,198,134,38,104,170,25,92,112,199,49,140,135,160,20,185,171,23,98,150,177,198,61,92,26,147,164,144,51,196,42,109,194,177,100,99,99,125,143,12,76,192,152,11,152,124,197,123,147,95,73,124,45,86,168,24,34,133,120,85,81,163,146,75,92,198,126,191]
print(Solution().maxArea(height))
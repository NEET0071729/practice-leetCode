'''
4. Median of Two Sorted Arrays
iven two sorted arrays nums1 and nums2 of size m and n respectively, return the median of the two sorted arrays.

The overall run time complexity should be O(log (m+n)).

Example 1:
Input: nums1 = [1,3], nums2 = [2]
Output: 2.00000
Explanation: merged array = [1,2,3] and median is 2.

Example 2:
Input: nums1 = [1,2], nums2 = [3,4]
Output: 2.50000
Explanation: merged array = [1,2,3,4] and median is (2 + 3) / 2 = 2.5.

'''

nums1 = []
nums2 = [2]

a = len(nums1)
b = len(nums2)

x = y = 0
dummy = []
i = True
if a > b:
    z = b
else:
    z = a

if b == 0 or a == 0:
    i = False
    if a > 0:
        dummy = nums1
    else:
        dummy = nums2
while i:
    if nums1[x] < nums2[y]:
        dummy.append(nums1[x])
        x += 1
    else:
        dummy.append(nums2[y])
        y += 1
    if x == len(nums1):
        dummy.extend(nums2[y:])
        i = False
    if y == len(nums2):
        dummy.extend(nums1[x:])
        i = False
print(dummy)
ans = 0


if (a + b) % 2.0 == 0:
    r = (a + b) // 2
    ans = (dummy[r] + dummy[r - 1])/ 2.0
else:
    r = (a + b - 1) // 2
    ans = dummy[r]

print(ans)
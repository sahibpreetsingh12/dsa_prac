

"""
Optimised sol - with O(n) time complexity

The idea is we will iterate through the list once and we will start with maxsum as list[0] and current sum as 0
update current sum after every iteration but if  current sum is less than zero we will 
mark current sum = 0 and we will update again.
This algorithm is called Kadane's algorithm - https://www.youtube.com/watch?v=5WZl3MMT0Eg

"""
class Solution:
    def maxSubArray(self, nums: list[int]) -> int:

        "start with maxsum as first elemnt of list and current sum as 0"
        maxsum = nums[0]
        cursum = 0
        " iterate through each elemnt of list"
        for i in nums:
            """if cursum is < 0 we will mark cursum as 0 
            (this basically means we are ignoring elemnts whose sum till now was 0)"""
            if cursum<0:
                cursum = 0
            cursum = cursum + i 
            "checking max from current sum and maxsum till now"
            maxsum = max(maxsum,cursum)
    
        return maxsum



sol = Solution()
sol.maxSubArray(nums=[-2,1,-3,4,-1,2,1,-5,4])
"""
Un-Optimal Solution

This solution is notoptimal because we have three for loops so O(n^3) time complexity and fails Memory case
and thats true too we have too because in this solution

we first found all the possibles sublists possible from nums(Original list) given.
once we found that we took sum of each sublist and put that in dictionary, sorted the dictionary
and then last element of ictionary because it was sorted we took that Value
class Solution:
    def maxSubArray(self, nums: list[int]) -> int:
        
        dict_max = {}
        lst = nums
        sublist = [lst[i:j] for i in range(len(lst)) for j in range(i + 1, len(lst) + 1)]
        for i in sublist:
            
            dict_max[str(i)] = sum(i)
        dict_max = {k: v for k, v in sorted(dict_max.items(), key=lambda item: item[1])}
        sum_dict_max = list(dict_max.values())[-1]
        return sum_dict_max

sol = Solution()
print(sol.maxSubArray(nums=[-64,78,56,10,-8,26,-18,47,-31,75,89,13,48,-19,-69,36,-39,55,-5,-4,-15,-37,-27,-8,-5,35,-51,83,21,-47,46,33,-91,-21,-57,0,81,1,-75,-50,-23,-86,39,-98,-29,69,38,32,24,-90,-95,86]))


"""
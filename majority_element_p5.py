"""
Given an array nums of size n, return the majority element.

The majority element is the element that appears more than ⌊n / 2⌋ times. 
You may assume that the majority element always exists in the array.

Example 1:

Input: nums = [3,2,3]
Output: 3
Example 2:

Input: nums = [2,2,1,1,1,2,2]
Output: 2

"""

"""
solution with O(n) time complexity

class Solution:
    def majorityElement(self, nums: list[int]) -> int:
        
        # create a set of unique numbers in the list
        set_nums = list(set(nums))

        #create a empty dictionary
        dict_num = {}

        #iterate once for each element in the list
        for i in nums:
            
            #if the elemnt exists in the array add 1
            if i in dict_num:
                dict_num[i] += 1
            #if the element is encountered just first time give it 1
            else:
                dict_num[i] = 1

        #sort the dictionary by value 
        sorted_dic = sorted(dict_num.items(), key=lambda x: x[1])
        
        #fetch the key for last elemnt (element that has highest frequency)
        return sorted_dic[-1][0]

"""

"""
O(nlogn) since sorting of array takes O(nlogn)

Intuition - The intuition behind this approach is that if an 
element occurs more than n/2 times in the array (where n is the size of the array), 
it will always occupy the middle position when the array is sorted. Therefore, 
we can sort the array and return the element at index n/2.

Solution-  https://shorturl.at/cdixY
"""

class Solution:
    def majorityElement(self, nums: list[int]) -> int:
        nums.sort()
        n = len(nums)
        return nums[n//2]
    
sol = Solution()
sol.majorityElement(nums = [3,2,3])
    
"""
Given an integer array of size n, find all elements that appear more than ⌊ n/3 ⌋ times.

Example 1:

Input: nums = [3,2,3]
Output: [3]
Example 2:

Input: nums = [1]
Output: [1]
Example 3:

Input: nums = [1,2]
Output: [1,2]

"""

"""
The below solution is O(n) now the challenge is we have to solve it in O(1) time complexity
"""
class Solution:
    def majorityElement(self, nums: list[int]) -> list[int]:
        ele = nums[0] #if just one elemnet in list

        #empty dictionary to keep frequency of each element
        dict_num = {}
        for i in nums:
            if i in dict_num:
                dict_num[i] += 1
            else:
                dict_num[i] = 1

        #sort the dictionary
        sorted_dic = sorted(dict_num.items(), key=lambda x: x[1])
        
        #final list
        final_ele=[]

        for i  in list(sorted_dic):
            #iterate through sorted dictioanry
            if list(i)[1]>len(nums)/3:
                #append only that elemnet which has frequency > len(list)/3
                final_ele.append(list(i)[0])
        if final_ele:
            return final_ele
        else:

            return ele

sol = Solution()
print(sol.majorityElement(nums = [3,2,3]))
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

"""
Next challenge is to solve in constant time complexity -> O(1)

Boyer-Moore Majority Vote Algorithm
The algorithm above is known as Boyer-Moore Majority Vote Algorithm.
The Boyer-Moore Majority Vote Algorithm is an efficient algorithm used to find the majority element (an element that appears more than half of the time) in a given array. 
This algorithm operates in linear time and requires O(1) additional space.

Here are the basic steps of the Boyer-Moore Majority Vote Algorithm:

  1. Candidate Element Selection: Choose the first element of the array as 
    the candidate element and initialize a counter.

  2. Element Counting: Traverse through the array. If the current element matches
        the candidate element, increment the counter. If they don't match, decrement 
        the counter.

  3. Check Counter: If the counter becomes zero, choose the current element as the 
        new candidate element and reset the counter to one.

  4. Final Candidate Verification: After these steps, verify if the selected candidate 
        is indeed the majority element.

By following these steps, the algorithm efficiently identifies the most frequently 
occurring element, if one exists, in linear time O(n) in the worst case. 
This efficiency is achieved by carefully selecting candidate elements and comparing them 
against other elements.
"""
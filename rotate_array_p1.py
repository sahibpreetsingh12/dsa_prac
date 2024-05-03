"""
problem - https://leetcode.com/problems/rotate-array/
"""
"""
Given an integer array nums, rotate the array to the right by k steps, where k is non-negative.Example 1:

Input: nums = [1,2,3,4,5,6,7], k = 3
Output: [5,6,7,1,2,3,4]
Explanation:
rotate 1 steps to the right: [7,1,2,3,4,5,6]
rotate 2 steps to the right: [6,7,1,2,3,4,5]
rotate 3 steps to the right: [5,6,7,1,2,3,4]


Example 2:

Input: nums = [-1,-100,3,99], k = 2
Output: [3,99,-1,-100]
Explanation: 
rotate 1 steps to the right: [99,-1,-100,3]
rotate 2 steps to the right: [3,99,-1,-100]

Constraints:

    1. 1 <= nums.length <= 10^5
    2. -2^31 <= nums[i] <= 2^31 - 1
    3. 0 <= k <= 10^5
"""


class Solution:
    def rotate(self, nums: list[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        if k==0:
            """ if k is 0 do not return anything just return the array as it is"""
            return 
        
        elif len(nums)>k:
            """if list is bigger than k -> Go with slicing the list"""
            nums[:] = nums[-k : ] + nums[ : (len(nums)-k)]
            print(nums)

        else:
            """if list is smaller than k -> them remember k will repeat itself after len of the list
            that's why we used modulo operator"""
            k = k % len(nums)

            if k!=0:
                """
                if after modulo k comes out to be a number then use slicing
                """
                nums[:] = nums[-k : ] + nums[ : (len(nums)-k)]
                print(nums)
            elif k==0:
                """ if k comes out to be zero which can be the case when 
                len of list is equal to k . we dont have to rotate the list"""
                nums = nums
                print(nums)

sol = Solution()
sol.rotate(k=788,nums=[1,2,3,4,5,6,7])

"""

Intuition
    The problem requires rotating an array nums to the right by k steps. One intuitive approach is to understand that rotating by k steps is equivalent to moving the last k elements to the front of the array.

Approach
    1.Take modulo k with the length of the array to handle cases where k is larger than the length of the array, as rotating by the length of the array or its multiples will result in the same array.
    2.Slice the array by taking the last k elements and concatenate them with the remaining elements of the array.

Complexity
    Time complexity:
        Time complexity: O(n) wheren is the length of the array nums. Slicing and concatenation operations take O(n) time.

    Space complexity:
        Space complexity: O(n) for the space used by the sliced portion of the array


Solution that beats 94% users in python below

class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        
        a=k%len(nums)
        nums[:]=nums[-a:]+nums[:-a]
        print(nums)

        
sol = Solution()
sol.rotate(k=3,nums=[1,2,3,4,5,6,7])
"""
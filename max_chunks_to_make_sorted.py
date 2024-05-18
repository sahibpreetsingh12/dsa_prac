"""
You are given an integer array arr of length n that represents 
a permutation of the integers in the range [0, n - 1].

We split arr into some number of chunks (i.e., partitions), and individually sort each chunk. After concatenating them, the result should equal the sorted array.

Return the largest number of chunks we can make to sort the array.

 

Example 1:

Input: arr = [4,3,2,1,0]
Output: 1
Explanation:
Splitting into two or more chunks will not return the required result.
For example, splitting into [4, 3], [2, 1, 0] will result in [3, 4, 0, 1, 2], which isn't sorted.
Example 2:

Input: arr = [1,0,2,3,4]
Output: 4
Explanation:

We can split into two chunks, such as [1, 0], [2, 3, 4].
However, splitting into [1, 0], [2], [3], [4] is the highest number of chunks possible.

"""


"""
Remember  -  array of length n can only elemnts from 0 to n-1

"""

"""
Youtube - https://www.youtube.com/watch?v=qArjodCgZSg&t=284s
"""
class Solution:
    def maxChunksToSorted(self, arr: list[int]) -> int:
        """
        If the array is already sorted
        """
        max_so_far = arr[0]
    
        count = 0
        
        for i in range(len(arr)):
            if max_so_far<arr[i]:
                max_so_far = arr[i]
                
            if max_so_far == i:
                count+=1
                
        return count

        
"""
Given a positive integer n, find the smallest integer which has exactly the same 
digits existing in the integer n and is greater in value than n. If no such positive 
integer exists, return -1.

Note that the returned integer should fit in 32-bit integer, if there is a valid 
answer but it does not fit in 32-bit integer, return -1.

 

Example 1:

Input: n = 12
Output: 21
Example 2:

Input: n = 21
Output: -1


"""


from itertools import permutations
class Solution:
    def nextGreaterElement(self, n: int) -> int:
        nums = str(n)
        max_barrier = pow(2, 31) - 1
        # print(max_barrier)

        # if all elemnts are same in the number return -1
        if len(set(nums))==1: 
            return -1
        
        #if the one's element in the number is the highest in the entire number
        # #than return -1 because think of this carefully if your first digit itself is the bigeest
        # and last place digit (It can be any Ten's, Hundreds or any) is not same as one' place you
        # are already dealing with biggest number

        elif (list(nums)[0]==max(list(nums))) and (list(nums)[0]!=list(nums)[-1]): 
            return -1
        else:
            # Get all permutations of the string
            perms = permutations(nums)
            # Join each permutation to form strings
            """
            Have not taken for loop way because that just increases time complexity
            """
            combinations = map(''.join, perms)
            combinations = sorted([int(i) for i in combinations])

            ele = n
            for i in combinations:

                """
                if the element in list of combinations has 
                just exceeded the element (ele) and is les than Barrier (2^31) than return the elemnt
                """
                if i>ele:
                    ele = i
                    if ele<=max_barrier:
                        return ele
                    else:
                        return -1
             

sol = Solution()
print(sol.nextGreaterElement(101))
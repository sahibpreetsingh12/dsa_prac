from itertools import permutations
class Solution:
    def nextGreaterElement(self, n: int) -> int:
        nums = str(n)

        # if all elemnts are same in the number return -1
        if len(set(nums))==1: 
            return -1
        
        
        #if the one's element in the number is the highest in the entire number
        #than return -1
        elif list(nums)[0]==max(list(nums)) and (list(nums)[0]!=list(nums)[-1]): 
            return -1
        else:
            # Get all permutations of the string
            perms = permutations(nums)
            # Join each permutation to form strings
            combinations = map(''.join, perms)

            combinations = sorted([int(i) for i in combinations])

            ele = n
            for i in combinations:
                if i>ele:
                    ele = i
                    return ele
            # return list(combinations)
            # return int(''.join(sorted(list(nums),reverse=True)))
sol = Solution()
print(sol.nextGreaterElement(101))
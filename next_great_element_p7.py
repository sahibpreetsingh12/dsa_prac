class Solution:
    def nextGreaterElement(self, n: int) -> int:
        nums = str(n)

        # if all elemnts are same in the number return -1
        if len(set(nums))==1: 
            return -1
        
        #if the one's element in the number is the highest in the entire number
        #than return -1
        elif list(nums)[0]==max(list(nums)): 
            return -1
sol = Solution()
print(sol.nextGreaterElement(11))
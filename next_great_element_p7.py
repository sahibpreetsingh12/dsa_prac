class Solution:
    def nextGreaterElement(self, n: int) -> int:
        nums = str(n)

        if len(set(nums))==1:
            return -1
        elif list(nums)[0]==max(list(nums)):
            return -1
sol = Solution()
print(sol.nextGreaterElement(11))
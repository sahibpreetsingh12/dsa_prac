class Solution:
    def nextGreaterElement(self, n: int) -> int:
        nums = str(n)

        if len(set(nums))==1:
            return -1
        else:
            pass
sol = Solution()
print(sol.nextGreaterElement(11))
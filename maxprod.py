

class Solution:
    def maxProduct(self, nums: list[int]) -> int:

        res = max(nums)
        curmin,curmax = 1,1

        for i in nums:
            if i ==0:
                curmin,curmax = 1,1
                continue

            else:
                temp = curmin * i

                curmin = min(i,i * curmin,i * curmax)

                curmax = max(i,temp ,i * curmax)
                
                res = max(res,curmax)
        return res


sol = Solution()
sol.maxProduct(nums=[2,3,-2,4])
        
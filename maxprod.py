class Solution:
    def maxProduct(self, nums: list[int]) -> int:
        maxprod = nums[0]
        curprod = nums[0]
        for i in range(len(nums)-1):
            if curprod>=0 and nums[i+1]>0:
                curprod *= nums[i+1]
                # print(f'curprod here is ',curprod)
            else:
                curprod = nums[i+1]
            maxprod = max(maxprod,curprod)
            # print(f'Maxprod is ',maxprod)
        return maxprod

sol = Solution()
sol.maxProduct(nums=[2,3,-2,4])
        
"""so the problem is to find max subarray by product. Just like in Kadane algorithm
where we iterated over an array and found if the addition of next element causes the 
current sum to be less than zero we mark cursum = 0 but in this case
case is tricky 
case1 - Had we just all positive elemnsts in array - we can easily iterate over complete array and 
get final product as max product.

case 2 - If we have mix of positive and negative elements we will have to keep track of both 
min and max becasue imagine our both min and max till ith element are same now if we multiply 
them with negative number our max will come out from product of ith elemnt and curmin

and when ith element is zero we will continue and mark our curmin and curmax as 1,1

video - https://www.youtube.com/watch?v=lXVy6YWFcRM  

"""

class Solution:
    def maxProduct(self, nums: list[int]) -> int:

        #started with res as max of the array because in case our array is just [-1]
        #then max is the only elemnt in the array
        res = max(nums)

        #intialising bith min and max
        curmin,curmax = 1,1

        for i in nums:

            #if elemnt is zero continue
            if i ==0:
                curmin,curmax = 1,1
                continue

            else:
                # storing product of curmin and current elemnt (i)
                temp = curmin * i
                
                #checking current minimum which can i , i * current minimum , i * current maximum
                curmin = min(i,i * curmin,i * curmax)

                #checking current max which can i , i * current minimum , i * current maximum
                curmax = max(i,temp ,i * curmax)
                
                #finally stroing max which can be result or current max
                res = max(res,curmax)
        return res


sol = Solution()
sol.maxProduct(nums=[2,3,-2,4])
        
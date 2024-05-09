class Solution:
    def majorityElement(self, nums: list[int]) -> list[int]:
        ele = nums[0] #if just one elemnet in list

        
        dict_num = {}
        for i in nums:
            if i in dict_num:
                dict_num[i] += 1
            else:
                dict_num[i] = 1

        sorted_dic = sorted(dict_num.items(), key=lambda x: x[1])
        
        final_ele=[]
        for i  in list(sorted_dic):
            if list(i)[1]>len(nums)/3:
                final_ele.append(list(i)[0])
        return final_ele

sol = Solution()
print(sol.majorityElement(nums = [3,2,3]))
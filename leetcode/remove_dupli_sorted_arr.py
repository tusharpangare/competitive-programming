class Solution:
    def removeDuplicates(self, nums) :
        '''count=len(nums)
        for i in range(len(nums)-1):
            if nums.count(nums[i])>1:
                nums[i+1]="_"
                count-=1

        print(count, nums)'''
        out=[]
        for i in nums:
            if i not in out:
                out.append(i)
        nums=out[:]    
        print(nums)

        

        '''out = []
        for i in nums:
            if i not in out:
                out.append(i)
        nums.clear()
        nums.extend(out)
        print(nums)'''

obj=Solution()
obj.removeDuplicates([0,0,1,1,1,2,2,3,3,4])        

from operator import truediv


class Solution:
    def containsDuplicate(self, nums):

        
        '''out= list(set([x for x in nums if nums.count(x) > 1]))
        if len(out)<len(nums) and len(out)!=0:
            return True
        return False    '''
        
        '''out=[]
        for i in nums:
            if i in out:
                return True
            out.append(i)
        return False '''        

        '''
        while len(nums)>=1:
            if nums.count(nums[0])>1:
                return True
            nums=nums[1:]    
        return False    '''

        # for i in range(len(set(nums))):
        #     if nums.count(nums[i])>1:
        #         return True
        # else:
        #     return False        
        
        
obj=Solution()
print(obj.containsDuplicate([1,2,3,4]))     



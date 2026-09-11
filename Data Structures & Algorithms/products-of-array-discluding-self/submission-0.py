class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        output = []
        #output=[1,1,2,8]
        #output=[1,1,2,8]
        for i in range(len(nums)):
            if i == 0:
                prod = 1
            else:
                prod *= nums[i - 1]
            
            output.insert(i, prod)

        suffix = 1
        for j in range(len(nums) - 1, -1, -1):
            output[j] *= suffix
            suffix *= nums[j]
        return output

        '''
        prefix, suffix, output = [], [], []
        #i=2
        #prefix[0]=1
        #prefix[1]=1

        for i in range(len(nums)):
            if i == 0:
                prod = 1
            else:
                prod *= nums[i - 1]
            
            prefix.insert(i, prod)

        for i in range(len(nums) - 1, -1, -1):
            if i == len(nums) - 1:
                prod = 1
            else:
                prod *= nums[i + 1]
            #suffix=[48,24,6,1]
            suffix.insert(0, prod)

        for i in range(len(prefix)):
            output.insert(i, prefix[i] * suffix[i])

        return output
        '''
        '''
        result = []
        
        #i=0
        #num[i]=1
        #j=0,1,2,3
        #num[j]=1,2,4,6
        #prod_num=48
        '''
        '''
        for i in range(len(nums)):
            prod_num = 1
            for j in range(len(nums)):
                if i != j:
                    prod_num *= nums[j]
            
            result.append(prod_num)

        return result
        '''
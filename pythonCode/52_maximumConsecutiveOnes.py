class Solution():
    def findMaxConsecutiveOnes(self, nums):
        
        max_seq = 0  
        seq = 0       

        for num in nums:
            if num == 1:
                seq += 1
                if seq > max_seq:
                    max_seq = seq
            else:
                seq = 0  

        return max_seq


solution = Solution()
print(solution.findMaxConsecutiveOnes([0,1,0,0,1,1,1]))

#ans=3

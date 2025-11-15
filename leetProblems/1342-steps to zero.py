class Solution(object):
    def numberOfSteps(self, num):
        """
        :type num: int
        :rtype: int
        """
        store=0
        while num>0:
            if num%2==0:
                num=num/2
                 
            elif num%2 != 0:
                num=num-1
            store+=1
        
        print(store)

solution= Solution()
solution.numberOfSteps(8)

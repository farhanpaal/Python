class Solution(object):
    def runningSum(self, nums):
        result = []
        current_sum = 0

        for n in nums:
            current_sum += n
            result.append(current_sum)

        return result


solution = Solution()

 
print(solution.runningSum([1, 2, 3, 4]))       # [1, 3, 6, 10]
print(solution.runningSum([1, 1, 1, 1, 1]))    # [1, 2, 3, 4, 5]
print(solution.runningSum([3, 1, 2, 10, 1]))   # [3, 4, 6, 16, 17]

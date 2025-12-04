#Write a Python function inside a class Solution named removeElement that removes all occurrences of a given value val from the list nums.
#Modify the list in-place and return the number of elements not equal to val.

class Solution:
    def removeElement(self, nums: list[int], val: int) -> int:
        k = 0  # pointer for next valid position

        for i in range(len(nums)):
            if nums[i] != val:
                nums[k] = nums[i]
                k += 1
        
        return k
solution= Solution()
print(solution.removeElement(nums=[1, 2, 6,3, 4], val=4))

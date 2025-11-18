class Solution(object):
    def duplicateZeros(self, arr):
        """
        :type arr: List[int]
        :rtype: None Do not return anything, modify arr in-place instead.
        """
        length = len(arr)
        store = []
        
        for num in arr:
            if len(store) >= length:
                break
            if num == 0:
                store.append(0)
                if len(store) < length:
                    store.append(0)   
            else:
                store.append(num)
        
      
        for i in range(length):
            arr[i] = store[i]

class Solution(object):
    def isValid(self, s):
        a = []
        store=True


        for i in s:
            if (len(a) !=0 and i == ')' and a[-1]=='('):
                a=a[:-1]
            elif(len(a) !=0 and i == '}' and a[-1]=='{'):
                a=a[:-1]
            elif(len(a) !=0 and i == ']' and a[-1]=='['):
                a=a[:-1]
            else:
                a.append(i)
        if(len(a)!=0):
            store=False
        return store
solution = Solution()
s = "()[]{}"  
print(solution.isValid(s))

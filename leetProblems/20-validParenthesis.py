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



# Another way to solve this question using dictionary

class Solution2(object):
    def isValid(self, s):
        stack = []
        pairs = {')': '(', '}': '{', ']': '['}

        for char in s:
            if char in pairs.values():
                stack.append(char)
            elif char in pairs.keys():
                if not stack or stack[-1] != pairs[char]:
                    return False
                stack.pop()
            else:
                return False

        return len(stack) == 0

 
solution2 = Solution2()

 
s = input("Enter a string of brackets (e.g. '()[]{}'): ")
print("Valid:" if solution2.isValid(s) else "Invalid!")

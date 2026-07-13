class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack=[]
        for a in tokens:
            if a=="+":
                stack.append(stack.pop() + stack.pop())
            elif a=="-": 
                a=stack.pop()
                b=stack.pop()
                stack.append(b-a)    
            elif a=="*":
                stack.append(stack.pop() * stack.pop())
            elif a=="/":
                a=stack.pop()
                b=stack.pop()
                stack.append(int(b/a))
            else:
                stack.append(int(a ))
        return stack [0]           
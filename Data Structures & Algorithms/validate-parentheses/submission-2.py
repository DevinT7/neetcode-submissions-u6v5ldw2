class Solution:
    def isValid(self, s: str) -> bool:
        chars = {'(', ')', '{', '}', '[', ']'}
        stack = []
        for char in s:
            if char == '(' or char == '{' or char == '[':
                stack.append(char)
            else:
                if not stack:
                    return False
                x = stack.pop()
                if char == ')' and x != '(':
                    return False
                if char == ']' and x != '[':
                    return False
                if char == '}' and x != '{':
                    return False
        if stack:
            return False
        return True

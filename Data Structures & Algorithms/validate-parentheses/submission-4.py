class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for i in s:
            if i in "({[":
                stack.append(i)
            match i:
                case ")":
                    if not stack or stack[-1] != "(":
                        return False
                    stack.pop()
                case "}":
                    if not stack or stack[-1] != "{":
                        return False
                    stack.pop()
                case "]":
                    if not stack or stack[-1] != "[":
                        return False
                    stack.pop()
        return len(stack) == 0
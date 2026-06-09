class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        
        def dfs():
            token = tokens.pop()
            if token not in "+-*/":
                return int(token)
            right = dfs()
            left = dfs()
            match token:
                case "+":
                    return left + right
                case "-":
                    return left - right
                case "*":
                    return left * right
                case "/":
                    return int(left / right)

        return dfs()
            

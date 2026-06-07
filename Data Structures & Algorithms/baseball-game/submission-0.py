class Solution:
    def calPoints(self, operations: List[str]) -> int:
        score = []
        for op in operations:
            if op not in "+DC":
                score.append(int(op))
            match op:
                case "+":
                    res = score[-1] + score[-2]
                    score.append(res)
                case "D":
                    res = score[-1] * 2
                    score.append(res)
                case "C":
                    score.pop()
        return sum(score)
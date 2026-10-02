class Solution:
    def calPoints(self, operations: List[str]) -> int:
        result  = []
        total = 0
        for op in operations:
            if op == "+":
                total +=  result[-1] + result[-2]
                result.append(result[-1] + result[-2])
                
            elif op == "C":
                num = result.pop()
                total -= num
            elif op == "D":
                total += 2*result[-1]
                result.append(2*result[-1])
                
            else:
                total += int(op)
                result.append(int(op))
                
        
        return total
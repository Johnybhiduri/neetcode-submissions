class Solution:
    def climbStairs(self, n: int) -> int:
        # Creates fibonacci sequence 
        # Formula i-1 + i-2 =  i
        if n == 1:
            return 1
    
        elif n == 2:
            return 2
        
        else:
            outputs = {1:1,
            2:2
        }
            for i in range(3, n+1):
                outputs[i] =  (outputs[i-1]+outputs[i-2])

            return list(outputs.values())[-1]
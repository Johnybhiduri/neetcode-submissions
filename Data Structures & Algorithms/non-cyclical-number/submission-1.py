class Solution:
    def isHappy(self, n: int) -> bool:
        def get_squares_of_digit(num):
            sum_of_sq = 0
            while num != 0:
                last_digit = num % 10
                num = num // 10
                sum_of_sq += last_digit*last_digit
            
            return sum_of_sq

        seen = set()
        while True:
            if n == 1:
                return True
            
            if n in seen:
                return False
            
            seen.add(n)

            n = get_squares_of_digit(n)
        

            
            



class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        carry = 1
        for i in range(len(digits)-1, -1,-1):
            if (digits[i] + carry) <= 9:
                if carry:
                    digits[i] += carry
                    carry = 0
            else:
                digits[i] = 0
                carry = 1
        
        if carry:
            digits.insert(0,carry)

        return digits
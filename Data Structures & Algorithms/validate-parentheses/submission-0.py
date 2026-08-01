class Solution:
    def isValid(self, s: str) -> bool:
        stack  = []
        parentheses_map = {"]" : "[", "}" : "{", ")" : "("}

        for ch in s:
            if ch in parentheses_map.values():
                stack.append(ch)
            elif ch in parentheses_map.keys():
                if not stack or stack.pop() != parentheses_map[ch]:
                    return False
            
        
        return not stack
    

class Solution:
    def clearDigits(self, s: str) -> str:
        non_digits = deque()
        
        for char in s:
            if char.isdigit():
                if non_digits:  
                    non_digits.pop()
            else:
                non_digits.append(char)
        
        return ''.join(non_digits) 

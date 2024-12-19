class Solution(object):
    def isValid(self, s):
        \\\
        :type s: str
        :rtype: bool
        \\\
        stack = []
        i = 0
        for char in s:
            if char in '{([':
                stack.append(char)
            else:
                if len(stack) == 0:
                    return False
                popChar = stack.pop()
                if popChar == \{\ and char == \}\:
                    continue
                elif popChar == \(\ and char == \)\:
                    continue
                elif popChar == \[\ and  char == \]\:
                    continue
                else:
                    return False
        return len(stack) == 0

class Solution(object):
    def translator(self, digit):
        # Phone number mapping
        digit_map = {
            '2': ['a', 'b', 'c'],
            '3': ['d', 'e', 'f'],
            '4': ['g', 'h', 'i'],
            '5': ['j', 'k', 'l'],
            '6': ['m', 'n', 'o'],
            '7': ['p', 'q', 'r', 's'],
            '8': ['t', 'u', 'v'],
            '9': ['w', 'x', 'y', 'z']
        }
        return digit_map[digit]

    def letterCombinations(self, digits):
        \\\
        :type digits: str
        :rtype: List[str]
        \\\
        if not digits:
            return []
        res = []
        def dfs(comb, index):
            if  len(comb) >= len(digits):
                res.append(comb[:])
                return 
            for letter in self.translator(digits[index]):
                dfs(comb + letter , index + 1)

        dfs(\\, 0)
        return res
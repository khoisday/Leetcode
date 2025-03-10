class Solution:
    def countOfSubstrings(self, word: str, k: int) -> int:
        n = len(word)
        vowels = {"a": 0, "e": 0, "i": 0, "o": 0, "u": 0}
        consonants = 0
        i = 0
        j = 0
        result = 0
        leading_vowel = 0

        while j < n:
            if word[j] in vowels:
                vowels[word[j]] += 1
            else:
                consonants += 1
            
            while consonants > k:
                leading_vowel = 0
                if word[i] in vowels:
                    vowels[word[i]] -= 1
                else:
                    consonants -= 1
                i += 1
            
            if consonants == k:
                if all(v > 0 for v in vowels.values()):
                    while consonants == k and i <= j:
                        if word[i] in vowels and vowels[word[i]] > 1:
                            vowels[word[i]] -= 1
                        else:
                            break
                        i += 1
                        leading_vowel += 1
                    result += leading_vowel + 1
            j += 1
        
        return result
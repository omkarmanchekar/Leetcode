class Solution:

    def isVowels(self,letter):
        v = ['a','e','i','o','u']
        if letter in v:
            return 1
        return 0

    def maxVowels(self, s: str, k: int) -> int:

        char = list(s)
        substring = 0

        for i in range(k):
            substring += self.isVowels(char[i])

        res = substring

        for i in range(k,len(char)):
            substring = substring + self.isVowels(char[i]) - self.isVowels(char[i-k])
            res = max(res,substring)
        return res

        
class Solution(object):
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        if not s:
            return ""
        vowels = {'a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'}
        output = list(s)
        left = 0
        right = len(s) - 1

        while True:
            while left < right and s[left] not in vowels:
                left += 1

            while right > left and s[right] not in vowels:
                right -= 1

            if left < right:
                output[left], output[right] = s[right], s[left]
                left += 1
                right -= 1
            else:
                break

        return "".join(output)

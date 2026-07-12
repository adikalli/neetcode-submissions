class Solution:
    def isPalindrome(self, s: str) -> bool:
        ns = re.sub(r'[^a-zA-Z0-9]', '', s).lower()
        return ns[::-1]==ns
        
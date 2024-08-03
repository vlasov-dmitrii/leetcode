s = "A man, a plan, a canal: Panama"

def isPalindrome(s):
        def remove_non_alphabetical(s):
            return ''.join([char for char in s if char.isalnum()])
        
        s = s.replace(" ", "").lower()
        s = remove_non_alphabetical(s)
        print(s)
        left = 0
        right = len(s) - 1

        while left < right:
            if s[left] != s[right]:
                return False
            left += 1
            right -= 1
        
        return True

print(isPalindrome(s))
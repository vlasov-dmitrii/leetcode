

def lengthOfLongestSubstring(s):
    chars = set()
    l = 0
    substr = 0

    for r in range(len(s)):
        while s[r] in chars:
            chars.remove(s[l])
            l += 1
        chars.add(s[r])
        substr = max(substr, r - l + 1)

    return substr
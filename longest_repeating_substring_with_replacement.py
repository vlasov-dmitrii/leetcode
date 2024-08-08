k = 1
s = "AABABBA"

def characterReplacement(s, k):
    count = {}
    l = 0
    max_length = 0
    for r in range(len(s)):
        count[s[r]] = 1 + count.get(s[r], 0)
        max_length = max(max_length, count[s[r]])
        if r - l + 1 - max_length > k:
            count[s[l]] -= 1
            l += 1
    return (r - l + 1)

print(characterReplacement(s, k))
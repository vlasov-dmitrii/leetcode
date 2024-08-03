# sol 1

def isAnagram(s, t):
        if len(s) != len(t):
            return False
        s_list = list(s)
        for char in t:
            if char in s_list:
                s_list.remove(char)
            else:
                return False
        return True

# sol 2

def isAnagram(s, t):
    if len(s) != len(t):
        return False

    count_s = {}
    count_t = {}

    for i in range(len(s)):
        count_s[s[i]] = 1 + count_s.get(s[i], 0)
        count_t[t[i]] = 1 + count_t.get(t[i], 0)
    return count_s == count_t
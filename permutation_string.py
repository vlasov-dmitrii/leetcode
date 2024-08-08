
s1 = "abc"
s2 = "lecabee"

def checkInclusion(s1, s2):

    def count_chars(s):
        count = [0] * 26
        for char in s:
            count[ord(char) - ord('a')] += 1
        return count
    
    len_s1 = len(s1)
    len_s2 = len(s2)
    
    if len_s1 > len_s2:
        return False
    s1_count = count_chars(s1)
    window_count = count_chars(s2[:len_s1])
    if s1_count == window_count:
        return True

    for i in range(len_s1, len_s2):
        window_count[ord(s2[i]) - ord('a')] += 1
        window_count[ord(s2[i - len_s1]) - ord('a')] -= 1
        if s1_count == window_count:
            return True

    return False

print(checkInclusion(s1, s2))
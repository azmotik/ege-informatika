str_24 = 'abcbdbefg'

def f(s):
    max_len = left = right = 0
    arr = []

    while right < len(s):
        c = s[right]
        if c not in arr:
            arr.append(c)
            max_len = max(max_len, right - left + 1)
            right += 1
        else:
            while c in arr:
                arr.remove(s[left])
                left += 1
    return max_len

print(f(str_24))
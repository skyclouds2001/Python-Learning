def is_palindrome_number(x):
    s = str(x)
    flag = True
    for k in range(len(s)):
        if s[k] != s[len(s) - k - 1]:
            flag = False
    return flag

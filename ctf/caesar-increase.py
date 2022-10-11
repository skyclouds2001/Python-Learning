secret = 'ZpyLfxGmelDeftewJwFbwDGssZszbliileadaa'

for i in range(0, 26):
    flag = ''
    index = i

    for j in range(0, len(secret)):
        if ord('a') <= ord(secret[j]) <= ord('z'):
            flag += chr((ord(secret[j]) - ord('a') + i) % 26 + ord('a'))
        if ord('A') <= ord(secret[j]) <= ord('Z'):
            flag += chr((ord(secret[j]) - ord('A') + i) % 26 + ord('A'))
        index = index + 1

    print(flag)


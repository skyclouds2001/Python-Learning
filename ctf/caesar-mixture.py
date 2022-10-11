a = 'abcdefghijklmnopqrstuvwxyz'

secret = 'ZpyLfxGmelDeftewJwFbwDGssZszbliileadaa'

for j in range(0, 26):
    t = []
    l = len(secret)

    for i in range(0, l):
        n = a.find(secret[i])

        if n == -1:
            t.append(secret[i])
            continue

        if n % 2 == 0:
            t.append(a[(n + j) % 26])
        elif n % 2 != 0:
            t.append(a[(n + 26 - j) % 26])

    for i in range(0, l):
        print(t[i], end="")

    print('\n')

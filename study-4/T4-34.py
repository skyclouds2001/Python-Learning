s = input("Enter a hex character: ")
if 'A' <= s <= 'F':
    d = ord(s) - ord('A') + 10
if 'a' <= s <= 'f':
    d = ord(s) - ord('a') + 10
if '0' <= s <= '9':
    d = int(s)
print("The decimal value is", d)

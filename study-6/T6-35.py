import RandomCharacter

count = 0
for i in range(10000):
    c = RandomCharacter.get_random_upper_case_letter()
    if c == 'A':
        count += 1

print(count)

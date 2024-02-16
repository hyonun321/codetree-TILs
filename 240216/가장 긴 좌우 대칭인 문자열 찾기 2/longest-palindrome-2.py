a = input()
max_str = 0
for start in range(len(a)):
    for end in range(start,len(a)) :
        strings = a[start:end]
        back_strings = strings[::-1]
        if strings == back_strings :
            if max_str < len(strings):
                max_str = len(strings)
print(max_str)
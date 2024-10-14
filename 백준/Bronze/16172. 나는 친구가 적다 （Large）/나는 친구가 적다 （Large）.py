my_str = input()
keyword = input()
new_str = ''
for s in my_str:
    if s in '1234567890':
        continue
    new_str += s

print(int(keyword in new_str))
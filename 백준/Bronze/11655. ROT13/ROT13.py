s = input()
ans = ''
for i in s:
    if i.isupper():
        if chr(ord(i) + 13).isupper():
            ans += chr(ord(i) + 13)
        else:
            ans += chr(ord(i) - 13)
    elif i.islower():
        if chr(ord(i) + 13).islower():
            ans += chr(ord(i) + 13)
        else:
            ans += chr(ord(i) - 13)
    else:
        ans += i
print(ans)
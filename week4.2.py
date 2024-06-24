def convert(s):
    ch = list(s)
    for i in range(len(s)):
        if i == 0 and ch[i] != '':
            if ch[i] == 'a' or ch[i] == '2':
                ch[i] = chr(ord(ch[i]) + 2)
    return ''.join(ch)

print(convert("H"))

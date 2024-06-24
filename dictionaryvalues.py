def invert_content(disc):
    invert_disc = {v: k for k, v in disc.items()}
    return invert_disc

n = int(input("Enter number of values: "))
dic = {}
for i in range(n):
    key = input("Enter key: ")
    value = input("Enter value: ")
    dic[key] = value

print("Original dictionary:", dic)
print("After inversion:")
print(invert_content(dic))

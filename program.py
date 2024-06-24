def AND(a, b):
    if a and b:
        return True
    else:
        return False

# Test case
print("A=True | B=True | A AND B =", AND(True, True))
print("A=True | B=False | A AND B =", AND(True, False))
print("A=False | B=True | A AND B =", AND(False, True))
print("A=False | B=False | A AND B =", AND(False, False))

print()
 # OR OPERARIONS
def OR(a, b):
    if a or b:
        return True
    else:
        return False

# Test case
print("A=True | B=True | A AND B =", OR(True, True))
print("A=True | B=False | A AND B =", OR(True, False))
print("A=False | B=True | A AND B =", OR(False, True))
print("A=False | B=False | A AND B =", OR(False, False))

print()

# xor
def XOR(a, b):
    return a!=b

# Test case
print("A=True | B=True | A AND B =", XOR(True, True))
print("A=True | B=False | A AND B =", XOR(True, False))
print("A=False | B=True | A AND B =", XOR(False, True))
print("A=False | B=False | A AND B =", XOR(False, False))
import marshal
src='''
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

number = int(input("Enter a number: "))
print("Factorial of", number, "is:", factorial(number))

'''
code=compile(src,"src","exec")
fp=open("marshal2..py.txt","wb")
marshal.dump(code,fp)
fp.close()

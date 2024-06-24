
def remove_word(str,word):
    str2= str.replace(word,' ')
    return str2
str3=("hello good afternoon hi hello good")
print("Before remove")
print(str3)
str4=remove_word(str3,"hello")
print(str4)
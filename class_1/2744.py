text = input()

for i in range(len(text)):
    if text[i].isupper() == True:
        result = text[i].lower()
    else:
        result = text[i].upper()
    print(result, end="")
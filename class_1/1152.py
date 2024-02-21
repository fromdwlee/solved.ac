word = input()
list = word.split(" ")

while '' in list:
    list.remove('')

print(len(list))
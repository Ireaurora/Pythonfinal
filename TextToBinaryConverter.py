#this program is a text to binary converter
print(">>>>>>>>>>>>>Text to Binary Convertor<<<<<<<<<<<<")

text = input("Enter text to convert to binary")

print(''.join(format(ord(x), 'b') for x in text))

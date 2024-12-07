'''file = open("test.txt", "r")
print(file.readable())
file.close()


file = open("test.txt", "w")
print(file.writable())
file.close()


file = open("test.txt", "r+")
print(file.readable())
file.close()'''


file = open("test.txt", "r+")
#print(file.readable())
text = file.read()
print(text)
size = len(text)
print(size)
file.close()
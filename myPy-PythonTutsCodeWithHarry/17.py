# tell() and seek() in files

f=open("16.txt")
print(f.tell())   # tell function tells the current position of the pointer
print(f.readline())
print(f.tell())
print(f.readline())
print(f.tell())

f.seek(10)
print(f.readline())
f.seek(0)  # seek functions brings the pointer to the specified position
print(f.readline())

f.close()
from array import array

# Create an integer array
a = array('i', [10, 20, 30, 20, 40])

print("Original array:", a)


# 1. append()
a.append(50)
print("1. After append(50):", a)


# 2. buffer_info()
print("2. buffer_info():", a.buffer_info())


# 3. byteswap()
b = array('i', [1, 2, 3])
b.byteswap()
print("3. After byteswap():", b)


# 4. count()
print("4. Count of 20:", a.count(20))


# 5. extend()
a.extend([60, 70])
print("5. After extend([60, 70]):", a)


# 6. frombytes()
c = array('i')
data = array('i', [100, 200, 300]).tobytes()
c.frombytes(data)
print("6. After frombytes():", c)


# 7. fromfile()
# Create a binary file and write array data
file = open("numbers.bin", "wb")
temp = array('i', [1, 2, 3, 4])
temp.tofile(file)
file.close()

# Read data from the file
file = open("numbers.bin", "rb")
d = array('i')
d.fromfile(file, 4)
file.close()

print("7. After fromfile():", d)


# 8. fromlist()
e = array('i')
e.fromlist([10, 20, 30])
print("8. After fromlist():", e)


# 9. fromunicode()
# 'u' typecode is used for Unicode characters
f = array('u')
f.fromunicode("HELLO")
print("9. After fromunicode():", f)


# 10. index()
print("10. Index of 30:", a.index(30))


# 11. insert()
a.insert(1, 99)
print("11. After insert(1, 99):", a)


# 12. pop()
x = a.pop()
print("12. Popped element:", x)
print("    Array after pop():", a)


# 13. remove()
a.remove(20)
print("13. After remove(20):", a)


# 14. reverse()
a.reverse()
print("14. After reverse():", a)


# 15. tobytes()
byte_data = a.tobytes()
print("15. tobytes():", byte_data)


# 16. tofile()
file = open("output.bin", "wb")
a.tofile(file)
file.close()
print("16. tofile(): Data written to output.bin")


# 17. tolist()
list_data = a.tolist()
print("17. tolist():", list_data)


# 18. tounicode()
unicode_data = f.tounicode()
print("18. tounicode():", unicode_data)
#30.	String Rotation 
#	Check whether one string is a rotation of another. 
#	Example:
#	ABCD
#	CDAB
#Output: Yes
str1 = input("Enter first string: ")
str2 = input("Enter second string: ")

if len(str1) == len(str2) and str2 in (str1 + str1):
    print("Yes, the second string is a rotation of the first string.")
else:
    print("No, the second string is not a rotation of the first string.")

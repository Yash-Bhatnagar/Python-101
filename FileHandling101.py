"""
Opening, reading, closing a txt file
"""
print("\n")
#Method 1
file1 = open("D:\Yash\Practical\Learning Python\Files to access\TryFileText.txt")
print(file1.read(7))

print("Rest :-")
content = file1.read()
print(content+"\n")

file1.close()

#Method 2
print("\nTo read individual lines as a list:-")
file1 = open("D:\Yash\Practical\Learning Python\Files to access\TryFileText.txt")
print(file1.readlines())
file1.close()

#Method 3
print("\nTo read individual lines :-")
file1 = open("D:\Yash\Practical\Learning Python\Files to access\TryFileText.txt")
print("Line 1 : "+file1.readline())
print("Line 2 : "+file1.readline())
print("Line 3 : "+file1.readline())
file1.close()

#Method 3
print("\nTo read individual lines by for loop:-")
file1 = open("D:\Yash\Practical\Learning Python\Files to access\TryFileText.txt")
for line1 in file1:
    print(line1)
file1.close()

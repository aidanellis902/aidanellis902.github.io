#2
file2 = open("one.txt", "w")
for i in range(5):
    if i == 4:
        file2.write("hello")
    else:
        file2.write("hello"+"\n")
file2.close()
file3 = open("two.txt", "w")
for i in range(5):
    if i == 4:
        file3.write("hello")
    else:
        file3.write("hello"+"\n")
file3.close()
file4 = open("three.txt", "w")
for i in range (3):
    if i == 2:
        file4.write("hello")
    else:
        file4.write("hello"+"\n")
file4.close()
filename=input("What is the name of the file? ")

file=open(filename, "r")

lines = file.readlines()

if len(lines) <= 4:
    print("".join(lines))
    file.close()
else:
    print("The file has 5 or more lines.")
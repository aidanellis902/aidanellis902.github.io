#1
file1 = open("numbers.txt", "w")
for i in range(20):
    file1.write(str(i+1)+ "\n")
file1.close()
file1 = open("numbers.txt", "r")
print(file1.read())
file1.close()
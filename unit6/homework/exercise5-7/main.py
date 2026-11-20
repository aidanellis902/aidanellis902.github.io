#5
import random
amount=int(input("How many random numbers would you like to generate? "))
file5=open("random.txt", "w")
for i in range(amount):
    number=random.randint(1,500)
    file5.write(str(number)+"\n")
file5.close()
print("Random numbers have been written to the file")
#6
try:
    file5=open("random.txt", "r")
    total=0
    count=0
    print("Random Numbers:")
    for line in file5:
        number=int(line.strip())
        print(number)
        total += number
        count += 1
    file5.close()
    print("Total of the random numbers:", total)
    print("Number of random numbers:", count)
except IOError:
    print("Error: File not found or could not be opened.")
except ValueError:
    print("Error: Could not convert data to an integer.")
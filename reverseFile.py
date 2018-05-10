#Maia Reynolds
#5/10/18
#reverseFile.py - reverses lines in file

file=open(input("Enter a file: "))

lines=[]
for line in file:
    lines.append(line.strip())
lines.reverse()
print(lines)
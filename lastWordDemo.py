#Maia Reynolds
#5/10/18
#lastWordDemo.py - print the last word of each line of a file

file=open("fileDemo.py")

for line in file:
    words=line.split()
    print(line.strip("\n"))
    print(words)
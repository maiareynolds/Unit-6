#Maia Reynolds
#5/17/18
#warmup17 - prints all words that contain letters of last name

file=open("engmix.txt")

name=input("Enter your last name: ")

inword=0
for line in file:
    for letter in line:
        if letter in name:
            inword+=1
    if len(line)==inword:
        print(line)
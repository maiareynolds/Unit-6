#Maia Reynolds
#5/17/18
#longShort.py - prints longest and shortest word for each letter in alphabet

file=open("engmix.txt")

alphabet="abcdefghijklmnopqrstuvwxyz"


for letter in alphabet:
    dictionary=[]
    for line in file:
        line.split()
        if line[0]==letter:
            dictionary.append(line)
            maxi=""
            for line in dictionary:
                if len(line)>=len(maxi):
                    maxi=line
            print(maxi)
            for line in dictionary:
                if len(line)<=len(maxi):
                    maxi=line
            print(maxi)
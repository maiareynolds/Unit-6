#Maia Reynolds
#5/17/18
#longShort.py - prints longest and shortest word for each letter in alphabet

file=open("engmix.txt")

alphabet="abcdefghijklmnopqrstuvwxyz"

short=["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
longest=["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]

for line in file:
    line.split()
    if len(line)>=1 and len(line)>=len(longest[alphabet.index(line[0])]):
        longest[alphabet.index(line[0])]=line
print(longest)
#Maia Reynolds
#5/17/18
#longShort.py - prints longest and shortest word for each letter in alphabet

file=open("engmix.txt")

alphabet="abcdefghijklmnopqrstuvwxyz"

short=["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
longest=["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]

for line in file:
    line.split()
    letter=alphabet.index(line[0])
    if len(line)>=len(longest[letter]):
        longest[letter]=line
print(longest)
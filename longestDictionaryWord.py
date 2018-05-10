#Maia Reynolds
#5/10/18
#longestDictionaryWord.py - prints longest word in dictionary file

file=open("engmix.txt")

length=0
for line in file:
    if len(line)>length:
        length=len(line)
        word=line
print(word)
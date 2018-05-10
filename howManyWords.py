#Maia Reynolds
#5/10/18
#howManyWords.py - prints number of words for each number of letters

file=open("engmix.txt")

lengthlist=[]
for line in file:
    lengthlist.append(len(line.strip()))
num=1
while num<=22:
    print("There are",lengthlist.count(num),num,"letter words")
    num+=1
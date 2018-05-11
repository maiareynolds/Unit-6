#Maia Reynolds
#5/11/18
#warmup16.py - print out words beginning with first initial and end with last initial

file=open("engmix.txt")
numWords=0
for line in file:
    line=line.strip()
    if len(line)>1:
        if line[0] is "m" and line[-1] is "r":
            print(line)
            numWords+=1
print("There are",numWords,"words that start with your first initial and end with your last")
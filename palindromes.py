#Maia Reynolds
#5/11/18
#palindromes.py - prints plandromes

file=open("engmix.txt")

for line in file:
    if len(line)%2==0:
        if line[0:((len(line)/2)]==line[((len(line))/2)+1):]:
            print(line)
    else:
        if line[:((len(line)-1)/2)]==line[((len(line)+1)/2):]:
            print(line)
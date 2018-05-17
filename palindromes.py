#Maia Reynolds
#5/11/18
#palindromes.py - prints palindromes

file=open("engmix.txt")

for line in file:
    line=line.strip()
    reverse=""
    for ch in line:
        reverse=ch+reverse
    if reverse==line:
        print(line)
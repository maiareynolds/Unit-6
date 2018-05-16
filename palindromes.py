#Maia Reynolds
#5/11/18
#palindromes.py - prints palindromes

file=open("engmix.txt")

for line in file:
    line.strip()
    reverse=""
    for ch in line:
        reverse=ch+reverse
    reverse.reverse()
    if reverse==line:
        print(line)
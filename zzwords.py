#Maia Reynolds
#5/10/18
#zzwords.py - all words containing zz

file=open("engmix.txt")

for line in file:
    if "zz" in line:
        print(line.strip())

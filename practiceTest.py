#Maia Reynolds
#5/18/18
#practiceTest.py - test

file=open("engmix.txt")

for line in file:
    if line.count("c")==3 and line.count("p")==2:
        print(line)
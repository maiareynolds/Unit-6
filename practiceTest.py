#Maia Reynolds
#5/18/18
#practiceTest.py - test

file=open("engmix.txt")
"""
for line in file:#words with 3 cs and 2 ps
    if line.count("c")==3 and line.count("p")==2:
        print(line)

count=0
for line in file:#number of words beginning with r
    line.split()
    if len(line)>=1 and line[0]=="r":
        count+=1
print(count,"words start with the letter r")
"""
num=int(input("Enter a number: "))
words=[]
for line in file:
    if len(line)==num:
        words.append(line)
print(words[0])
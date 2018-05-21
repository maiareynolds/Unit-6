#Maia Reynolds
#5/20/18
#quiz6.py - Unit 6 Quiz, 5 Programs

file=open("engmix.txt")
"""
#1 - enter letter, prints all words from dictionary file with 4 of the letter in them
letter=input("Enter a letter: ")
for line in file:
    line.split()
    if line.count(letter)==4:
        print(line)

#2 - prints word from dictionary file where 1st, 5th, and 9th letters are the same
words=[]
for line in file:
    line.split()
    if len(line)>=9 and line[0]==line[4] and line[0]==line[8]:
        words.append(line)
print(words[0])
"""
#3 - enter number and letter, print all words from dictionary file that begin with letter and are the number's length
number=int(input("Enter a number: "))
letter=input("Enter a letter: ")
for line in file:
    line.split()
    if len(line)==number and line[0]==letter:
        print(line)
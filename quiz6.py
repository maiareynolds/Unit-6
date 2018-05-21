#Maia Reynolds
#5/20/18
#quiz6.py - Unit 6 Quiz, 5 Programs

file=open("engmix.txt")

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

#3 - enter number and letter, print all words from dictionary file that begin with letter and are the number's length
number=int(input("Enter a number: "))
letter=input("Enter a letter: ")
for line in file:
    line.split()
    if len(line)==number+1 and line[0]==letter:
        print(line)

#4 - finds 8000th word in dictionary file with more than 10 letters
longwords=[]
for line in file:#adds words with ten or more letters to longwords list
    line.strip()
    if len(line)>=10:
        longwords.append(line)
print(longwords[7999])#prints 8000th word in list

#5 - word in dictionary with greatest number of vowels (a,e,i,o,u)
vowels=0
word=""
for line in file:
    line.strip()
    lineVowels=line.count("a")+line.count("e")+line.count("i")+line.count("o")+line.count("u")#vowels in line
    if len(line)>=1 and lineVowels>vowels:
        word=line
        vowels=lineVowels
print(word)
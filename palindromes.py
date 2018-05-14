#Maia Reynolds
#5/11/18
#palindromes.py - prints palindromes

file=open("engmix.txt")

part1=0
part2=0
for line in file:
    line.strip()
    line=[line]
    if len(line)%2==0:
        part1=line[0][:((len(line))/2)+1]
        part2=line[0][(((len(line))/2)+1):]
        if part1==part2.reverse():
            print(line)
    else:
        part1=line[:((len(line)-1)/2)]
        part2=line[((len(line)+1)/2):]
        if part1==part2.reverse():
            print(line)
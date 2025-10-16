# /bin/python3

# Loops

mynumber = input("give me numbers you want in an array ")

print(mynumber.split(","))

splitted_mynumber = mynumber.split(",")

print(splitted_mynumber)

for n in range(0, len(splitted_mynumber)):
    splitted_mynumber[n] = int(splitted_mynumber[n])
    
print(splitted_mynumber)
all_splitted_mynumber = 0
for n in range(0, len(splitted_mynumber)):
    all_splitted_mynumber += int(splitted_mynumber[n])
    
print(all_splitted_mynumber,len(splitted_mynumber))
print(all_splitted_mynumber/len(splitted_mynumber))
print(round(all_splitted_mynumber/len(splitted_mynumber)))

# for i in range(7, 9):
#     print(i)


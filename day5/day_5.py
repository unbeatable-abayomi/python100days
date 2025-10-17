# /bin/python3

# Loops

mynumber = input("give me numbers you want in an array ")

print(mynumber.split(","))

splitted_mynumber = mynumber.split(",")

print(splitted_mynumber)

for n in range(0, len(splitted_mynumber)):
    splitted_mynumber[n] = int(splitted_mynumber[n])
    
print(splitted_mynumber , "after converting to int", type(splitted_mynumber[0]))

all_splitted_mynumber = 0
number_of_elements = 0
sum_of_elements = 0
container_var = 0
highest_value = splitted_mynumber[0]

print(number_of_elements, "first")
print(highest_value, "firstdd")

for x in splitted_mynumber:
    print(f"{x} is in the array")
    number_of_elements += 1
    sum_of_elements += x
    # container_var = x
    if x > highest_value:
      highest_value = x



print(f"{highest_value} is the highest")
print(number_of_elements, "second")
print(round(sum_of_elements/number_of_elements), "second method")

for n in range(0, len(splitted_mynumber)):
    all_splitted_mynumber += int(splitted_mynumber[n])
    
print(all_splitted_mynumber,len(splitted_mynumber))
print(all_splitted_mynumber/len(splitted_mynumber))
print(round(all_splitted_mynumber/len(splitted_mynumber)))

# for i in range(7, 9):
#     print(i)


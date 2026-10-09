number_list=[]
unique_numbers=[]
i=1
while i <= 10:
    num_input=int(input(f"Enter integer {i}: "))
    number_list.append(num_input)
    i+=1

for item in number_list:
    if item not in unique_numbers:
        unique_numbers.append(item)

sorted_list=[item for item in unique_numbers]
sorted_list.sort()

print(f"Original List: {number_list}")
print(f"Unique List: {unique_numbers}")
print(f"Sorted Unique List: {sorted_list}")
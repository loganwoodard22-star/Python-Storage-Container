friends = {"Alice": {"Bob", "Chris", "Emma"},
           "Bob": {"Alice", "Chris", "David"},
           "Chris": {"Alice", "Bob", "Emma", "Frank"},
           "Emma": {"Alice", "Chris"},
           "David": {"Bob", "Frank"}, 
           "Frank": {"Chris", "David"}}


print("Social Network Data")
print("-------------------")
for item, data in friends.items():
    print (f"{item}: {data}")




print("")

print("Pair with Most Mutual Friends")
print("-----------------------------")

combination_dict={}

for name1, data1 in friends.items():
    for name2, data2 in friends.items():
        friend_name_set=set()
        friend_name_set.add(name1)
        friend_name_set.add(name2)
        con_friend_name_set=tuple(friend_name_set)
        combinded_set=data1.intersection(data2)
        if combinded_set != set():
            if name1 != name2:
                combination_dict[con_friend_name_set]=combinded_set

len_mutal_friends=[]

for values in combination_dict.values():
    ind_len_mutal_friend=len(values)
    len_mutal_friends.append(ind_len_mutal_friend)

highest_mutal_friends=max(len_mutal_friends)


for names, items in combination_dict.items():
    if len(items) == highest_mutal_friends:
        print(f"{names[0]} and {names[1]}")
        print(f"Mutal Friends: {items}")
        print(f"Number of Mutal Friends: {len(items)}")
        break

print("")

print("Please enter two names to to see if they exist in the list")

print("")


names=[]
name1=input("Enter name 1 here: ")
name2=input("Enter name 2 here: ")

for name,data in friends.items():
    if name==name1 or name==name2:
        names.append(data)

print("")

print("Mutal Friends")
print("-------------")
if len(names) == 2:
    print(names[0].intersection(names[1]))
elif len(names) == 1:
    print("Both names do not appear on the list")
else:
    print("Neither name appears on the list")

print("")

print("Largest Friend Network")
print("----------------------")
all_length_set=[]
for data in friends.values():
    all_length_set.append(len(data))
    
highest_length_set=max(all_length_set)

for name, data in friends.items():
    if len(data)==highest_length_set:
        print(f"{name} has the largest friend network")
        print(f"Number of friends: {len(data)}")
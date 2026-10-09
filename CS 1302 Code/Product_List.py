product_list=[("Keyboard", 4, 25.50), ("Mouse", 10, 15.75), ("Monitor", 3, 120.00), ("Floppy Disks", 9, 45.00),("USB Cable", 15, 8.00), ("Webcam", 5, 45.00)]

inventory_value=[]

for item in product_list:
    in_inv_value=item[1]*item[2]
    inventory_value.append(in_inv_value)

inventory_value_total=sum(inventory_value)
inventory_value_highest=max(inventory_value)

counter=0

print("Product Inventory")
print("-----------------------------------------------------")
for item in product_list:
    print(f"Product: {item[0]}, Quantity: {item[1]:.2f}, Unit Price: {item[2]:.2f}, Inventory Value: {inventory_value[counter]:.2f}")
    if item[1]*item[2] == inventory_value_highest:
        inventory_value_name=item[0]
    counter+=1
print("")
print(f"Total inventory value: {inventory_value_total:.2f}")
print(f"Product with highest inventory value: {inventory_value_name}")
print(f"Highest inventory value: {inventory_value_highest:.2f}")
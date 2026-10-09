sales = { "East": {"Alice": 1200, "Bob": 1500, "Emma": 1350}, "West": {"Chris": 1800, "David": 1600, "Sophia": 1700}, "North": {"Liam": 1400, "Olivia": 1550, "Noah": 1480}}

total_region_sales={}
all_salepeople={}

print("Sales Data by Region")
print("--------------------")
for item, values in sales.items():
    running_total=0
    print(item)
    for name, number in values.items():
        print(f"    {name}: {number}")
        running_total+=number
        total_region_sales[item]=running_total
        all_salepeople[name]=number

print("")

print("Total Sales by Region")
print("---------------------")
for item, values in total_region_sales.items():
    print(f"{item}: {values}")

print("")

print("Top Salesperson in Each Region")
print("-------------------------------")
for item, values in sales.items():
    region_sales=[]
    highest_region_name=""
    for name, number in values.items():
        region_sales.append(number)
        highest_region_sales=max(region_sales)
        if number == highest_region_sales:
            highest_region_name=name
    print(f"{item}: {highest_region_name} with {highest_region_sales}")

print("")

print("Region with Highest Total Sales")
print("-------------------------------")
top_region=[]
for values in total_region_sales.values():
    top_region.append(values)

highest_top_region=max(top_region)

for items, value in total_region_sales.items():
    if value==highest_top_region:
        print(f"{items} with {value}")

print("")

salesperson_value=[]
print("Overall Top Salesperson")
print("-----------------------")
for number in all_salepeople.values():
    salesperson_value.append(number)

top_salesperson_value=max(salesperson_value)

for item, number in all_salepeople.items():
    if number==top_salesperson_value:
        print(f"{item} with {number}")
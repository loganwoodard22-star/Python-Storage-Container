employees = open(r"C:\Users\logan\Comp Sci\Assignments\employees.txt")

alice_sales=employees.readline()
alice_salesp=alice_sales.split(",")
alice_name=alice_salesp[0]
alice_salesp.remove("Alice")
alice_total=sum((int(i) for i in alice_salesp))
alice_average=alice_total/12

bob_sales=employees.readline()
bob_salesp=bob_sales.split(",")
bob_name=bob_salesp[0]
bob_salesp.remove("Bob")
bob_total=sum((int(i) for i in bob_salesp))
bob_average=bob_total/12

charlie_sales=employees.readline()
charlie_salesp=charlie_sales.split(",")
charlie_name=charlie_salesp[0]
charlie_salesp.remove("Charlie")
charlie_total=sum((int(i) for i in charlie_salesp))
charlie_average=charlie_total/12

diana_sales=employees.readline()
diana_salesp=diana_sales.split(",")
diana_name=diana_salesp[0]
diana_salesp.remove("Diana")
diana_total=sum((int(i) for i in diana_salesp))
diana_average=diana_total/12

edward_sales=employees.readline()
edward_salesp=edward_sales.split(",")
edward_name=edward_salesp[0]
edward_salesp.remove("Edward")
edward_total=sum((int(i) for i in edward_salesp))
edward_average=edward_total/12

top_total_name=""
all_emp_total=max([alice_total,bob_total,charlie_total,diana_total,edward_total])
if all_emp_total == alice_total:
    top_total_name=alice_name
if all_emp_total == bob_total:
    top_total_name=bob_name
if all_emp_total == charlie_total:
    top_total_name=charlie_name
if all_emp_total == diana_total:
    top_total_name=diana_name
if all_emp_total == edward_total:
    top_total_name=edward_name
all_emp_total=str(max([alice_total,bob_total,charlie_total,diana_total,edward_total]))

top_average_name=""
all_emp_average=max([alice_average,bob_average,charlie_average,diana_average,edward_average])
if all_emp_average == alice_average:
    top_average_name=alice_name
if all_emp_average == bob_average:
    top_average_name=bob_name
if all_emp_average == charlie_average:
    top_average_name=charlie_name
if all_emp_average == diana_average:
    top_average_name=diana_name
if all_emp_average == edward_average:
    top_average_name=edward_name
all_emp_average=str(max([alice_average,bob_average,charlie_average,diana_average,edward_average]))

most_total=open('top_annual.txt', "w")
most_total.write(top_total_name+": "+all_emp_total)

most_average=open('top_average.txt', "w")
most_average.write(top_average_name+": "+all_emp_average)

alice_total=str(alice_total)
alice_average=str(alice_average)
bob_total=str(bob_total)
bob_average=str(bob_average)
charlie_total=str(charlie_total)
charlie_average=str(charlie_average)
diana_total=str(diana_total)
diana_average=str(diana_average)
edward_total=str(edward_total)
edward_average=str(edward_average)

summary=open("summary.csv", "w")
summary.write(alice_name+" total: "+alice_total+" average: "+alice_average+"\n")
summary.write(bob_name+" total: "+bob_total+" average: "+ bob_average+"\n")
summary.write(charlie_name+" total: "+charlie_total+" average: "+charlie_average+"\n")
summary.write(diana_name+" total: "+diana_total+" average: "+diana_average+"\n")
summary.write(edward_name+" total: "+edward_total+" average: "+edward_average+"\n")
try:
    rain_file=open(r"C:\Users\logan\Comp Sci\Assignments CS 1302\rainfall.txt","r")
except FileNotFoundError:
    print("File type not found, please enter another file name")
    exit
else:
    

    master_list=[]
    all_rain_totals=[]
    all_rain_average=[]

    try:
        for line in rain_file:
            word=line.strip().split(",")
            counter=0
            rain_numbers=[]

            for number in word:
                if counter==0:
                    city_name=number
                    counter+=1
                else:
                    in_rain_num=float(number)
                    rain_numbers.append(in_rain_num)
            
            if len(rain_numbers) == 7:
                rain_total=sum(rain_numbers)
                all_rain_totals.append(rain_total)
                rain_average=rain_total / len(rain_numbers)
                all_rain_average.append(rain_average)
                master_list.append((city_name,rain_total,rain_average))
                rain_numbers.clear()
            else:
                print("The amount of items in the file are incorrect please enter a file that has the proper amount of items")
                exit
            
    except TypeError:
        print("Please enter a file that only has whole or decimal numbers for the data")
        exit

    highest_rain_total=max(all_rain_totals)
    lowest_rain_total=min(all_rain_totals)
    highest_rain_name=[]
    lowest_rain_name=[]

    for item in master_list:
        if item[1] == highest_rain_total:
            highest_rain_name.append(item[0])
            highest_rain_name.append(item[1])
        elif item[1] == lowest_rain_total:
            lowest_rain_name.append(item[0])
            lowest_rain_name.append(item[1])

    highest_rain_file=open("most_rain.txt","w")
    highest_rain_file.write(f"{highest_rain_name[0]} has the highest rainfall total with {highest_rain_name[1]:.2f} inches")

    lowest_rain_file=open("least_rain.txt","w")
    lowest_rain_file.write(f"{lowest_rain_name[0]} has the lowest rainfall total with {lowest_rain_name[1]:.2f} inches")

    summary=open("rainfall_summary.csv","w")
    for item in master_list:
        summary.write(f"Name of City: {item[0]} Total Rainfall: {item[1]:.2f} inches Average Rainfall: {item[2]:.2f} inches \n")
    print("Files created successfully")
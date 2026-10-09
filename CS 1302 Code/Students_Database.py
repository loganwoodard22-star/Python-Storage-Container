import sqlite3

conn = sqlite3.connect("students.db")
cursor=conn.cursor()

def descending_order():
    cursor.execute("SELECT StudentName,Major,GPA FROM Students ORDER BY GPA")
    desc_order_results=cursor.fetchall()
    desc_order_results.reverse()
    for items in desc_order_results:
        print(f"{items[0]} {items[1]} {items[2]}")

def ascending_order():
    cursor.execute("SELECT StudentName,Major,GPA FROM Students ORDER BY GPA")
    asce_order_results=cursor.fetchall()
    for items in asce_order_results:
        print(f"{items[0]} {items[1]} {items[2]}")

def sort_by_name():
    cursor.execute("SELECT StudentName,Major,GPA FROM Students ORDER BY StudentName")
    name_results=cursor.fetchall()
    for items in name_results:
        print(f"{items[0]} {items[1]} {items[2]}")


def sort_by_major():
    which_major=input("Please enter the major your would like to search by: ")
    cursor.execute(f'SELECT StudentName,Major,GPA FROM Students WHERE Major LIKE "{which_major}"')
    major_results=cursor.fetchall()
    for items in major_results:
        print(f"{items[0]} {items[1]} {items[2]}")

def average_gpa():
    cursor.execute("SELECT AVG(GPA) FROM Students")
    average_gpa_results=cursor.fetchall()
    for items in average_gpa_results:
        print(f"Average GPA: {items[0]}")

def highest_gpa():
    cursor.execute("SELECT MAX(GPA) FROM Students")
    highest_gpa_number=cursor.fetchall()
    for items in highest_gpa_number:
        single_highest_gpa=items[0]
    cursor.execute(f'SELECT StudentName,Major,GPA FROM Students WHERE GPA=={single_highest_gpa}')
    highest_gpa_result=cursor.fetchall()
    for item in highest_gpa_result:
        print(f"{item[0]} {item[1]} {item[2]}")


def lowest_gpa():
    cursor.execute("SELECT MIN(GPA) FROM Students")
    lowest_gpa_number=cursor.fetchall()
    for items in lowest_gpa_number:
        single_lowest_gpa=items[0]
    cursor.execute(f'SELECT StudentName,Major,GPA FROM Students WHERE GPA=={single_lowest_gpa}')
    lowest_gpa_result=cursor.fetchall()
    for item in lowest_gpa_result:
        print(f"{item[0]} {item[1]} {item[2]}")

is_program_running=True
try_again=True
while is_program_running==True:
    print("Please enter the number for the function you wish to access")
    print("1. Sort Database's GPAs by ascending order")
    print("2. Sort Database's GPAs by descending order")
    print("3. Sort Database by Student First Name")
    print("4. Filter Database by inputed Major")
    print("5. Find the average GPA of the Database")
    print("6. Find the highest GPA of the Database")
    print("7. Find the lowest GPA in the Database")
    print("8. Exit the Program")
    user_input=input("")
    if user_input == "1":
        ascending_order()
    elif user_input == "2":
        descending_order()
    elif user_input =="3":
        sort_by_name()
    elif user_input=="4":
        sort_by_major()
    elif user_input=="5":
        average_gpa()
    elif user_input=="6":
        highest_gpa()
    elif user_input=="7":
        lowest_gpa()
    elif user_input=="8":
        is_program_running=False
        break
    else:
        print("Invalid Number Entered")

    try_again_prompt=input("Would you like to preform another function (y/n): ")
    if try_again_prompt=="y":
        try_again=True
    else:
        try_again=False
        is_program_running=False
        break
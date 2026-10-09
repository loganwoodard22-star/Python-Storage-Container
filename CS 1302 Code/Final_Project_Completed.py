from tkinter import *
from tkinter import messagebox

def user_creation(first_name,last_name,username,password):
    user_id=1
    for item in user_list:
        if item.user_id==user_id:
            user_id+=1
    created_user=User(user_id,first_name,last_name,username,password)
    user_list.append(created_user)
    filemanger.user_creator(created_user.formatted_data())

def user_verifaction(username,password):
    can_enter=False
    for item in user_list:
        if username == item.username and password == item.password:
            can_enter=True
            change_logged_user(item)
            break
    return can_enter

def change_logged_user(user):
    global logged_user
    logged_user=user

def does_user_exist(username):
    users_exist=False
    for item in user_list:
        if item.username == username:
            users_exist=True
            break
    return users_exist

def add_income(category,amount,date):
    transaction_id=1
    type="Income"
    for item in transaction_list:
        if item.transaction_id == transaction_id:
            transaction_id+=1
    created_income=Transaction(transaction_id,type,category,amount,date)
    transaction_list.append(created_income)

def add_expense(category,amount,date):
    transaction_id=1
    type="Expense"
    for item in transaction_list:
        if item.transaction_id == transaction_id:
            transaction_id+=1
    created_expense=Transaction(transaction_id,type,category,amount,date)
    transaction_list.append(created_expense)

def create_budget(category,monthly_limit):
    created_budget=Budget(category,monthly_limit)
    budget_list.append(created_budget)

def does_category_exist(category):
    category_exist=False
    for item in budget_list:
        if category==item.category:
            category_exit=True
            break
    return category_exist

def clean_lists():
    transaction_list.clear()
    budget_list.clear()

def retrieve_user_files():
    global logged_user
    logged_user_id=logged_user.user_id
    filemanger.transaction_retrieval(logged_user_id)
    filemanger.budget_retrieval(logged_user_id)

def refresh_user_files():
    global logged_user
    logged_user_id=logged_user.user_id
    filemanger.transaction_refresh(logged_user_id)
    filemanger.budget_refresh(logged_user_id)

class User:
    def __init__(self,user_id,first_name,last_name,username,password):
        self.user_id=user_id
        self.first_name=first_name
        self.last_name=last_name
        self.username=username
        self.password=password

    def raw_data(self):
        return f"{self.user_id} {self.first_name} {self.last_name} {self.username} {self.password}"
    
    def formatted_data(self):
        return f"\n{self.user_id}\n{self.first_name}\n{self.last_name}\n{self.username}\n{self.password}"

class Transaction:
    def __init__(self,transaction_id,type,category,amount,date):
        self.transaction_id=transaction_id
        self.type=type
        self.category=category
        self.amount=amount
        self.date=date

    def raw_data(self):
        return f"Transaction ID: {self.transaction_id} Type: {self.type} Category: {self.category} Amount: {self.amount} Date: {self.date}"
    
    def formatted_data(self):
        return f"\n{self.transaction_id}\n{self.type}\n{self.category}\n{self.amount}\n{self.date}"

class Budget:
    def __init__(self,category,monthly_limit):
        self.category=category
        self.monthly_limit=monthly_limit

    def formatted_data(self):
        return f"\n{self.category}\n{self.monthly_limit}"

class FileManager:
    def start_up(self):
        try:
            user_file=open("user_list.txt","r")
            datastorage=[]
            for lines in user_file:
                clean_line=lines.rstrip("\n")
                if clean_line != "":
                    if clean_line == "-":
                        user_id=int(datastorage[0])
                        first_name=datastorage[1]
                        last_name=datastorage[2]
                        username=datastorage[3]
                        password=datastorage[4]
                        created_user=User(user_id,first_name,last_name,username,password)
                        user_list.append(created_user)
                        datastorage.clear()
                    else:
                        datastorage.append(clean_line)
            user_file.close()
        except FileNotFoundError:
            user_file=open("user_list.txt","x")
            user_file.close()

    def user_creator(self,user):
        user_file=open("user_list.txt","a")
        user_file.write(user)
        user_file.write("\n-")
        user_file.close()

    def transaction_retrieval(self,user):
        try:
            transaction_file=open(f"{user}_transactions.txt","r")
            datastorage=[]
            for line in transaction_file:
                clean_line=line.rstrip("\n")
                if clean_line != "":
                    if clean_line == "-":
                        transaction_id=int(datastorage[0])
                        type=datastorage[1]
                        category=datastorage[2]
                        amount=float(datastorage[3])
                        date=datastorage[4]
                        created_transaction=Transaction(transaction_id,type,category,amount,date)
                        transaction_list.append(created_transaction)
                        datastorage.clear()
                    else:
                        datastorage.append(clean_line)
            transaction_file.close()
        except FileNotFoundError:
            transaction_file=open(f"{user}_transactions.txt","x")
            transaction_file.close()

    def budget_retrieval(self,user):
        try:
            budget_file=open(f"{user}_budgets.txt","r")
            datastorage=[]
            for line in budget_file:
                clean_line=line.rstrip("\n")
                if clean_line != "":
                    if clean_line =="-":
                        category=datastorage[0]
                        month_limit=float(datastorage[1])
                        created_budget=Budget(category,month_limit)
                        budget_list.append(created_budget)
                        datastorage.clear()
                    else:
                        datastorage.append(clean_line)
        except FileNotFoundError:
            budget_file=open(f"{user}_budgets.txt","x")
            budget_file.close()

    def transaction_refresh(self,user):
        transaction_file=open(f"{user}_transactions.txt","w")
        transaction_file.write("")
        transaction_file.close()
        transaction_file=open(f"{user}_transactions.txt","a")
        for items in transaction_list:
            transaction_file.write(items.formatted_data())
            transaction_file.write("\n-")
        transaction_file.close()

    def budget_refresh(self,user):
        budget_file=open(f"{user}_budgets.txt","w")
        budget_file.write("")
        budget_file.close()
        budget_file=open(f"{user}_budgets.txt","a")
        for items in budget_list:
            budget_file.write(items.formatted_data())
            budget_file.write("\n-")
        budget_file.close()

class Login_Menu:
    def __init__(self):
        self.login_menu=Tk()
        self.login_menu.title("Login Page")
        self.login_menu_frame=Frame(self.login_menu)
        self.username_frame=Frame(self.login_menu_frame)
        self.password_frame=Frame(self.login_menu_frame)
        self.button_frame=Frame(self.login_menu_frame)

        self.username_label=Label(self.username_frame,text="Username: ")
        self.username_field=Entry(self.username_frame)

        self.password_label=Label(self.password_frame,text="Password")
        self.password_field=Entry(self.password_frame)

        self.login_menu_frame.pack(padx=200,pady=200)
        self.username_frame.pack(pady=5)
        self.username_label.pack(side="left",padx=5)
        self.username_field.pack(side="right")
        self.password_frame.pack(pady=5)
        self.password_label.pack(side="left",padx=5)
        self.password_field.pack(side="right")

        def loginprot():
            username=self.username_field.get()
            password=self.password_field.get()
            if username != "" and password != "":
                can_enter=user_verifaction(username,password)
                if can_enter == True:
                    self.login_menu.destroy()
                    clean_lists()
                    retrieve_user_files()
                    open_main_menu()
                else:
                    invalid_title="Invalid User Credentials"
                    invalid_message="Please enter a valid username and password"
                    messagebox.showinfo(invalid_title,invalid_message)
            else:
                field_title="Fields Empty Error"
                field_message="Please enter an input into both of thefields"
                messagebox.showinfo(field_title,field_message)
        self.login_button=Button(self.button_frame,text="Login",command=loginprot)
        def regiprot():
            self.login_menu.destroy()
            open_regi_menu()
        self.regi_button=Button(self.button_frame,text="Register",command=regiprot)
        self.exit_button=Button(self.button_frame,text="Exit",command=self.login_menu.destroy)
        
        self.button_frame.pack(pady=20)
        self.login_button.pack(side="left",padx=8)
        self.exit_button.pack(side="right",padx=8)
        self.regi_button.pack()

        mainloop()

class Regi_Menu:
    def __init__(self):
        self.regi_menu=Tk()
        self.regi_menu.title("Registration Menu")
        self.regi_menu_frame=Frame(self.regi_menu)
        self.first_name_frame=Frame(self.regi_menu_frame)
        self.last_name_frame=Frame(self.regi_menu_frame)
        self.username_frame=Frame(self.regi_menu_frame)
        self.password_frame=Frame(self.regi_menu_frame)
        self.button_frame=Frame(self.regi_menu_frame)

        self.first_name_label=Label(self.first_name_frame,text="First Name: ")
        self.first_name_field=Entry(self.first_name_frame)

        self.last_name_label=Label(self.last_name_frame,text="Last Name: ")
        self.last_name_field=Entry(self.last_name_frame)

        self.username_label=Label(self.username_frame,text="Username: ")
        self.username_field=Entry(self.username_frame)

        self.password_label=Label(self.password_frame,text="Password: ")
        self.password_field=Entry(self.password_frame)

        self.regi_menu_frame.pack(padx=200,pady=200)

        self.first_name_frame.pack(pady=5)
        self.first_name_label.pack(padx=5,side="left")
        self.first_name_field.pack(padx=8,side="right")

        self.last_name_frame.pack(pady=5)
        self.last_name_label.pack(padx=5,side="left")
        self.last_name_field.pack(padx=8,side="right")

        self.username_frame.pack(pady=5)
        self.username_label.pack(side="left",padx=8)
        self.username_field.pack(side="right")

        self.password_frame.pack(pady=5)
        self.password_label.pack(side="left",padx=8)
        self.password_field.pack(side="right")

        def regi_prot():
            first_name=self.first_name_field.get()
            last_name=self.last_name_field.get()
            username=self.username_field.get()
            password=self.password_field.get()
            if first_name != "" and last_name != "" and username != "" and password != "":
                user_exist=does_user_exist(username)
                if user_exist==False:
                    user_creation(first_name,last_name,username,password)

                else:
                    user_exist_title="User Exist Error"
                    user_exist_message="Please select another username"
                    messagebox.showinfo(user_exist_title,user_exist_message)
            else:
                field_title="Fields Empty Error"
                field_message="Please enter an input into both of the fields"
                messagebox.showinfo(field_title,field_message)

        self.regi_button=Button(self.button_frame,text="Register",command=regi_prot)

        def return_prot():
            self.regi_menu.destroy()
            open_login_menu()

        self.return_button=Button(self.button_frame,text="Return",command=return_prot)

        self.button_frame.pack(pady=5)
        self.regi_button.pack(padx=8)
        self.return_button.pack()

        mainloop()

class Main_Menu:
    def __init__(self):
        self.main_menu=Tk()
        self.main_menu.title("Main Menu")
        self.button_frame=Frame(self.main_menu)
        def add_income():
            self.main_menu.destroy()
            open_add_income()
        self.add_income_button=Button(self.button_frame,text="Add Income",command=add_income)
        def add_expense():
            self.main_menu.destroy()
            open_add_expense()
        self.add_expense_button=Button(self.button_frame,text="Add Expense",command=add_expense)
        def set_budget():
            self.main_menu.destroy()
            open_set_menu()
        self.set_budget_button=Button(self.button_frame,text="Set Budget",command=set_budget)
        def view_transactions():
            self.main_menu.destroy()
            open_view_transaction_menu()
        self.view_transactions_button=Button(self.button_frame,text="View Transaction History",command=view_transactions)
        def view_budget_report():
            self.main_menu.destroy()
            open_view_budget_report()
        self.view_budget_button=Button(self.button_frame,text="View Budget Report",command=view_budget_report)
        def edit_transactions():
            self.main_menu.destroy()
            open_edit_menu()
        self.edit_button=Button(self.button_frame,text="Edit Transaction",command=edit_transactions)
        def delete_transactions():
            self.main_menu.destroy()
            open_delete_menu()
        self.delete_button=Button(self.button_frame,text="Delete a Transaction",command=delete_transactions)
        def logout_prot():
            self.main_menu.destroy()
            refresh_user_files()
            clean_lists()
            open_login_menu()
        self.logout_button=Button(self.button_frame,text="Logout",command=logout_prot)

        self.button_frame.pack(pady=200,padx=200)
        self.add_income_button.pack(pady=5)
        self.add_expense_button.pack(pady=5)
        self.set_budget_button.pack(pady=5)
        self.view_transactions_button.pack(pady=5)
        self.view_budget_button.pack(pady=5)
        self.edit_button.pack(pady=5)
        self.delete_button.pack(pady=5)
        self.logout_button.pack(pady=5)

        mainloop()

class Add_Income_Menu:
    def __init__(self):
        self.add_menu=Tk()
        self.add_menu.title("Add Income")
        self.add_menu_frame=Frame(self.add_menu)

        self.category_frame=Frame(self.add_menu_frame)
        self.category_label=Label(self.category_frame,text="Source: ")
        self.category_field=Entry(self.category_frame)

        self.amount_frame=Frame(self.add_menu_frame)
        self.amount_label=Label(self.amount_frame,text="Amount: ")
        self.amount_field=Entry(self.amount_frame)

        self.date_frame=Frame(self.add_menu_frame)
        self.date_label=Label(self.date_frame,text="Date: ")
        self.date_field=Entry(self.date_frame)

        self.add_menu_frame.pack(pady=200,padx=200)
        self.category_frame.pack(pady=5)
        self.category_label.pack(side="left",padx=8)
        self.category_field.pack(side="right")
        self.amount_frame.pack(pady=5)
        self.amount_label.pack(side="left",padx=8)
        self.amount_field.pack(side="right")
        self.date_frame.pack(pady=5)
        self.date_label.pack(side="left",padx=8)
        self.date_field.pack(side="right")

        self.button_frame=Frame(self.add_menu_frame)
        def add_transaction():
            try:
                category=self.category_field.get()
                amount=float(self.amount_field.get())
                date=self.date_field.get()
                if category != "" and amount != "" and date != "":
                    add_income(category,amount,date)
                    refresh_user_files()
            except ValueError:
                incorrect_date_title="Incorrect Data Type"
                incorrect_date_message="Please enter a valid date type"
                messagebox.showinfo(incorrect_date_title,incorrect_date_message)

        self.add_button=Button(self.button_frame,text="Add",command=add_transaction)
        def return_prot():
            self.add_menu.destroy()
            open_main_menu()
        self.return_button=Button(self.button_frame,text="Return",command=return_prot)

        self.button_frame.pack(pady=5)
        self.add_button.pack(side="left",padx=8)
        self.return_button.pack(side="right")

        mainloop()
    
class Add_Expense_Menu:
    def __init__(self):
        self.add_menu=Tk()
        self.add_menu.title("Add Expense")
        self.add_menu_frame=Frame(self.add_menu)

        self.category_frame=Frame(self.add_menu_frame)
        self.category_label=Label(self.category_frame,text="Category: ")
        self.category_field=Entry(self.category_frame)

        self.amount_frame=Frame(self.add_menu_frame)
        self.amount_label=Label(self.amount_frame,text="Amount: ")
        self.amount_field=Entry(self.amount_frame)

        self.date_frame=Frame(self.add_menu_frame)
        self.date_label=Label(self.date_frame,text="Date: ")
        self.date_field=Entry(self.date_frame)

        self.add_menu_frame.pack(pady=200,padx=200)
        self.category_frame.pack(pady=5)
        self.category_label.pack(side="left",padx=8)
        self.category_field.pack(side="right")
        self.amount_frame.pack(pady=5)
        self.amount_label.pack(side="left",padx=8)
        self.amount_field.pack(side="right")
        self.date_frame.pack(pady=5)
        self.date_label.pack(side="left",padx=8)
        self.date_field.pack(side="right")

        self.button_frame=Frame(self.add_menu_frame)
        def add_transaction():
            try:
                category=self.category_field.get()
                amount=float(self.amount_field.get())
                date=self.date_field.get()
                if category != "" and amount != "" and date != "":
                    add_expense(category,amount,date)
                    refresh_user_files()
            except ValueError:
                incorrect_date_title="Incorrect Data Type"
                incorrect_date_message="Please enter a valid date type"
                messagebox.showinfo(incorrect_date_title,incorrect_date_message)

        self.add_button=Button(self.button_frame,text="Add",command=add_transaction)
        def return_prot():
            self.add_menu.destroy()
            open_main_menu()
        self.return_button=Button(self.button_frame,text="Return",command=return_prot)

        self.button_frame.pack(pady=5)
        self.add_button.pack(side="left",padx=8)
        self.return_button.pack(side="right")

        mainloop()

class Set_Budget_Menu:
    def __init__(self):
        self.set_menu=Tk()
        self.set_menu.title("Set_Budget")
        self.set_menu_frame=Frame(self.set_menu)

        self.category_frame=Frame(self.set_menu_frame)
        self.category_label=Label(self.category_frame,text="Category")
        self.category_field=Entry(self.category_frame)

        self.month_limit_frame=Frame(self.set_menu_frame)
        self.month_limit_label=Label(self.month_limit_frame,text="Monthly Limit: ")
        self.month_limit_field=Entry(self.month_limit_frame)

        def setprot():
            try:
                category=self.category_field.get()
                month_limit=float(self.month_limit_field.get())
                test_category=does_category_exist(category)
                if test_category == False:
                    create_budget(category,month_limit)
                    refresh_user_files()
                else:
                    category_exist_title="Category Already Exists"
                    category_exist_message="Please enter another category"
                    messagebox.showinfo(category_exist_title,category_exist_message)
            except ValueError:
                incorrect_date_title="Incorrect Data Type"
                incorrect_date_message="Please enter a valid date type"
                messagebox.showinfo(incorrect_date_title,incorrect_date_message)

        self.set_button=Button(self.set_menu_frame,text="Set",command=setprot)
        
        def returnprot():
            self.set_menu.destroy()
            open_main_menu()

        self.return_button=Button(self.set_menu_frame,text="Return",command=returnprot)

        self.set_menu_frame.pack(padx=200,pady=200)
        self.category_frame.pack(pady=5)
        self.category_label.pack(side="left",padx=8)
        self.category_field.pack(side="right")
        self.month_limit_frame.pack(pady=5)
        self.month_limit_label.pack(side="left",padx=8)
        self.month_limit_field.pack(side="right")
        self.set_button.pack(pady=5)
        self.return_button.pack(pady=5)

        mainloop()

class View_Transactions:
    def __init__(self):
        self.edit_menu=Tk()
        self.edit_menu.title("View Transactions")
        self.edit_menu_frame=Frame(self.edit_menu)

        self.selection_listbox_frame=Frame(self.edit_menu_frame)
        self.selection_listbox=Listbox(self.selection_listbox_frame,height=20,width=100,selectmode=SINGLE)

        self.edit_menu_frame.pack(padx=50,pady=50)
        self.selection_listbox_frame.pack()
        self.selection_listbox.pack()

        def refresh_prot():
            self.selection_listbox.delete(0,END)
            for item in transaction_list:
                self.selection_listbox.insert(END,item.raw_data())
        
        self.refresh_button=Button(self.selection_listbox_frame,text="Refresh",command=refresh_prot)
        self.refresh_button.pack(pady=5)

        def returnprot():
            self.edit_menu.destroy()
            open_main_menu()

        self.return_button=Button(self.selection_listbox_frame,text="Return",command=returnprot)
        self.return_button.pack(pady="5")

        mainloop()

class Budget_Report:
    def __init__(self):
        self.budget_menu=Tk()
        self.budget_menu.title("View Budget Report")
        self.budget_menu_frame=Frame(self.budget_menu)

        self.caluclate_frame=Frame(self.budget_menu_frame)

        self.income_frame=Frame(self.caluclate_frame)
        self.income_value=StringVar()
        self.income_title=Label(self.income_frame,text="Total Income: ")
        self.income_display=Label(self.income_frame,textvariable=self.income_value)

        self.expenses_frame=Frame(self.caluclate_frame)
        self.expenses_value=StringVar()
        self.expenses_title=Label(self.expenses_frame,text="Total Expenses: ")
        self.expenses_display=Label(self.expenses_frame,textvariable=self.expenses_value)

        self.remain_frame=Frame(self.caluclate_frame)
        self.remain_value=StringVar()
        self.remain_title=Label(self.remain_frame,text="Remaining Balance: ")
        self.remain_display=Label(self.remain_frame,textvariable=self.remain_value)

        self.budget_menu_frame.pack(padx=200,pady=10)
        self.caluclate_frame.pack(pady=8)
        self.income_frame.pack(pady=8)
        self.income_title.pack(side="left",padx=8)
        self.income_display.pack(side="right")
        self.expenses_frame.pack(pady=8)
        self.expenses_title.pack(side="left",padx=8)
        self.expenses_display.pack(side="right")
        self.remain_frame.pack(pady=8)
        self.remain_title.pack(side="left",padx=8)
        self.remain_display.pack(side="right")

        def calculate_amounts():
            total_income=0
            total_expense=0
            total_budget=0

            for item in transaction_list:
                if item.type == "Income":
                    total_income+=item.amount
                if item.type == "Expense":
                    total_expense+=item.amount

            for items in budget_list:
                total_budget+=items.monthly_limit

            remaining_balance=(total_budget+total_income)-total_expense

            self.income_value.set(total_income)
            self.expenses_value.set(total_expense)
            self.remain_value.set(remaining_balance)
        
        self.caluclate_button=Button(self.caluclate_frame,text="Calculate",command=calculate_amounts)
        self.caluclate_button.pack(pady=8)

        


        def returnprot():
            self.budget_menu.destroy()
            open_main_menu()

        self.return_button_frame=Frame(self.budget_menu_frame)
        self.return_button_frame.pack(pady=5)
        self.return_button=Button(self.return_button_frame,text="Return",command=returnprot)
        self.return_button.pack(pady=8)

        self.category_frame=Frame(self.budget_menu_frame)
        self.category_listbox=Listbox(self.category_frame,height=10,width=100)
        self.category_frame.pack(pady=5)
        self.category_listbox.pack(pady=8)

        def categoryrefreshprot():
            self.category_listbox.delete(0,END)
            categories={}
            for items in budget_list:
                categories[items.category]=items.monthly_limit
            
            for item in transaction_list:
                if item.type=="Expense":
                    if item.category in categories:
                        categories[item.category]-=item.amount

            for keys,value in categories.items():
                self.category_listbox.insert(END,f"Category: {keys}| Balance: {value}")

        self.refresh_button_frame=Frame(self.budget_menu_frame)
        self.refresh_button=Button(self.refresh_button_frame,text="Refresh",command=categoryrefreshprot)
        self.refresh_button_frame.pack()
        self.refresh_button.pack()

        mainloop()

class Edit_Transaction_Menu:
    def __init__(self):
        self.edit_menu=Tk()
        self.edit_menu.title("Edit Transaction")
        self.edit_menu_frame=Frame(self.edit_menu)

        self.selection_listbox_frame=Frame(self.edit_menu_frame)
        self.selection_listbox=Listbox(self.selection_listbox_frame,height=20,width=100,selectmode=SINGLE)

        self.edit_menu_frame.pack(padx=50,pady=50)
        self.selection_listbox_frame.pack()
        self.selection_listbox.pack()


        def refresh_prot():
            self.selection_listbox.delete(0,END)
            for item in transaction_list:
                self.selection_listbox.insert(END,item.raw_data())
        
        self.refresh_button=Button(self.selection_listbox_frame,text="Refresh",command=refresh_prot)
        self.refresh_button.pack(pady=5)
        
        self.fields_frame=Frame(self.edit_menu_frame)

        self.source_frame=Frame(self.fields_frame)
        self.source_label=Label(self.source_frame,text="Source/Category: ")
        self.source_field=Entry(self.source_frame)

        self.amount_frame=Frame(self.fields_frame)
        self.amount_label=Label(self.amount_frame,text="Amount: ")
        self.amount_field=Entry(self.amount_frame)

        self.date_frame=Frame(self.fields_frame)
        self.date_label=Label(self.date_frame,text="Date: ")
        self.date_field=Entry(self.date_frame)

        def editprot():
            try:
                source=self.source_field.get()
                amount=float(self.amount_field.get())
                date=self.date_field.get()
                if source != "" and amount != "" and date !="":
                    for items in self.selection_listbox.curselection():
                        selected_item=items
                    selected_item_info=self.selection_listbox.get(selected_item)
                    for item in transaction_list:
                        if item.raw_data()==selected_item_info:
                            item.category=source
                            item.amount=amount
                            item.date=date
                refresh_user_files()
            except ValueError:
                incorrect_date_title="Incorrect Data Type"
                incorrect_date_message="Please enter a valid date type"
                messagebox.showinfo(incorrect_date_title,incorrect_date_message)

        self.edit_button=Button(self.fields_frame,text="Edit",command=editprot)

        def returnprot():
            self.edit_menu.destroy()
            open_main_menu()

        self.return_button=Button(self.fields_frame,text="Return",command=returnprot)

        self.fields_frame.pack(pady=5)
        self.source_frame.pack(pady=5)
        self.source_label.pack(side="left",padx=8)
        self.source_field.pack(side="right")
        self.amount_frame.pack(pady=5)
        self.amount_label.pack(side="left",padx=8)
        self.amount_field.pack(side="right")
        self.date_frame.pack(pady=5)
        self.date_label.pack(side="left",padx=8)
        self.date_field.pack(side="right")
        self.edit_button.pack(pady=5)
        self.return_button.pack(pady=5)

        mainloop()

class Delete_Transaction_Menu:
    def __init__(self):
        self.edit_menu=Tk()
        self.edit_menu.title("Delete Transaction")
        self.edit_menu_frame=Frame(self.edit_menu)

        self.selection_listbox_frame=Frame(self.edit_menu_frame)
        self.selection_listbox=Listbox(self.selection_listbox_frame,height=20,width=100,selectmode=SINGLE)

        self.edit_menu_frame.pack(padx=50,pady=50)
        self.selection_listbox_frame.pack()
        self.selection_listbox.pack()

        def refresh_prot():
            self.selection_listbox.delete(0,END)
            for item in transaction_list:
                self.selection_listbox.insert(END,item.raw_data())
        
        self.refresh_button=Button(self.selection_listbox_frame,text="Refresh",command=refresh_prot)
        self.refresh_button.pack(pady=5)

        def delprot():
            for items in self.selection_listbox.curselection():
                selected_item=items
            selected_item_data=self.selection_listbox.get(selected_item)
            for item in transaction_list:
                if item.raw_data()==selected_item_data:
                    transaction_list.remove(item)
            refresh_user_files()

        self.delete_button=Button(self.selection_listbox_frame,text="Delete",command=delprot)

        def returnprot():
            self.edit_menu.destroy()
            open_main_menu()

        self.return_button=Button(self.selection_listbox_frame,text="Return",command=returnprot)

        self.delete_button.pack(pady=8)
        self.return_button.pack(pady=8)

        mainloop()

user_list=[]
transaction_list=[]
budget_list=[]
filemanger=FileManager()
logged_user=""

def open_login_menu():
    Login_Menu()

def open_regi_menu():
    Regi_Menu()

def open_main_menu():
    Main_Menu()

def open_add_income():
    Add_Income_Menu()

def open_add_expense():
    Add_Expense_Menu()

def open_set_menu():
    Set_Budget_Menu()

def open_view_transaction_menu():
    View_Transactions()

def open_view_budget_report():
    Budget_Report()

def open_edit_menu():
    Edit_Transaction_Menu()

def open_delete_menu():
    Delete_Transaction_Menu()

filemanger.start_up()
open_login_menu()
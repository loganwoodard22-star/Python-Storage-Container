from tkinter import *
from tkinter import messagebox

def user_verifaction(username,password):
    cred_correct=False
    for item in user_list:
        if item.username == username and item.password == password:
            cred_correct=True
            change_logged_user(item.username)
            break
    return cred_correct

def user_creation(username,password):
    created_user=User("user",username,password)
    user_list.append(created_user)

def verify_user_exist(username):
    user_exist=False
    for item in user_list:
        if item.username == username:
            user_exist=True
            break
    return user_exist

def movie_creation(title,show_time,ticket_price,seats):
    created_movie=Movie(title,show_time,ticket_price,seats)
    all_movies.append(created_movie)

def verify_movie_exist(title,show_time,ticket_price,seats):
    test_class=Movie(title,show_time,ticket_price,seats)
    movie_exist=False
    for items in all_movies:
        if test_class.movie_title==items.movie_title:
            movie_exist=True
            break
    return movie_exist

def change_logged_user(user):
    global logged_user
    logged_user=user

def initialize_dictonary():

    global logged_user
    if logged_user not in users_registered_movies:
        users_registered_movies[logged_user]=[]

def retrieve_logged_user():
    global logged_user
    return logged_user

class Movie:
    def __init__ (self, movie_title,show_time,ticket_price,seats):
        self.movie_title=movie_title
        self.show_time=show_time
        self.ticket_price=ticket_price
        self.seats=seats

    def display_info(self):
        return f"{self.movie_title}|{self.show_time}|{self.ticket_price}|Seats: {self.seats}"

class User:
    def __init__(self,type,username,password):
        self.type=type
        self.username=username
        self.password=password

class Login_Menu:
    def __init__(self):
        self.login_window=Tk()
        self.login_window.title("Login Page")
        self.login_menu_frame=Frame(self.login_window)
        self.username_frame=Frame(self.login_menu_frame)
        self.username_label=Label(self.username_frame,text="Username: ")
        self.username_field=Entry(self.username_frame)
        self.password_frame=Frame(self.login_menu_frame)
        self.password_label=Label(self.password_frame,text="Password: ")
        self.password_field=Entry(self.password_frame)
        def login_prot():
            username=self.username_field.get()
            password=self.password_field.get()
            if username!="" and password != "":
                can_enter=user_verifaction(username,password)
                if can_enter==True:
                    self.login_window.destroy()
                    initialize_dictonary()
                    open_main_menu(username)
                    
                else:
                    invalid_title="Invalid User Credentials"
                    invalid_message="Please enter a valid username and password"
                    messagebox.showinfo(invalid_title,invalid_message)
            else:
                field_title="Fields Empty Error"
                field_message="Please enter an input into both of thefields"
                messagebox.showinfo(field_title,field_message)
                
        def register_prot():
            self.login_window.destroy()
            open_regi_menu()

        self.button_frame=Frame(self.login_menu_frame)
        self.login_button= Button(self.button_frame,text="Login",command=login_prot)
        self.register_button= Button(self.button_frame,text="Register",command=register_prot)

        self.login_menu_frame.pack(padx=200,pady=200)
        self.username_frame.pack(pady=5)
        self.username_label.pack(side="left",padx=5)
        self.username_field.pack(side="right")
        self.password_frame.pack(pady=5)
        self.password_label.pack(side="left",padx=5)
        self.password_field.pack(side="right")
        self.button_frame.pack(pady=5)
        self.login_button.pack(side="left",padx=10)
        self.register_button.pack(side="right")
        mainloop()

class Main_Menu:
    def __init__(self,username):
        self.main_menu=Tk()
        self.main_menu.title("Movie Ticket Booking System")
        self.main_menu_title=Label(text=f"Hello, {username}")
        
        def logout_prot():
            self.main_menu.destroy()
            open_login_menu()

        def add_movie():
            try:
                title=self.title_field.get()
                show_time=self.show_time_field.get()
                price=float(self.price_field.get())
                avaliable_seats=int(self.avaliable_seats_field.get())
                does_movie_exist=verify_movie_exist(title,show_time,price,avaliable_seats)
                if title != "" and show_time != "" and price != "" and avaliable_seats != "":
                    if does_movie_exist==False:
                        movie_creation(title,show_time,price,avaliable_seats)
                    else:
                        movie_exist_title="Movie Exist"
                        movie_exist_message="Movie already exist, please enter another one"
                        messagebox.showinfo(movie_exist_title,movie_exist_message)
                else:
                    field_empty_title="Field Empty Error"
                    field_empty_message="Please enter a value in all of the fields"
                    messagebox.showinfo(field_empty_title,field_empty_message)
            except ValueError:
                incorrect_value_title="Incorrect Value"
                incorrect_value_message="Please enter the right type of data"
                messagebox.showinfo(incorrect_value_title,incorrect_value_message)

        #Top Most Frames
        self.top_frames=Frame(self.main_menu)
        #Left Side Gui
        self.left_side_frame=Frame(self.top_frames,relief="raised",border=2)
        self.top_left_side_frame=Frame(self.left_side_frame)

        self.add_movie=Label(self.top_left_side_frame,text="Add Movie")

        self.title_frame=Frame(self.top_left_side_frame)
        self.title=Label(self.title_frame,text="Title: ")
        self.title_field=Entry(self.title_frame)

        self.show_time_frame=Frame(self.top_left_side_frame)
        self.show_time=Label(self.show_time_frame,text="Show Time: ")
        self.show_time_field=Entry(self.show_time_frame)

        self.price_frame=Frame(self.top_left_side_frame)
        self.price=Label(self.price_frame,text="Price: ")
        self.price_field=Entry(self.price_frame)

        self.avaliable_seats_frame=Frame(self.top_left_side_frame)
        self.avaliable_seats=Label(self.avaliable_seats_frame,text="Avaliable Seats: ")
        self.avaliable_seats_field=Entry(self.avaliable_seats_frame)

        self.add_movie_button=Button(self.top_left_side_frame,text="Add Movie",command=add_movie)

        self.bottom_left_frame=Frame(self.left_side_frame)
        self.movie_list=Label(self.bottom_left_frame,text="Movie List")
        self.movie_list_listbox=Listbox(self.bottom_left_frame,height=10,width=75,selectmode=SINGLE)

        self.tickets_book_frame=Frame(self.bottom_left_frame)
        self.tickets_book_label=Label(self.tickets_book_frame,text="Tickets to Book: ")
        self.tickets_book_field=Entry(self.tickets_book_frame)
        
        

        #Right Side Gui
        self.right_side_frame=Frame(self.top_frames,relief="raised",border=2)
        self.right_side_title=Label(self.right_side_frame,text="My Bookings")
        self.bookings_listbox=Listbox(self.right_side_frame,height=10,width=50,selectmode=SINGLE)
        
        

        #Bottom Gui
        self.misc_buttons_frame=Frame(self.main_menu)
        self.logout_button=Button(self.misc_buttons_frame,text="Logout",command=logout_prot)
        self.exit_button=Button(self.misc_buttons_frame,text="Exit", command=self.main_menu.destroy)
        
        #Title Rendering
        self.main_menu_title.pack(padx=250,pady=20)

        #Left Side Rendering
        self.top_frames.pack()
        self.left_side_frame.pack(side="left",padx=5)

        self.top_left_side_frame.pack()
        self.add_movie.pack(padx=150,pady=5)
        
        self.title_frame.pack(pady=5)
        self.title.pack(padx=20,side="left")
        self.title_field.pack(side="right")

        self.show_time_frame.pack(pady=5)
        self.show_time.pack(padx=5,side="left")
        self.show_time_field.pack(padx=5,side="right")

        self.price_frame.pack(pady=5)
        self.price.pack(side="left",padx=14)
        self.price_field.pack(side="right")

        self.avaliable_seats_frame.pack(pady=5)
        self.avaliable_seats.pack(side="left")
        self.avaliable_seats_field.pack(side="right")
        self.add_movie_button.pack()

        self.bottom_left_frame.pack(pady=5)
        self.movie_list.pack(pady=5)
        self.movie_list_listbox.pack(padx=5,pady=5)

        self.tickets_book_frame.pack(pady=5)
        self.tickets_book_label.pack(side="left",padx=5)
        self.tickets_book_field.pack(side="right")
        def book_prot():
            try:
                number_of_tickets=int(self.tickets_book_field.get())
                for item in self.movie_list_listbox.curselection():
                    selected_booking=item
                selected_movie=self.movie_list_listbox.get(selected_booking)
                for items in all_movies:
                    if items.display_info() == selected_movie:
                        if number_of_tickets <= items.seats:
                            items.seats-=number_of_tickets
                            created_booking_title=items.movie_title
                            created_booking_show_time=items.show_time
                            created_booking_price=items.ticket_price*number_of_tickets
                            created_booking_seats=number_of_tickets
                            created_booking=Movie(created_booking_title,created_booking_show_time,created_booking_price,created_booking_seats)
                            for keys,values in users_registered_movies.items():
                                if keys==retrieve_logged_user():
                                    values.append(created_booking)
            except ValueError:
                incorrect_data_title="Incorrect Data"
                incorrect_data_message="Please enter the correct data type"
                messagebox.showinfo(incorrect_data_title,incorrect_data_message)
        self.tickets_book_button=Button(self.bottom_left_frame,text="Book Selected Movie",command=book_prot)
        self.tickets_book_button.pack()

        #Right Side Rendering
        self.right_side_frame.pack(side="right",padx=5)
        self.right_side_title.pack(pady=5)
        self.bookings_listbox.pack()
        def refresh_book_prot():
            self.bookings_listbox.delete(0,END)
            for keys,values in users_registered_movies.items():
                if keys == retrieve_logged_user():
                    for item in values:
                        self.bookings_listbox.insert(END,item.display_info())
        self.bookings_refresh_button=Button(self.right_side_frame,text="Refresh Bookings",command=refresh_book_prot)
        self.bookings_refresh_button.pack(pady=5)
        def cancel_book_prot():
            for items in self.bookings_listbox.curselection():
                selected_from_booking=items
            selected_booking=self.bookings_listbox.get(selected_from_booking)
            for keys,values in users_registered_movies.items():
                if keys==retrieve_logged_user():
                    for item in values:
                        if item.display_info()==selected_booking:
                            for k in all_movies:
                                if k.movie_title==item.movie_title:
                                    k.seats+=item.seats
                                    values.remove(item)
                                    self.bookings_listbox.delete(selected_from_booking)

        self.bookings_cancel_button=Button(self.right_side_frame,text="Cancel Selected Booking",command=cancel_book_prot)
        self.bookings_cancel_button.pack(pady=5)

        #Bottom Rendering
        def refresh_prot():
            self.movie_list_listbox.delete(0,END)
            for items in all_movies:
                self.movie_list_listbox.insert(END,items.display_info())
        self.refresh_button=Button(self.misc_buttons_frame,text="Refresh Movies",command=refresh_prot)
        self.misc_buttons_frame.pack(side="bottom",pady=20,padx=100)
        self.refresh_button.pack(side="left",padx=50)
        self.exit_button.pack(side="right",padx=50)
        self.logout_button.pack()
        
        mainloop()

class Registration_Menu:
    def __init__(self):
        self.regi_menu=Tk()
        self.regi_menu.title("Register New User")
        self.regi_menu_frame=Frame(self.regi_menu)

        self.username_frame=Frame(self.regi_menu_frame)
        self.username_label=Label(self.username_frame,text="Username: ")
        self.username_field=Entry(self.username_frame)

        self.password_frame=Frame(self.regi_menu_frame)
        self.password_label=Label(self.password_frame,text="Password: ")
        self.password_field=Entry(self.password_frame)

        def regi_prot():
            username=self.username_field.get()
            password=self.password_field.get()
            if username != "" and password !="":
                does_user_exist=verify_user_exist(username)
                if does_user_exist==False:
                    user_creation(username,password)
                else:
                    user_exists_title="Username Found"
                    user_exist_message="Please enter another username"
                    messagebox.showinfo(user_exists_title,user_exist_message)
            else:
                empty_field_title="Fields Empty Error"
                empty_field_message="Please enter an input in both of the fields"
                messagebox.showinfo(empty_field_title,empty_field_message)

        def return_prot():
            self.regi_menu.destroy()
            open_login_menu()

        self.button_frame=Frame(self.regi_menu_frame)
        self.regi_button=Button(self.button_frame,text="Register",command=regi_prot)
        self.return_button=Button(self.button_frame,text="Return",command=return_prot)

        self.regi_menu_frame.pack(padx=200,pady=200)
        self.username_frame.pack(pady=5)
        self.username_label.pack(padx=5,side="left")
        self.username_field.pack(side="right")
        self.password_frame.pack(pady=5)
        self.password_label.pack(side="left",padx=5)
        self.password_field.pack(side="right")
        self.button_frame.pack(pady=5)
        self.regi_button.pack(side="left",padx=5)
        self.return_button.pack(side="right")
        mainloop()


def open_login_menu():
    Login_Menu()

def open_main_menu(username):
    Main_Menu(username)

def open_regi_menu():
    Registration_Menu()

def_user=User("admin","admin123","movie123")

user_list=[def_user]
all_movies=[]
users_registered_movies={}
logged_user=""

open_login_menu()

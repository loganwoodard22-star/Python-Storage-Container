


class Admin:
    def __init__ (self, username, password):
        self.username=username
        self.password=password

class Owner:
    def __init__ (self, username, name, email, password, role):
        self.username=username
        self.name=name
        self.email=email
        self.password=password
        self.role=role

    def displayinfo(self):
        return f"Username: {self.username} Name: {self.name} Email: {self.email} Password: {self.password} Role: {self.role}"

class Tenant:
    def __init__ (self, username, name, email, password, role):
        self.username=username
        self.name=name
        self.email=email
        self.password=password
        self.role=role

    def displayinfo(self):
        return f"Username: {self.username} Name: {self.name} Email: {self.email} Password: {self.password} Role: {self.role}"

class Property:
    def __init__ (self, property_id, location, type, rent_price, avalibility,owner):
        self.property_id=property_id
        self.location=location
        self.type=type
        self.rent_price=rent_price
        self.avali=avalibility
        self.owner=owner

    def displayinfo(self):
        return f"Property ID: {self.property_id} \nLocation: {self.location} \nType: {self.type} \nRent Price: {self.rent_price} \nAvalibility: {self.avali}"
    
    def displayinfoadmin(self):
        return f"Property ID: {self.property_id} \n Owner={self.owner} \nLocation: {self.location} \nType: {self.type} \nRent Price: {self.rent_price} \nAvalibility: {self.avali}"

class TenantProperty:
    def __init__ (self, tenant_name, property_id, location, type, rent_price, avalibility, owner, rent_date):
        self.tenant_name=tenant_name
        self.property_id=property_id
        self.location=location
        self.type=type
        self.rent_price=rent_price
        self.avali=avalibility
        self.owner=owner
        self.rent_date=rent_date

    def displayinfo(self):
        return f"Property ID: {self.property_id} \nLocation: {self.location} \nType: {self.type} \nRent Price: {self.rent_price} \nAvalibility: {self.avali}"
    
    def displayinfoadmin(self):
        return f"Tenant Name: {self.tenant_name} \nProperty ID: {self.property_id} \nOwner: {self.owner} \nType: {self.type} \nLocation: {self.location} \nRent Price: {self.rent_price} \nStatus: {self.avali}"

def AdminMenu():
    print("")
    print("1. Create Account")
    print("2. Delete Account")
    print("3. View Reports")
    print("4. Logout")
    print("To navigate the menus, please enter the number related to the function you wish to enter")
    navi=int(input(""))
    
    if navi == 1:
        create_prot=True
        while create_prot==True:
            account_type=input("What kind of account would you like to make (Owner/Tenant): ")
            if account_type == "Owner":
                owner_entry=True
                while owner_entry==True:
                    owner_username=input("Please enter the username of the owner: ")
                    owner_name=input("Please enter the name of the owner: ")
                    owner_email=input("Please enter the email of the owner: ")
                    owner_password=input("Please enter the password of the owner: ")
                    owner_role="Owner"
                    owner_account=Owner(owner_username,owner_name,owner_email,owner_password,owner_role)
                    owner_list.append(owner_account)
                    print("Owner Account Created Successfully")
                    owner_retry=input("Would you like to enter another account (y/n): ")
                    if owner_retry == "y":
                        owner_entry=True
                    else:
                        owner_entry=False
                        create_prot=False
                        AdminMenu()
            elif account_type == "Tenant":
                tenant_entry=True
                while tenant_entry==True:
                    tenant_username=input("Please enter the username of the tenant: ")
                    tenant_name=input("Please enter the name of the tenant: ")
                    tenant_email=input("Please enter the email of the tenant: ")
                    tenant_password=input("Please enter the password of the tenant: ")
                    tenant_role="Tenant"
                    tenant_account=Tenant(tenant_username,tenant_name,tenant_email,tenant_password,tenant_role)
                    tenant_list.append(tenant_account)
                    print("Tenant Account Created Successfully")
                    tenant_retry=input("Would you like to enter another account (y/n): ")
                    if tenant_retry == "y":
                        tenant_entry=True
                    else:
                        tenant_entry=False
                        create_prot=False
                        AdminMenu()
            else:
                print("Please enter a valid user type")
    elif navi == 2:
        del_process=True
        while del_process==True:
            deletion_prot=input("Please enter the username of the user you would like to delete (Case Sensetive): ")
            for item in owner_list:
                if deletion_prot == item.username:
                    owner_list.remove(item)    
            for item in tenant_list:
                if deletion_prot == item.username:
                    tenant_list.remove(item)
            print("Account Deleted Successfully")
            del_retry=input("Would you like to delete another account (y/n): ")
            if del_retry == "y":
                del_process==True
            else:
                del_process==False
                AdminMenu()
    
    elif navi == 3:
        print("1. View User Report")
        print("2. View Property Report")
        print("3. Rental Report")
        report_prot=True
        while report_prot==True:
            sub_navi=int(input(""))
            if sub_navi == 1:
                for item in owner_list:
                    print(item.displayinfo())
                for item in tenant_list:
                    print(item.displayinfo())
            if sub_navi==2:
                for item in property_list:
                    print(item.displayinfoadmin())
            if sub_navi==3:
                for item in approved_rentals:
                    print(item.displayinfoadmin())
            report_prot=False
            AdminMenu()               
    
    elif navi == 4:
       MainMenu()
    
    else:
        print("Please enter a valid menu button")
        AdminMenu()

def OwnerMenu():
    print("")
    print("1. List Property")
    print("2. Remove Property")
    print("3. View My Properties")
    print("4. View Rental Requests")
    print("5. Approve/Reject Requests")
    print("6. Logout")
    print("To navigate the menus, please enter the number related to the function you wish to enter")
    navi=int(input(""))
    
    if navi == 1:
        list_prot=True
        while list_prot== True:
            property_id=int(input("Please enter the Property ID for the property"))
            location=input("Please enter the location of the property: ")
            type=input("Please enter the type of property: ")
            price=int(input("Please enter the price of the property: "))
            availability=input("Please enter if this property is avaliable or not: ")
            owner=logged_user
            listed_property=Property(property_id,location,type,price,availability,owner)
            property_list.append(listed_property)
            retry_list=input("Would you like to list another property (y/n): ")
            if retry_list == "y":
                list_prot=True
            else:
                list_prot=False
                OwnerMenu()
    
    elif navi == 2:
        remove_prot=True
        while remove_prot == True:
            id_of_prop=int(input("Please enter the id of the property you would like to delete: "))
            for item in property_list:
                if item.property_id == id_of_prop:
                    property_list.remove(item)
            retry_remove=input("Would you like to delete another property (y/n): ")
            if retry_remove == "y":
                remove_prot=True
            else:
                remove_prot=False
                OwnerMenu()
    
    elif navi == 3:
        view_prot=True
        while view_prot==True:
            for item in property_list:
                if item.owner == logged_user:
                    print(item.displayinfo())
            view_retry=input("Would you like to see the properties you own again (y/n): ")
            if view_retry == "y":
                view_prot==True
            else:
                view_prot==False
                OwnerMenu()
    
    elif navi == 4:
        request_prot=True
        while request_prot==True:
            for name, value in tenant_requests.items():
                print(f"{name} would like to rent the property with the id:{value}")
            request_retry=input("Would you like to view your requests again (y/n): ")
            if request_retry=="y":
                request_prot=True
            else:
                request_prot==False
                OwnerMenu()
    
    elif navi == 5:
        approve_prot=True
        while approve_prot==True:
            name_tenant=input("Please enter the name of the tenant requesting property: ")
            for name, value in tenant_requests.items():
                if name_tenant == name:
                    approve_message=input(f"Would you like to approve the request for {name} (y/n): ")
                    if approve_message == "y":
                        for item in property_list:
                            if item.property_id == value:
                                tenant_name=name
                                tenant_property_id=item.property_id
                                tenant_location=item.location
                                tenant_type=item.type
                                tenant_rent_price=item.rent_price
                                item.avali="Not Avalible"
                                tenant_avali=item.avali
                                tenant_owner=item.owner
                                tenant_rent_date=input("Please enter the date for which the property was approved: ")
                                tenant_result=TenantProperty(tenant_name,tenant_property_id,tenant_location,tenant_type,tenant_rent_price,tenant_avali, tenant_owner,tenant_rent_date)
                                approved_rentals.append(tenant_result)
                    else:
                        pass
            print("No more approvals left")
            approve_prot=False
            OwnerMenu()
    
    elif navi == 6:
        MainMenu()
    
    else:
        print("Please enter a valid menu number")
        OwnerMenu()

def TenantMenu():
    print("")
    print("1. View Avaliable Properties")
    print("2. Request Rental")
    print("3. View My Rentals")
    print("4. Cancel Request")
    print("5. Logout")
    print("To navigate the menus, please enter the number related to the function you wish to enter")
    navi=int(input(""))

    if navi == 1:
        view_prot=True
        while view_prot==True:
            for item in property_list:
                if item.avali == "Avaliable":
                    print(item.displayinfo())
            view_retry=input("Would you like to see what properties are avaliable again (y/n): ")
            if view_retry== "y":
                view_prot=True
            else:
                view_prot=False
                TenantMenu()

    elif navi == 2:
        request_prot=True
        while request_prot==True:
            request_id=int(input("Please enter the id of the property you wish to make a request for: "))
            for item in tenant_list:
                if item.username == logged_user:
                    name_tenant=item.name
            for item in property_list:
                    if item.property_id == request_id and item.avali=="Avaliable":
                        tenant_requests[name_tenant]=item.property_id
            request_retry=input("Would you like to make another request (y/n): ")
            if request_retry == "y":
                request_prot==True
            else:
                request_prot=False
                TenantMenu()
    
    elif navi == 3:
        view_rent_prot=True
        while view_rent_prot==True:
            for item in tenant_list:
                if item.username == logged_user:
                    name_tenant2=item.name
            for item in approved_rentals:
                if item.tenant_name == name_tenant2:
                    print(item.displayinfo())
            view_rent_retry=input("Would you like to see your properties again (y/n): ")
            if view_rent_retry == "y":
                view_rent_prot=True
            else:
                view_rent_prot=False
                TenantMenu()
    
    elif navi == 4:
        cancel_prot=True
        while cancel_prot==True:
            for item in tenant_list:
                if item.username == logged_user:
                    name_tenant3=item.name
            for name in tenant_requests:
                if name == name_tenant3:
                    del tenant_requests[name]
            print("Request Deleted Successfully")
            cancel_prot=False
            TenantMenu()
    
    elif navi == 5:
        MainMenu()
    
    else:
        print("Please enter a valid menu button")
        TenantMenu()
            
def LoginProt():
    global logged_user
    print("")
    username=input("Please enter your username: ")
    password=input("Please enter your password: ")
    can_enter=False
    
    while can_enter==False:
        if username == default_admin.username and password==default_admin.password:
            can_enter=True
            logged_user=username
            AdminMenu()
        for item in owner_list:
            if item.username==username and item.password==password:
                can_enter=True
                logged_user=username
                OwnerMenu()
        for item in tenant_list:
            if item.username==username and item.password==password:
                can_enter=True
                logged_user=username
                TenantMenu()
        
        if can_enter==False:
            print("Please enter a valid username and password")
            logged_user=""
            username=input("Please enter your username: ")
            password=input("Please enter your password: ")
    
def MainMenu():
    print("1. Login")
    print("2. Exit")
    print("To navigate the menus, please enter the number related to the function you wish to enter")
    main_menu_input=int(input(""))
    if main_menu_input==1:
        LoginProt()

    if main_menu_input==2:
        exit

default_admin=Admin("admin","admin123")

owner_list=[]
tenant_list=[]
property_list=[]
tenant_requests={}
approved_rentals=[]
logged_user=""

MainMenu()
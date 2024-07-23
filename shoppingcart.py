cart = []
logins = [{'UserName':'Anushya', 'Password':'anu@123'}]

def has_lowercase(password):
    return any(char.islower() for char in password)

def has_uppercase(password):
    return any(char.isupper() for char in password)

def has_digit(password):
    return any(char.isdigit() for char in password)

def has_special_character(password):
    special_characters = "!@#$%^&*(),.?\":{}|<>"
    return any(char in special_characters for char in password)

def check_password_strength(password):
    if len(password) < 8:
        return (False,"Weak: Password must be at least 8 characters long.")
    if not has_lowercase(password) or not has_uppercase(password):
        return (False,"Weak: Password must contain both uppercase and lowercase letters.")
    if not has_digit(password):
        return (False,"Weak: Password must contain at least one digit.")
    if not has_special_character(password):
        return (False,"Weak: Password must contain at least one special character.")
    return (True,"Strong: Password meets all criteria.")

def create_account():
    flag = 1
    uid = input("Enter the User Name: ")
    for i, d in enumerate(logins):
        if uid == d['UserName']:
            print("User Name already exist, Try again")
            create_account()
    else: 
        while (flag):
            pwd = input("Enter the Password: ")
            result,reason = check_password_strength(pwd)
            if result == False:
                print(reason)
                print("Try another Password")
            else:
                flag = 0
                logins.append({'UserName':uid, 'Password':pwd})
                print("Account Created Successfully")
    
def add_item():
    name = input("Enter item name: ")
    price = float(input("Enter item price:Rs. "))
    qty = int(input("Enter item Quantity: "))
    cart.append({'Item':name, 'Price':price,'Quantity':qty})
    print("Item added successfully into the Cart")
    
def view_cart():
    if len(cart) == 0:
        print("Cart is Empty")
    else:
        print("Items present in the Cart are: ")
        print("Name\tPrice\tQuantity")
        for i,d in enumerate(cart):
            print(F"{i+1}.{d['Item']}\t{d['Price']}\t{d['Quantity']}")

def calculate_total():
    if len(cart) == 0:
        print("Cart is Empty")
        print("Cannot Calculate the Amount")
    else:
        print("Items present in the Cart are: ")
        print("Name\tPrice\tQuantity\tTotal")
        sum = 0
        for i,d in enumerate(cart):
            t = d['Price'] * d['Quantity']
            sum = sum + t
            print(F"{i+1}.{d['Item']}\t{d['Price']}\t{d['Quantity']}\t{t}")
        gst = sum * 18 / 100
        net = sum + gst
        print(F"Total Amount = Rs.{sum}")
        print(F"GST = Rs.{gst}")
        print(F"Net Amount Payable = Rs.{net}")
        
def remove_item():
    if len(cart) == 0:
        print("Cart is Empty")
        print("Removal is not possible on an Empty Cart")
    else:
        view_cart()
        print()
        delete = int(input("Enter the Number to be deleted: "))
        if delete <=0 or delete > len(cart):
            print("Deletion is not possible")
        else:
            x = cart.pop(delete-1)
            print(F"Data - {x} deleted successfully")
        
def modify_Qty():
    if len(cart) == 0:
        print("Cart is Empty")
        print("No content to Modify")
    else:
        view_cart()
        print()
        index = int(input("Enter the Number that need to be Modified: "))
        qty = int(input("Enter the New Quantity: "))
        d = cart[index-1]
        d['Quantity'] = qty
        print("Quantity Modified Successfully")
    
while True:
    print("===== Shopping Cart =====")
    print("1. Create Your Shopping Account")
    print("2. Add Item to Cart")
    print("3. View Cart")
    print("4. Calculate Total")
    print("5. Remove Item from Cart")
    print("6. Modify the Quantity")
    print("7. Quit")
    opt = int(input("Select an option (1 to 7): "))
    
    if opt == 1:
        create_account()
    elif opt == 2:
        add_item()
    elif opt == 3:
        view_cart()
    elif opt == 4:
        calculate_total()
    elif opt == 5:
        remove_item()
    elif opt == 6:
        modify_Qty()
    elif opt == 7:
        print("Application is Closing")
        print("Thank You ! Visit again .... ")
        break
    else:
        print("Invalid Option entered. Try again")

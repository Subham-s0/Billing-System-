
import datetime

def welcome_():
    '''
     This Function displays a decorative banner or a  welcome message for the BRJ Furniture Management System.
     This function acceps no parameter.It doesnot return any value adn doesnot raise any exception
    '''
    print("_"*140)
    print("\n")
    print(" "*40+"-"*62)
    print(" "*40+"|"+" "*60+"|")
    print(" "*40+"|"+" "*24+"BRJ Furniture"+" "*23+"|")
    print(" "*40+"|"+" "*7+"Kamalpokhari, Kathmandu | Phone No: 9801010101"+" "*7+"|")
    print(" "*40+"|"+" "*60+"|")
    print(" "*40+"-"*62)
    print("\n")
    print("\n")
    print(" "*49+"Welcome to BRJ Furniture Management System!")
    print("_"*140)
    print("\n\n")

 
    
def display_furniture(stock):
    '''
    This function is used to display the stock availble in the furniture store.

    parameter:
    -stock(dictionary) :a dictionary containing stock information is passed in this parameter.

    return:
    this function doesnot return 
    
    '''
    print("\n")
    print("-_"*70)
    print("\n")
    print("-"*140)
    print("| Furniture ID |"+"\t\tManufacturor Name"+" "*19+"|"+"\t\tFurniture Item"+" "*6+"|"+"   Quantity"+" "*5+"|"+"    Amount"+" "*6+"|")
    print("_"*140+"\n")
    for value in stock.values():
        print("|   " + value[0] + " " * (11 - len(value[0])) + "|  " + value[1] + 
              " " * (50 - len(value[1]) ) + "|   " + value[2] + 
              " " * (28 - len(value[2]) )+ "|    " + value[3] + 
              " " * (12 - len(value[3]) )+ "|    " + value[4]+
              " " * (12 - len(value[4]) ) + "|  " )
        print("-"*140)

    print("\n\n")
def ensure_valid_name():
    '''
    This function is checks if the name entered by the user is valid or not. A valid name is defined as a non-empty string containing only
    alphabetic characters. The loop works until the user enter th valid name .

    parameter:
    It has no Parameters

    return:
    this function return the valid name  
    
    '''
    
    loop=True
    while loop==True:
        name=input("Enter you Name:").strip()
        if len(name)>0 and name.isalpha()==True:
            loop=False
            return name
        else:
            print("Please enter valid name !.")

def ensure_valid_number():
    '''
    This function is checks if the number entered by the user is valid or not. A valid number is defined as a non-empty string containing only
    numerical characters. The loop works until the user enter th valid number .

    parameter:
    It has no Parameters

    return:
    this function return the valid number  
    
    '''
    
    loop=True
    while loop==True:
        number = input("Enter your Phone number : ").strip()
        if len(number)>0 and number.isnumeric()==True:
            loop=False
            return number
            
        else:
            print("Please enter valid number !.")

def check_user_entry(prompt,valid_range):
    '''
    This function asks  the user to input data of specified range and
    runs a loop that works until the user entered data is in the  valid range or list.
    Once a valid entry is made, the function returns it.

    parameter
     prompt (str): The message displayed to the user when asking for input.
     valid_range(list):  A list of valid entries that the user is allowed to input.


    return
    This function return the valid entry of the user.
    
    '''
    loop=True
    while loop==True:
        user_entry=input(prompt).lower().strip()
        if user_entry in valid_range:
            loop=False
            return user_entry
        else:
            print("Invalid entry.\n"+str(valid_range) +"is the valid range.\nPlease enter correct data .\n")
def ensure_valid_quantity(user_choice,stock,furniture_Id):
    '''
    This function eunsures that the entered quantity is valid based on the user choice .
    parameter.
    stock(Dictionary):This is the dictionary that contains the stock information of furniture Items.
    furniture_Id(String):user entered valid furniture id  whose quantity they want to buy or sell.

    Return:
    this function returns the valid quantity that lies in the range.


    Raises:
        This function raises a value error if the user enters other value instead of integers
     
    '''
    loop=True
    while loop==True:
        try:
            if user_choice==2:#for purchasing items
                quantity=int(input("Enter the quantity of the item you want to order : "))

            
                if  quantity>0 and (int(stock[furniture_Id][3])+quantity)<1000:
                    return quantity
                    loop=False
                
                else:
                    print("Invalid input or the maximum limit crossed for a furnitutre item i.e( <1000)")
            elif user_choice==3: #for selling furniture items
                quantity=int(input("Enter the quantity that of item you want to sell : "))
                
                if quantity>0 and quantity<=int(stock[furniture_Id][3]):
                    loop=False
                    return quantity
                else:
                    print("\nThe max quantity you can order is  "+stock[furniture_Id][3])
        except Exception as ee:
            print("Invalid data entered : ",str(ee)+"\n")

def get_date_time():
    '''
    This function gives the current date and time .
    It has no parameter.
    Return:
    This function return the current date and time storing it as string datatype.
    '''
   
    year = datetime.datetime.now().year
    month = datetime.datetime.now().month
    day = datetime.datetime.now().day
    hour = datetime.datetime.now().hour
    minute = datetime.datetime.now().minute
    second = datetime.datetime.now().second
    date_time=str(year)+"/"+str(month)+"/"+str(day)+" "+str(hour)+"-"+str(minute)+"-"+str(second)
    return  date_time





def update_dictionary(user_choice,stock,furniture_Id,quantity):
    '''
    This function updates the stock dictionary according to user_choice.
    the stock increases if user_choice=2 and is decreases if user_choice=3

    parameter:
    
    user_choice(int): The choice that user made to sell or purchase.
    stock(Dictionary):This is the dictionary that contains the stock information of furniture Items.
    furniture_Id(String):user entered valid furniture id
    quantity(int): This is the quantity of the funriture item that user wants to sell or purchase.


    returns
    this function returns the updated stock dictionary

    '''
    if user_choice== 2:
        updated_quantity=int(stock[furniture_Id][3])+quantity
        stock[furniture_Id][3]=str(updated_quantity)
        return stock
    elif user_choice==3:
        updated_quantity=int(stock[furniture_Id][3])-quantity
        stock[furniture_Id][3]=str(updated_quantity)
        return stock

def display_invoice(user_choice,stock,ordered_item,total_amount,shipping_charge,date_time):
    '''
    This function  is used to display the bill on the screen.

    parameter:
    user_choice(int): The choice that user made to sell or purchase.
    stock(Dictionary):This is the dictionary that contains the stock information of furniture Items.
    ordered_item(List):This is a 2-D list. IT contains
        Name(string) :contains the emoployee or customer name
        phone_number(string):  phone number of user
        furniture_id(string): user entered valid furniture id
        quantity(int) : quantity user wants
        amount(float):amount for a item
    total_amount(float) :the sum of amount  of all ordered item before adding VAT
    shipping_charge(int): the additions charge taken for delivery
    date_time(string): the current date and time while purchaseing or selling


    this function does not return any value
    
    '''
    amount_with_vat=total_amount+(0.13*total_amount)
    final_amount=amount_with_vat+shipping_charge
    i=1
    print("_"*140)
    print("\n")
    print(" "*40+"-"*62)
    print(" "*40+"|"+" "*60+"|")
    print(" "*40+"|"+" "*24+"BRJ Furniture"+" "*23+"|")
    print(" "*40+"|"+" "*7+"Kamalpokhari, Kathmandu | Phone No: 9801010101"+" "*7+"|")
    print(" "*40+"|"+" "*60+"|")
    print(" "*40+"-"*62)

    print("\n")
    if user_choice==2:
        print("Employee Name : "+ordered_item[0][0]+" "*(95-len(ordered_item[0][0]))+"Date Time : "+date_time)

    elif user_choice==3:
        print("Customer Name : "+ordered_item[0][0]+" "*(95-len(ordered_item[0][0]))+"Date Time : "+date_time)
    print("Phone Number : "+ordered_item[0][1] )
    print("\n")
    print("_"*140)
    print("\n")
    print("|S.no      |" + " " * 19 + " Company Name " + " " * 19 + "|" + " " * 9 + "Furniture Item" + " " * 9 + "|  Quantity  |   Price    |   Amount   |")
    print("-"*140)
    for item in ordered_item:
        print("|" + str(i) + " " * (10 - len(str(i))) + "|  " + stock[item[2]][1] + 
              " " * (50 - len(stock[item[2]][1])) + "|  " + stock[item[2]][2] + 
              " " * (30 - len(stock[item[2]][2])) + "|  " + str(item[3]) + 
              " " * (10 - len(str(item[3]))) + "|  " + stock[item[2]][4] +
              " " * (10 - len(stock[item[2]][4])) + "| " + "$"+str(item[4]) +
              " " * (10 - len(str(item[4]))) + "|  ")
        print("-"*140)
        i=i+1
    print("_"*140)
    print(" "*140)
    print(" "*100+"Total Amount = "+ "$"+str(total_amount))
    print(" "*100+"Amount with VAT = "+ "$"+str(amount_with_vat))
    

    if shipping_charge ==10:
        print(" "*100+"Shipping Charge = "+ "$"+str(shipping_charge))
        print(" "*100+"Amount With Shipping Charge = "+ "$"+str(final_amount))
    else:
        if user_choice==3:
            print(" "*100+"The item wasnot shipped!")
        print(" "*100+"Final amount  = "+ "$"+str(amount_with_vat))
    print(" "*140)
    print("-"*54+"Thank you for Shopping with us !"+"-"*54)

    print("_"*140)

    
    
       
    
    
    

    
    
    
    
    



    
        
    
            

                
                            
                        
    

                  

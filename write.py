def write_stock(stock_dictionary):
    '''
    This function overwrites the dictionary in the stockfile in the same format of the previous dictionary .
    (i.e by joining line by , and breaking after a loop)

    Parameter :

    Stock_dictionary(dictionary):the dictionary containing the updated  stock information.
        the furniture id is the  key while its value is [furniture id,company name,furniture item,quantity,price]
    
    '''
    stockfile=open("stockfile.txt","w")
    for line in stock_dictionary.values():
        line=",".join(line)+"\n"
        stockfile.write(line)
    stockfile.close()

def write_invoice(user_choice,stock,ordered_item,total_amount,shipping_charge,date_time):
    '''
    This function  is used to print the unique bill with unique bill name .

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
    unique=ordered_item[0][0]+date_time.replace("/","")
    invoice_file=open(unique+".txt","w")
    invoice_file.write("\n")
    invoice_file.write("_"*140)
    invoice_file.write("\n")
    invoice_file.write(" "*40+"-"*62)
    invoice_file.write("\n")
    invoice_file.write(" "*40+"|"+" "*60+"|")
    invoice_file.write("\n")
    invoice_file.write(" "*40+"|"+" "*24+"BRJ Furniture"+" "*23+"|")
    invoice_file.write("\n")
    invoice_file.write(" "*40+"|"+" "*7+"Kamalpokhari, Kathmandu | Phone No: 9801010101"+" "*7+"|")
    invoice_file.write("\n")
    invoice_file.write(" "*40+"|"+" "*60+"|")
    invoice_file.write("\n")
    invoice_file.write(" "*40+"-"*62)
    invoice_file.write("\n")
    if user_choice==2:
        invoice_file.write("\n")
        invoice_file.write("Employee Name : "+ordered_item[0][0]+" "*(95-len(ordered_item[0][0]))+"Date Time : "+date_time)
        invoice_file.write("\n")
    elif user_choice==3:
        invoice_file.write("\n")
        invoice_file.write("Customer Name : "+ordered_item[0][0]+" "*(95-len(ordered_item[0][0]))+"Date Time : "+date_time)
        invoice_file.write("\n")
        
    invoice_file.write("Phone Number : "+ordered_item[0][1] )
    invoice_file.write("\n")
    invoice_file.write("\n")
    invoice_file.write("_"*140)
    invoice_file.write("\n")
    invoice_file.write("\n")
    invoice_file.write("|S.no      |" + " " * 19 + " Company Name " + " " * 19 + "|" + " " * 9 + "Furniture Item" + " " * 9 + "|  Quantity  |   Price    |   Amount    |")
    invoice_file.write("\n")
    invoice_file.write("-"*140)
    invoice_file.write("\n")
    for item in ordered_item:
        invoice_file.write("|" + str(i) + " " * (10 - len(str(i))) + "|  " + stock[item[2]][1] + 
              " " * (50 - len(stock[item[2]][1])) + "|  " + stock[item[2]][2] + 
              " " * (30 - len(stock[item[2]][2])) + "|  " + str(item[3]) + 
              " " * (10 - len(str(item[3]))) + "|  " + stock[item[2]][4] +
              " " * (10 - len(stock[item[2]][4])) + "|  " +"$"+ str(item[4]) +
              " " * (10 - len(str(item[4]))) + "|  ")
        invoice_file.write("\n")
        invoice_file.write("-"*140)
        invoice_file.write("\n")
        i=i+1
    invoice_file.write("_"*140)
    invoice_file.write("\n")
    invoice_file.write(" "*140)
    invoice_file.write("\n")
    invoice_file.write(" "*100+"Amount with VAT = "+"$"+str(amount_with_vat))
    invoice_file.write("\n")
    if shipping_charge ==10:
        invoice_file.write(" "*100+"Shipping Charge = "+"$"+str(shipping_charge))
        invoice_file.write(" "*100+"Amount With Shipping Charge = "+"$"+str(final_amount))
        invoice_file.write("\n")
    else:
        if user_choice==3:
            invoice_file.write("\n")
            invoice_file.write(" "*100+"The item wasnot shipped!")
            invoice_file.write("\n")
        invoice_file.write("\n")
        invoice_file.write(" "*100+"Final amount  = "+"$"+str(amount_with_vat))
        invoice_file.write("\n")
    invoice_file.write(" "*140)
    invoice_file.write("\n")
    invoice_file.write("-"*54+"Thank you for Shopping with us !"+"-"*54)
    invoice_file.write("\n")

    invoice_file.write("_"*140)
    invoice_file.write("\n")

    print("\nThe bill has been printed to " +unique+".txt\n")
    invoice_file.close()
    


    
        
    

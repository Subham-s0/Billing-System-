import operation
import read
import write
#Reads the main stock file and stores the stock information in dictionary d
d=read.read_stock()
loop = True
while loop==True:
    try:
        operation.welcome_()#displays the welcome banner
          
        print(" "*32+" _________________________________________________________________________")
        print(" "*32+"|                                                                         |")
        print(" "*32+"|                                                                         |")
        print(" "*32+"|                          SELECT YOUR PREFERENCE:                        |")
        print(" "*32+"|                                                                         |")
        print(" "*32+"|              PRESS 1 TO VIEW FURNITURE AVIAILABLE ON STORE.             |")
        print(" "*32+"|              PRESS 2 TO PURCHASE FURNITURE FROM MANUFACTUTOR.           |")
        print(" "*32+"|              PRESS 3 TO SELL FURNITURE TO CUSTOMERS.                    |")
        print(" "*32+"|              PRESS 4 TO EXIT FOR THE TERMINAL.                          |")
        print(" "*32+"|                                                                         |")
        print(" "*32+"|                                                                         |")
        print(" "*32+"|_________________________________________________________________________|")
        print("\n")
        user_choice=int(input("Enter an option : ") )
        if(user_choice==1):
            #displays all the available stock information 
            operation.display_furniture(d)
        elif(user_choice==2 or user_choice==3):
            #if user enters 2 (purchase),if user enters 3 (sell)
            customer_Name=operation.ensure_valid_name() #Gets valid Customer name
            phone_number=operation.ensure_valid_number() # Gets valid Phn Number
            total_amount=0#total amount of entire transaction
            shipping_charge=0#initializing additional charge
            shipping="n"
            ordered_items=[]#list containting information of ordered items
            
            while True: # this loop runs until the user enters "n" to stop adding item.
                #displays stock information
                operation.display_furniture(d)
                furniture_Id=operation.check_user_entry("Enter the furniture ID : ",list(d.keys()))#Gets valid furniture id 
                if user_choice==3 and d[furniture_Id][3]=="0" or user_choice==2 and d[furniture_Id][3]=="999":
                #the loop is continued or skipped to next iteration because the item is not available on stock or the stock is full
                    if user_choice==3 and d[furniture_Id][3]=="0":
                        print("\nThe item is not available right now.\n")
                    elif user_choice==2 and d[furniture_Id][3]=="999":
                        print("\nThe stock is already full.now\n")#max stock  for a item is 999
                    continue
                quantity=operation.ensure_valid_quantity(user_choice,d,furniture_Id)#gets valid quantity
                #updates the dictionary
                d=operation.update_dictionary(user_choice,d,furniture_Id,quantity)
                #writes the updated dictionary to stockfile
                write.write_stock(d)
                
                amount=float(int(d[furniture_Id][4].replace("$",""))*quantity)#calculates the amount (i.e price x quantity)
                total_amount= total_amount+amount
                item=[customer_Name,phone_number,furniture_Id,quantity,amount]#stores the data in a list
                ordered_items.append(item)#adds the current item to total item
                more_item=operation.check_user_entry("Do you want to order more Item ? [y/n]: ",["y","n"])
                if more_item=="n":
                    break
            if user_choice==3:
                shipping=operation.check_user_entry("Do you want to ship your item ? [y/n]: ",["y","n"])
            if shipping=="y":
                shipping_charge=10
            date_time=operation.get_date_time()# gets current date time
            operation.display_invoice(user_choice,d,ordered_items,total_amount,shipping_charge,date_time)# displays invoice
            write.write_invoice(user_choice,d,ordered_items,total_amount,shipping_charge,date_time) #prints invoice    
        elif user_choice==4:
            #exits from the system
            print("----------------------------------------------------Thank you for shopping with us------------------------------------------------------")
            print("------------------------------------------------------------BRJ Furniture---------------------------------------------------------------")
            loop=False
        else:
            print("Invalid input.\nOption not available")
            

 
    except Exception as ee:
        #handles any exception that occurs during the program
        print(" There was an error  :" , str(ee))
        
        





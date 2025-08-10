def read_stock():
    '''
    This function reads the textfile about and stock information and stores it in a dictionary .
    it removes the the extra spcaes and line break and splits the string by comma.


    Return:
    this function returns the dictionary whose keys is the furniture id and all other data including furniture id is stored as the value of the key
    '''
    stockfile = open("stockfile.txt","r")
    lines=stockfile.readlines()
    stockfile.close()
    stock_dictionary={}
    for line in lines:
        line=line.strip().split(",")
        stock_dictionary[line[0]]=line

    return(stock_dictionary)
    


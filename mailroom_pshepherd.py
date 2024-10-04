

def get_zone(zipcode): #change function name to get_zone and zip to zipcode (Takes a ruturns a what does it do)
    '''
    gets the zones of the starting and ending zipcodes for later use

    Args:
        zipcode: takes both the starting and ending zip and runs them through this function

    Returns:
        integer between 1-6 depending on the input zip code, the zone of the zip code
    
    
    '''
    if 1<=zipcode <=6999: # if the zip coedes are in between a certain range, the zone is assigned
        return 1 
    elif 7000< zipcode <=19999:
        return 2
    elif 20000 <= zipcode <= 35999:
        return 3
    elif 36000<= zipcode <= 62999:
        return 4
    elif 63000 <= zipcode <= 84999:
        return 5
    elif 85000<zipcode<= 99999:
        return 6
    else:
        return None # if the input is not between any of these numbers, return none
def get_type(length,height,width): 
    """

    Takes the user input of the length, width, and height and figures our what type of package the user has input

    Args:
        length (float): the length of the package
        width (float): the width of the package
        height (float): the height of the package
    
    Returns:
        mail_type: the type of package to be used to determine the cost

    """
    if 3.5<= length<=4.25 and 3.5<=height<=6 and 0.007<=width<=0.016: # Checks if the length, width and height match to a specific mail type
        return 'pst_crd' # return type as "post card"
    elif 4.25< length<=6 and 6<height<=11.5 and 0.007<=width<=0.015:
        return 'lrg_pst_crd' # return type as "large post card"
    elif 3.5<= length<=6.125 and 5<=height<=11.5 and 0.16<=width<=0.25:
        return 'envelope'# return type as "envelope"
    elif 6.125< length<=24 and 11<=height<=18 and 0.25<width<=0.5:
        return 'lrg_envelope' # return type as "large envelope"
    elif length + 2* (width + height) <= 84:
        return 'pckge' # return type as "package"
    elif length + 2 * (width + height) <= 130:
        return 'lrg_pckge' # return type as "large package"
    else:
        return 'unmailable' # if the dimensions don't fit the parameters of a mailable package, than return that the package is unmailable
def get_cst(mail_type, dist):

    '''
    
    using the distance and mailtype, calculates the cost of the package

    Args:
        mail_type: the type of mail, each diffrent mail type has a diffrent cost
        dist: the amount of zones needed to travel to mail the package

    Returns:
        cost: number for total cost to ship a package



        
    '''
    if mail_type == 'pst_crd': # each mail type has a flat mail cost added to a additional mailling cost which is multiplied by the zomes the package must travel through
        return 0.20 + dist * 0.03
    elif mail_type == 'lrg_pst_crd':
        return 0.37 + dist * 0.03
    elif mail_type =='envelope':
        return 0.37 + dist * 0.04
    elif mail_type == 'lrg_envelope':
        return 0.6 + dist * 0.05
    elif mail_type == 'pckge':
        return 2.95 + dist * 0.25
    elif mail_type == 'lrg_pckge':
        return 3.95 + dist * 0.35
    else:
        return "unmailable" # if the mailtype was previousely defined as unmailable, then the funcution will continue to return that the package is unmailable
def main():
    '''



    Args:
    length (float): the length of the package
    width (float): the width of the package
    height (float): the height of the package

    '''
    
    mesurements=input('What are the dimensions and sending location of your box (length, height, width, your zip, the zip of receiving location)').split(",")
    
    zip_end = 0 
    dist = 0
    length = 0
    width = 0
    zip_start = 0
    height = 0
    mail_type = 0



    if len(mesurements) != 5:
        print("Enter the correct data")

    else:
        # Define perameters of the package and define terms
        try:
            length = float(mesurements[0]) # Names length and turns it into a float
            height = float(mesurements[1]) # Names height and turns it into a float
            width = float(mesurements[2]) # Names width and turns it into a float
            zip_start = int(mesurements[3]) # Names starting zip code and turns it into a integer
            zip_end = int(mesurements[4]) # Names ending zip code and turns it into a integer
        except ValueError: # if there is a letter or special character, stop the program and alert the user that thier input is not usable
            print('Your input contains a letter or other special character. Please print your mesurements in digits.')
        try:
            dist = abs(get_zone(zip_start) - get_zone(zip_end)) # grabs the diffrence between the two zones, so you can calculate the price
        except TypeError: 
            print('Your input does not follow mailing parameters because someting you have input is wrong, please try again')
        mail_type = get_type(length,height,width) # Sends Length, Height, Width to the function get_type to get the type
        
        if mail_type == 'unmailable' or 99999<zip_start or zip_start<0 or zip_end>99999 or zip_end<0: 
            print("I'm sorry but the dimensions or zip codes of the package you have input qualify as unmailabe, please try again.") # If the mail type was retured as unmailable or the zip code is out of bounds, ends the program
        else:
            print('The total cost to mail this package is ' + str(get_cst(mail_type, dist))) # If the package is mailable the mail type and distance are sent to get the cost
main()



import random
uppercase_list = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
lowercase_list = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z',' ']
vowel_list = ['a','e','i','o','u']

def name_checker(name):
    '''
    Checks name to see if it's a name

    Args:
        name(str): the name that the user input.
    
    Returns:
        bool: If the name is valid, return True, else return False.  

    Raises:
        None
    '''

    name = ''.join(name)
    for i in lowercase(name):
        if i not in lowercase_list:
            return False
    return True

def lowercase(name):    
    '''
    Turns the input to lowercase

    Args:
        name(str): the input.
    
    Returns:
        name(str): Return the input as lowercase version of itself. 

    Raises:
        None
    '''
    lowercase_name = []
    for i in range(len(name)):
        name_part = list(name[i])
        for l in range(len(name_part)):
            for k in range(len(uppercase_list)):
                if name_part[l] == uppercase_list[k]:
                    name_part[l] = lowercase_list[k]
        name_part=''.join(name_part)
        lowercase_name.append(name_part)
    lowercase_name=' '.join(lowercase_name)
    return lowercase_name    
   
def uppercase(name):
    '''
    Turns the input to uppercase

    Args:
        name(str): the input.
    
    Returns:
        name(str): Return the input as uppercase version of itself. 

    Raises:
        None
    '''
    uppercase_name = []
    for i in range(len(name)):
        name_part = list(name[i])
        for l in range(len(name_part)):
            for k in range(len(lowercase_list)):
                if name_part[l] == lowercase_list[k]:
                    name_part[l] = uppercase_list[k]
        name_part=''.join(name_part)
        uppercase_name.append(name_part)
    uppercase_name=' '.join(uppercase_name)
    return uppercase_name

def reverse(name):
    '''
    Reverses the name

    Args:
        name(str): the input.
    
    Returns:
        name(str): A reversed version of itself. 

    Raises:
        None
    '''
    print(name[:0])
    return name

def vowel_counter(name):
    '''
    Reverses the name

    Args:
        name(str): the input.
    
    Returns:
        counted_vowels(str): A string stating the amount of vowels in the name

    Raises:
        None
    '''
    counter = 0
    name = lowercase(name)
    name = list(name)
    for i in range(len(name)):
        for k in range(len(vowel_list)):
            if name[i] == vowel_list[k]:
                counter += 1
    name = ''.join(name)
    counter = str(counter)
    counted_vowels = "Your vowel total is: " + counter
    return counted_vowels

def consonant_counter(name):
    '''
    Counts the consonants in the name

    Args:
        name(str): the input.
    
    Returns:
        counted_consanants(str): A string stating the amount of consanants in the name

    Raises:
        None
    '''
    counter = 0
    name = lowercase(name)
    name = list(name)
    for i in range(len(name)):
        vowels = False
        for k in range(len(vowel_list)):
            if name[i] == vowel_list[k]:
                vowels = True
        if vowels == False:
            counter += 1
    name = ''.join(name)
    counter = str(counter)
    counted_consanants = "Your consonant total is: " + counter
    return counted_consanants


def get_name():
    '''
    Gets the name from the user and checks whether the name has a title

    Args:
        name(str): the input.
    
    Returns:
        name(str): The name, with the title taken out to get true name

    Raises:
        None
    '''
    name = input("Please input your full name [First Middle(if you have one) Last]: ")
    name = name.split()
    if uppercase(name[0]) == "SIR." or uppercase(name[0]) == "DR." or uppercase(name[0]) == "PH.D":
        print("Title is: " + name[0])
        name = name[1:]
    if name_checker(name) == False:
        while name_checker(name) == False:
            print("You have input something other then a letter")
            name = input("Please input your full name [First Middle(if you have one) Last]: ")
    return name

def first_name(name):
    '''
    Gets the first name of the user

    Args:
        name(str): the input
    
    Returns:
        first_name(str): The first name
    Raises:
        None
    '''
    first_name = name[0]
    return first_name

def last_name(name):
    if len(name) < 1:
        print("No last name given")
        return False
    else:
        last_name = name[-1].strip('.')
    return last_name

def middle_name(name):    
    '''
    Gets the middle name

    Args:
        name(str): the input.
    
    Returns:
        middle_name(str): The middle name if given, or a string stating that the input has no middle name

    Raises:
        None
    '''
    if len(name) < 3:
        middle_name = "No middle name given."
    else:
        middle_name = (name[1:-2])
    return middle_name

def scramble(name):
    '''
    Scrambles the letters of the name

    Args:
        name(str): the input.
    
    Returns:
        scrambled_name(str): A string with all the letters in the name scrambled

    Raises:
        None
    '''
    namelist = ''.join(name)
    namelist = list(namelist)
    random.shuffle(namelist)
    namelist = ''.join(namelist)
    scrambled_name = namelist
    return scrambled_name

def reverse(name):
    '''
    Reverses the name

    Args:
        name(str): the input.
    
    Returns:
        reversed_name(str): A string of the reversed name

    Raises:
        None
    '''

    name_list = ''.join(name)
    name_list = list(name_list)
    reversed_name = name_list[::-1]
    reversed_name = ''.join(reversed_name)
    return reversed_name

def palindrome_checker(name):
    '''
    Checks whether the name is a palindrome

    Args:
        name(str): the input.
    
    Returns:
        boolean: States whether the name is a palindrome

    Raises:
        None
    '''
    name_list = ''.join(name)
    reversed_name_list = ''.join(reverse(name))
    if lowercase(reversed_name_list) == lowercase(name_list):
        return True
    else:
        return False
def initial_finder(name):
    '''
    Gets the initials of the given name

    Args:
        name(str): the input.
    
    Returns:
        initials(str): A string representing the initials of the name

    Raises:
        None
    '''
    initials = []
    for i in range(len(name)):
        initial = list(name[i])[0]
        initials.append(str(initial) + '.')
    initials = ''.join(initials)
    initials = initials[0:-1]
    return initials
def main():
    name = get_name()
    menu = "1. Pick new name\n2. Put name into lowercase\n3. Put name into uppercase\n4. Reverse name\n5. Vowel counter\n6. Consonant counter\n7. Print first name\n8. Print last name\n9. Print middle name\n10. Scramble name\n11. Palindrome checker\n12. Print initials" 
    while True:
        print(menu)
        menu_choice = input("Which function would you like to perform?")
        if menu_choice == "1":
            name = get_name()
        elif menu_choice == "2":
            print(lowercase(name))
        elif menu_choice == "3":
            print(uppercase(name))
        elif menu_choice == "4":
            print(reverse(name))
        elif menu_choice == "5":
            print(vowel_counter(name))
        elif menu_choice == "6":
            print(consonant_counter(name))
        elif menu_choice == "7":
            print(first_name(name))
        elif menu_choice == "8":
            print(last_name(name))
        elif menu_choice == "9":
            print(middle_name(name))
        elif menu_choice == "10":
            print(scramble(name))
        elif menu_choice == "11":
            print("palindrome = "+ str(palindrome_checker(name)))
        elif menu_choice == "12":
            print("Your initials are " + str(initial_finder(name)))
        else:
            print("Please input a number listed above.")
main()


    

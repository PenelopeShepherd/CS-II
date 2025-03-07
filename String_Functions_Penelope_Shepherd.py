import random
uppercase_list = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
lowercase_list = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z',' ']
vowel_list = ['a','e','i','o','u']

def word_checker(thing):
    '''
    Checks word to see if it's a word

    Args:
        thing(str): the word that the user input.
    
    Returns:
        bool: If the word is valid, return True, else return False.  

    Raises:
        None
    '''

    thing = ''.join(thing)
    for i in list(thing):
        if lowercase(i) not in lowercase_list:
            return False
    return True

def lowercase(thing):    
    '''
    Turns the input to lowercase

    Args:
        thing(str): the input.
    
    Returns:
        thing(str): Return the input as lowercase version of itself. 

    Raises:
        None
    '''
    thing = list(thing)
    for i in range(len(thing)):
        for k in range(len(uppercase_list)):
            if thing[i] == uppercase_list[k]:
                thing[i] = lowercase_list[k]
    thing = ''.join(thing)
    return thing    
   
def uppercase(thing):
    '''
    Turns the input to uppercase

    Args:
        thing(str): the input.
    
    Returns:
        thing(str): Return the input as uppercase version of itself. 

    Raises:
        None
    '''
    thing = []
    for i in range(len(thing)):
        for k in range(len(lowercase_list)):
            if thing[i] == lowercase_list[k]:
                thing[i] = uppercase_list[k]
    thing = ''.join(thing)      
    return thing

def reverse(word):
    '''
    Reverses the word

    Args:
        word(str): the input.
    
    Returns:
        thing(str): A reversed version of itself. 

    Raises:
        None
    '''
    print(word[:0])
    return word

def vowel_counter(word):
    '''
    Reverses the word

    Args:
        word(str): the input.
    
    Returns:
        thing(str): A reversed version of itself. 

    Raises:
        None
    '''
    counter = 0
    word = lowercase(word)
    word = list(word)
    for i in range(len(word)):
        for k in range(len(vowel_list)):
            if word[i] == vowel_list[k]:
                counter += 1
    word = ''.join(word)
    counter = str(counter)
    print("Your vowel total is: " + counter)
    return word

def consonant_counter(word):
    '''
    Counts the consonants in the word

    Args:
        word(str): the input.
    
    Returns:
        thing(str): A reversed version of itself. 

    Raises:
        None
    '''
    counter = 0
    word = lowercase(word)
    word = list(word)
    for i in range(len(word)):
        vowels = False
        for k in range(len(vowel_list)):
            if word[i] == vowel_list[k]:
                vowels = True
        if vowels == False:
            counter += 1
    word = ''.join(word)
    counter = str(counter)
    print("Your consonant total is: " + counter)
    return word


def get_name():
    name = input("Please input your full name [First Middle(if you have one) Last]: ")
    name = name.split()
    if uppercase(name[0]) == "SIR." or uppercase(name[0]) == "DR." or uppercase(name[0]) == "PH.D":
        print("Title is: " + name[0])
        name = name[1:]
    if word_checker(name) == False:
        while word_checker(name) == False:
            print("You have input something other then a letter")
            name = input("Please input your full name [First Middle(if you have one) Last]: ")
    return name

def first_name(name):
    print(name[0])
    return name

def last_name(name):
    if len(name) < 1:
        print("No last name given")
        return False
    else:
        last_name = name[-1].strip('.')
    return last_name

def middle_name(name):
    if len(name) < 3:
        print("No middle name given.")
        return name
    else:
        print(name[1:-2])

def scramble(name):
    namelist = ''.join(name)
    namelist = list(namelist)
    random.shuffle(namelist)
    namelist = ''.join(namelist)
    print(namelist)

def reverse(name):

    name_list = ''.join(name)
    name_list = list(name_list)
    reversed_name = name_list[::-1]
    return reversed_name

def palindrome_checker(name):
    name_list = ''.join(name)
    reversed_name_list = ''.join(reverse(name))
    if lowercase(reversed_name_list) == lowercase(name_list):
        return True
    else:
        return False
def initial_finder(name):
    initials = []
    for i in range(len(name)):
        initial = list(name[i])[0]
        initials.append(str(initial) + '.')
    initials = ''.join(initials)
    initials = initials[0:-1]
    return initials
def main():

    name = get_name()

    print

    print(lowercase(name))
    print(uppercase(name))
    print(reverse(name))
    vowel_counter(name)
    consonant_counter(name)
    first_name(name)
    last_name(name)
    middle_name(name)
    scramble(name)
    print("palindrome = "+ str(palindrome_checker(name)))
  
    print("Your initials are " + str(initial_finder(name)))

main()


    
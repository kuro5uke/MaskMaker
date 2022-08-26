import string
import cleancombo22

print("""\n
oooo     oooo      o       oooooooo8 oooo   oooo              
 8888o   888      888     888         888  o88                
 88 888o8 88     8  88     888oooooo  888888                  
 88  888  88    8oooo88           888 888  88o                
o88o  8  o88o o88o  o888o o88oooo888 o888o o888o              
                                                              
oooo     oooo      o      oooo   oooo ooooooooooo oooooooooo  
 8888o   888      888      888  o88    888    88   888    888 
 88 888o8 88     8  88     888888      888ooo8     888oooo88  
 88  888  88    8oooo88    888  88o    888    oo   888  88o   
o88o  8  o88o o88o  o888o o888o o888o o888ooo8888 o888o  88o8\n""")

def string_to_mask(s):

    lower = list(string.ascii_lowercase)
    upper = list(string.ascii_uppercase)
    digit = list(string.digits)
    speci = list(string.punctuation)

    result = []

    # for every character in char array
    for character in s:

        #*** WRITTEN WITH HASHCAT MASK RULES IN MIND - CHNAGE TO FIT YOUR PASSWORD CRACKER ***
        
        if character in lower:
            result.append("?l")
        elif character in upper:
            result.append("?u")
        elif character in digit:
            result.append("?d")
        elif character in speci:
            result.append("?s")
            
        #*** WRITTEN WITH HASHCAT MASK RULES IN MIND - CHNAGE TO FIT YOUR PASSWORD CRACKER ***

    return result # return mask (as a list) when function is called


def email_counter():
    counter = {}

    for email in emails:

        if email in counter:
            counter[email] += 1
        else:
            counter[email] = 1

def mask_counter():
    counter = {}

    for mask in masks:

        if mask in counter:
            counter[mask] += 1
        else:
            counter[mask] = 1
    

file = cleancombo22.combopath() # Call to clean combo function

with open(cleancombo22.cleanpass(file)) as passwords_list:

          passwords = passwords_list.readlines()
 
          masks = [] # Create empty list for hashcat masks
          
          for password in passwords:
              mask = ''.join(string_to_mask(password)) # Convert function return value (mask as list) to string

              masks.append(mask) # Add mask to list

counter = {} # Write masks and count to dictionary with for loop

for mask in masks:
    
    if mask in counter:
        counter[mask] += 1 # Write masks and count to dictionary with for loop

    else:
        counter[mask] = 1

counter_list = sorted(counter.items(), key=lambda x:x[1], reverse=True)   # Convert dictionary to list

sort_counter = dict(counter_list)   # Sort values

with open('maskcount.txt', 'w') as data: # Overwrites last maskcount
    
    for k, v in sort_counter.items():
        key_pairs = k + ": " + str(v) + "\n"

        data.write(key_pairs)


decision = str(input("\nCreate an email file?\n [y/N]: \n"))

if decision == 'y' or decision == 'Y':
    usernames = cleancombo22.cleanuser(file)
    print(usernames)
    
else:
    print("\nThank You")

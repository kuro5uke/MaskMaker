def banner():
    print(
"""\n
 ▄████████  ▄█          ▄████████    ▄████████ ███▄▄▄▄        
███    ███ ███         ███    ███   ███    ███ ███▀▀▀██▄      
███    █▀  ███         ███    █▀    ███    ███ ███   ███      
███        ███        ▄███▄▄▄       ███    ███ ███   ███      
███        ███       ▀▀███▀▀▀     ▀███████████ ███   ███      
███    █▄  ███         ███    █▄    ███    ███ ███   ███      
███    ███ ███▌    ▄   ███    ███   ███    ███ ███   ███      
████████▀  █████▄▄██   ██████████   ███    █▀   ▀█   █▀       
           ▀                                                  
 ▄████████  ▄██████▄    ▄▄▄▄███▄▄▄▄   ▀█████████▄   ▄██████▄  
███    ███ ███    ███ ▄██▀▀▀███▀▀▀██▄   ███    ███ ███    ███ 
███    █▀  ███    ███ ███   ███   ███   ███    ███ ███    ███ 
███        ███    ███ ███   ███   ███  ▄███▄▄▄██▀  ███    ███ 
███        ███    ███ ███   ███   ███ ▀▀███▀▀▀██▄  ███    ███ 
███    █▄  ███    ███ ███   ███   ███   ███    ██▄ ███    ███ 
███    ███ ███    ███ ███   ███   ███   ███    ███ ███    ███ 
████████▀   ▀██████▀   ▀█   ███   █▀  ▄█████████▀   ▀██████▀  
                                                              

A simple script for turning combolists into email or password lists.
By civilkmkz
\n
""")

def combolist():
    #Combolist used as argument for functions
    filename = input("Please specify combolist file path:")
    return filename

#CLEAN PASSWORDS FUNCTION
def cleanpass(combolist):

    newfilename = input("\nName for new password list (with extension - ie: .txt)?: ") #Prompts user for input
    
    with open(combolist) as f:
        lines = f.readlines()

        passwords = []

    for line in lines:
        password = line.split(":")[1]
        passwords.append(password)

    print ("\nTotal number of combos = " + str((len(passwords))))

    newfile = open(newfilename, 'w')

    startoff = int(input("\nWhich combo to start at?: (0 for first combo) "))
    print("\nStarting at " + passwords[startoff])
    cutoff  = int(input("\nWhich combo to stop at?: "))
    print("\nStopping at" + passwords[cutoff])

    #For password in list "up to" (:)cutoff [:cutoff]
    shortlist = passwords[startoff:cutoff]
    print(shortlist)
    print()

    for word in shortlist:
        newfile.write(word)
        print(word)

    newfile.close
    newfile = open(newfilename, 'r')
    return newfilename
    
#CLEAN USERNAMES FUNCTION
def cleanuser(combolist):

    newfilename = input("\nName for new e-mail/username list (with extension - ie: .txt)?: ") #Prompts user for input

    with open(combolist) as f:
        lines = f.readlines()

        usernames = []

    for line in lines:
        username = line.split(":")[0]
        usernames.append(username)

    print ("\nTotal number of combos = " + str((len(usernames))))

    newfile = open(newfilename, 'w')

    startoff = int(input("\nWhich combo to start at?: (0 for first combo) "))
    print("\nStarting at " + usernames[startoff])
    cutoff  = int(input("\nWhich combo to stop at?: "))
    print("\nStopping at" + usernames[cutoff])

    #For username in list "up to" (:)cutoff [:cutoff]
    shortlist = usernames[startoff:cutoff]
    print(shortlist)
    print()

    for user in shortlist:
        newfile.write(user+"\n")
        print(user)

    newfile.close
    newfile = open(newfilename, 'r')
    return newfilename

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

# FUNCTION RETURNS COMBOLIST'S FILE PATH WHEN CALLED.

def combopath():
        filepath = input("\nPlease specify existing combolist's file path:")
        return filepath

def strip_option(cleanlist):

                x = int(input("\n List Options:\nPress 0 - Use entire list.\nPress 1 - Specify a range.\n"))
                
                if x == 1:
                                startoff = int(input("\nWhich line to start at?:(0 for first line)"))
                                print("\nStarting at " + cleanlist[startoff])
                                cutoff = int(input("\nWhich line to stop at?:"))
                                print("\nStopping at" + cleanlist[cutoff])
                                
                                shortlist = cleanlist[startoff:cutoff]
                                
                else:
                                shortlist = cleanlist
                
                return shortlist
                
# FUNCTION RETURNS A FILE CONTAINING STRIPPED PASSWORDS

def cleanpass(combolist):

    passwordfile = input("\nName (your) new password list:")

    with open(combolist) as f:
        lines = f.readlines()

    passwords = [] # initialize empty list for passwords

    for line in lines:
        password = line.split(":")[1] # set password variable to index 1
        passwords.append(password) # write each password to passwords list

    print ("\nTotal number of passwords = " + str((len(passwords))))

    newfile = open(passwordfile, 'w') # open user-defined "passwordfile" in write mode
    shortlist = strip_option(passwords) # set shortlist to strip_option return value

    for word in shortlist:
        newfile.write(word)
        print(word)

    newfile.close
    newfile = open(passwordfile, 'r')
    return passwordfile

#FUNCTION RETURNS A FILE CONTAINING STRIPPED USERNAMES

def cleanuser(combolist):

    usernamefile = input("\nName for new e-mail/username list (with extension - ie: .txt)?: ") #Prompts user for input
    
    with open(combolist) as f:
        lines = f.readlines()

    usernames = [] # initialize empty list for usernames

    for line in lines:
        username = line.split(":")[0] # set user variable to index 0
        usernames.append(username) # write each user to passwords list

    print ("\nTotal number of usernames = " + str((len(usernames))))

    newfile = open(usernamefile, 'w') # open user-defined "passwordfile" in write mode
    shortlist = strip_option(usernames) # set shortlist to strip_option return value

    for user in shortlist:
        newfile.write(user+"\n")
        print(user)

    newfile.close
    newfile = open(usernamefile, 'r')
    return usernamefile

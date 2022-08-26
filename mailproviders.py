x = str(input("\nEmail list?"))
file = open(x, 'r') # open email list in read mode

emails = file.readlines() # init "emails" as list read in from file

def email_providers(email_list):
    
    counter = {}

    for email in email_list:
        
        provider = email.split("@")[1] # init "provider" as everything after "@" char

        if provider in counter:
            counter[provider] += 1 # increment by 1
        else:
            counter[provider] = 1

    # Convert counter to a list and sort in descending order
    provider_list = sorted(counter.items(), key=lambda x:x[1], reverse=True)

    providers = dict(provider_list)  # Convert back into a dictionary

    # Create/Overwrite file named "providercount.txt"
    with open('providercount.txt', 'w') as data:

        for k, v in providers.items():

            key_pairs = k.strip() + ":" + str(v) + " \n" # string format

            data.write(key_pairs)

    return key_pairs

email_providers(emails)

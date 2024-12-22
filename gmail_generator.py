# Display the banner at the beginning
print("""
=====================================================================================
    ╔═══╗╔═╗╔═╗╔═══╗╔══╗╔╗       ╔═══╗╔═══╗╔═╗ ╔╗╔═══╗╔═══╗╔═══╗╔════╗╔═══╗╔═══╗
    ║╔═╗║║║╚╝║║║╔═╗║╚╣╠╝║║       ║╔═╗║║╔══╝║║╚╗║║║╔══╝║╔═╗║║╔═╗║║╔╗╔╗║║╔═╗║║╔═╗║
    ║║ ╚╝║╔╗╔╗║║║ ║║ ║║ ║║       ║║ ╚╝║╚══╗║╔╗╚╝║║╚══╗║╚═╝║║║ ║║╚╝║║╚╝║║ ║║║╚═╝║
    ║║╔═╗║║║║║║║╚═╝║ ║║ ║║ ╔╗    ║║╔═╗║╔══╝║║╚╗║║║╔══╝║╔╗╔╝║╚═╝║  ║║  ║║ ║║║╔╗╔╝
    ║╚╩═║║║║║║║║╔═╗║╔╣╠╗║╚═╝║    ║╚╩═║║╚══╗║║ ║║║║╚══╗║║║╚╗║╔═╗║ ╔╝╚╗ ║╚═╝║║║║╚╗
    ╚═══╝╚╝╚╝╚╝╚╝ ╚╝╚══╝╚═══╝    ╚═══╝╚═══╝╚╝ ╚═╝╚═══╝╚╝╚═╝╚╝ ╚╝ ╚══╝ ╚═══╝╚╝╚═╝                                                                         
                                                                                                                   
                         Gmail Generator Created - By ASADQI
                             Website: https://asadqi.com
=====================================================================================
""")


import random

# List of Arabic names to be used in the alias generation
arabic_names = [
    "ahmed", "mohammed", "ali", "fatima", "sarah", "omar", "zainab", "layla", "noura", "hassan", 
    "yasmine", "khalid", "salma", "huda", "mariam", "ramez", "samira", "bilal", "tariq", "lina",
    "fayza", "karim", "yasir", "salim", "nehal", "aisha", "tawfiq", "nada", "kawthar", "mahmoud",
    "zahra", "islam", "sami", "rawan", "lina", "yasmin", "faris", "nour", "karim", "bilal", "selim",
    "nada", "zain", "shaimaa", "karim", "mona", "nada", "ali", "rami", "mohammad", "sulaiman", "aamir",
    "tamer", "hassan", "khalil", "amira", "zeinab", "azhar", "samar", "ramzi", "mustafa", "ibrahim"
]

def generate_aliases(gmail_account, num_aliases):
    aliases = []
    
    # Generate the specified number of aliases
    for i in range(num_aliases):
        name = arabic_names[i % len(arabic_names)]  # Cycle through the names if needed
        alias = f"{gmail_account}+{name}{i}@gmail.com"  # Append an index to ensure uniqueness
        aliases.append(alias)
    
    return aliases

def save_to_file(aliases):
    # Save generated aliases to emails.txt
    with open("emails.txt", "w") as file:
        for alias in aliases:
            file.write(alias + "\n")
    print(f"Generated {len(aliases)} email addresses have been saved to 'emails.txt'.")

def main():
    # Ask for the Gmail account
    gmail_account = input("Enter your Gmail account (without @gmail.com): ")
    
    # Specify how many email aliases you want to generate
    num_aliases = int(input("Enter the number of email aliases to generate (e.g., 1000): "))
    
    # Generate aliases
    aliases = generate_aliases(gmail_account, num_aliases)
    
    # Save to file
    save_to_file(aliases)

if __name__ == "__main__":
    main()


from string import ascii_uppercase, ascii_lowercase, digits, punctuation
import json
import random
import os

filename = "vault.json"

def load_vault():
    if os.path.exists(filename):
        with open(filename, "r") as file:
            data = json.load(file)
            return data
    else:
        return {}

def save_vault(vault_data):
    with open(filename, "w") as file:
        json.dump(vault_data, file, indent=4)

def generate_password():
    while True:
        try:
            length = int(input("enter desired password length: "))
            if length > 0:
                break
            else:
                print("cannot be less than zero")
        except ValueError:
            print("Invald input")
        
    use_upper = input("Include uppercase(y/n): ").lower()
    use_numbers = input("Include numbers(y/n): ").lower()
    use_symbol = input("Include symbols(y/n): ").lower()

    char_pool = ascii_lowercase
    if use_upper == 'y':
        char_pool += ascii_uppercase
    if use_numbers == 'y':
        char_pool += digits
    if use_symbol == 'y':
        char_pool += punctuation
    
    password = ""
    for i in range(length):
        random_char = random.choice(char_pool)
        password += random_char 

    return password

def main():
    vault_dict = load_vault()  

    while True:
        print("""---Password Vault---
        1. Generate a New Password
        2. Look up a saved password
        3. Exit
                        """)

        choice = input("Choose an option: ")

        if choice == '1':
            new_password = generate_password()
            print(f"new password is {new_password}")
            
            save_prompt = input("Would tou like to save this password(y/n):").lower()
            if save_prompt == 'y':
                website_name = input("Enter Website name: ")
                username = input("Enter username: ")

                vault_dict[website_name] = {"username": username, "password": new_password}
                save_vault(vault_dict)
                print("password securely saved")

        elif choice == '2':
            search_site = input("Enter a website name: ")
            
            if search_site in vault_dict:
                retrieved_entry = vault_dict[search_site]
                print(f"username: {retrieved_entry["username"]}")
                print(f"password: {retrieved_entry["password"]}")
            else:
                print("no entry found")
        
        elif choice == '3':
            print("Goodbye")
            break
             
if __name__ == "__main__":
    main()

    


 






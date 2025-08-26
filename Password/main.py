def main():
    from passwordmanager import PasswordManager

    passwords = {
    }

    pm = PasswordManager()

    
    
    done = False
    while not done:

        print("""What do you want me to do?
          (1) Create a new key
          (2) Load an existing key
          (3) Create a new password file
          (4) Load existing password file
          (5) Add a new password
          (6) Delete a password
          (7) Get a password
          (q) Quit
          """)

        choice = input("Enter your choice: ")
        if choice == "1":
            path = input("Enter path: ")
            pm.createkey(path)

        elif choice == "2":
            path = input("Enter path: ")
            pm.loadkey(path)

        elif choice == "3":
            path = input("Enter path: ")
            pm.createpasswordfile(path, passwords)

            #create option to add their own passwords OR start with empty file

        elif choice == "4":
            path = input("Enter path: ")
            pm.loadpasswordfile(path)

        elif choice == "5":
            site = input("Enter site: ")
            password1 = input("Enter password: ")
            pm.addpassword(site, password1)

        elif choice == "6":
            site = input ("Enter site: ")
            password1 = input("Enter password: ")
            if (pm.getpassword(site) == password1):
                confirm = input("Are you sure? [Y]/[N] YOU CANNOT UNDO THIS ACTION: ")
                if (confirm == "Y"):
                    pm.deletepassword(site)
            else:
                print("AUTHORIZATION FAILED (Incorrect password)")
                    

        elif choice == "7":
            site = input("Enter site: ")
            print(f"Password for {site} is {pm.getpassword(site)}")

        elif choice == "q":
            done = True
            print("Thank you!")
        else:
            print("INVALID")

if __name__ == "__main__":
    main()
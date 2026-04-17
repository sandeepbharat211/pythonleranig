from getpass import getpass
correct_user = "sandeep"
correct_pass = "1234"

for i in range(3):
    username = input("Enter Your Username: ")
    if correct_user!= username:
        print("Invalid Username")
        continue
    password = getpass("Enter your Password: ")

    if password == correct_pass:
        print("Login Successful")
        break
    else:
        print("Login Failed. Attempts left:",2-i)

else:
    print("Account Locked")
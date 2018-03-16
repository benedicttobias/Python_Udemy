correct_password = "python123"
name = input("Enter name: ")
surname = input("Enter surname: ")

password = input("Enter password: ")

while password != correct_password:
    print("Wrong password!")
    password = input("Enter password: ")

message = "Hi %s %s, you logged in" % (name, surname)
print (message)

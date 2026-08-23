username = input("Enter Username:")
password = input("Enter Password:")

if username == "dave" and password == "python123":
    print("Login Successfully! welcome dave")
elif username == "dave":
    print("Username is correct, password doesn't match")
else:
    print("not found")

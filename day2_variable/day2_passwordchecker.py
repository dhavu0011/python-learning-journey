password = input("Enter Password : ")
length = len(password)
if 1 <= length <= 7:
    print("password is too short.")
elif length >= 8:
    print("Valid password.")
else:
    print("wrong input.")

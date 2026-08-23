age = int(input("Enter the age :"))
if age <= 12 and age >= 0:
    print("child ticket is : $8")
elif age < 60 and age > 12:
    print("adult ticket is : $15")
elif age >= 60:
    print("senior tickets: $10")
else:
    print("wrong input")

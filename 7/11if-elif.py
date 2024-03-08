#
age = input("Enter your age.")
if int(age) >= 18:
    print("you can vote")
elif int(age) < 18 and int(age) > 3:
    print("you are in school")
else:
    print("you are a kid")
print("thank you")
#error rais so proggram stops and nothing unexpected happens
a = input("Enter the value:-")

if(a != "quit"):
    raise ValueError("Please enter the correct input")
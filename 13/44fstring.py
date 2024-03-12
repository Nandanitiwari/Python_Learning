#string formatting

#previous
letter = "hey my name is {1} and i am from {0}"
country = "america"
name = "alix"
print(letter.format(country, name))

#better way
print(f"hey my name is {name} and i am from {country}")

txt = "for only {price:.2f} dollars!"
print(txt.format(price = 49))

rate = 49.0099
txt = f"for only {rate:.2f} dollars!"
print(txt)
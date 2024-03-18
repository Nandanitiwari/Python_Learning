import os
folders = os.listdir("data")

# print(folders)

for folder in folders:
    print(folder)
    print(os.listdir(f"data/{folder}"))

# print(os.getcwd())
# os.chdir("/users")
# print(os.getcwd())
# os.chdir("/python")
# print(os.getcwd())



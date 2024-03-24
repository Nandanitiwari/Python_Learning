import time
print(4)
time.sleep(3)  #-->next line will execute after 3 seconds
print("this is printed after 3 second")


#strftime
print("strftime")
t = time.localtime()
formatted_time = time.strftime("%Y-%m-%d %H:%M:%S", t)
print(formatted_time)
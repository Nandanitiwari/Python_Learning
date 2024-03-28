import asyncio
import requests

async def function1():
    print("func 1")
    URL = "https://instagram.com/favicon.ico"
    response = requests.get(URL)
    open("40/images/insta.ico", "wb").write(response.content)
   
    return "Harry"

async def function2():
    print("func 2")
    URL = "https://instagram.com/favicon.ico"
    response = requests.get(URL)
    open("40/images/insta2.ico", "wb").write(response.content)
  

async def function3():
    print("func 3")
    URL = "https://instagram.com/favicon.ico"
    response = requests.get(URL)
    open("40/images/insta3.ico", "wb").write(response.content)
   
    
async def main():
    await function1()
    await function2()
    await function3()
    return 3
   
asyncio.run(main())

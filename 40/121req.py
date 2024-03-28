import asyncio
import requests

async def function1():
    print("func 1")
    URL = "https://instagram.com/favicon.ico"
    response = requests.get(URL)
    open("40/images/instagram.ico", "wb").write(response.content)
   
    return "Harry"

async def function2():
    print("func 2")
    URL = "https://instagram.com/favicon.ico"
    response = requests.get(URL)
    open("40/images/instagram2.ico", "wb").write(response.content)
   

async def function3():
    print("func 3")  
    URL = "https://instagram.com/favicon.ico"
    response = requests.get(URL)
    open("40/images/instagram3.ico", "wb").write(response.content)
   
async def main():
   
    L = await asyncio.gather(
        function1(),
        function2(),
        function3(),
      )
    print(L)
asyncio.run(main())

import asyncio
import time

class Test():
    
    def login(self, username, password):
        asyncio.run(self.keep_conn_alive())
            
    async def keep_conn_alive(self):
        while True:
            await asyncio.sleep(3)
            print("Still awake...")        

            
if __name__ == "__main__":
    test = Test()
    print('logging in...')
    test.login('user', 'pw')

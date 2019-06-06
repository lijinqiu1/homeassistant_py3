import asyncio
import json
import time
from aiohttp import ClientSession
from platform import python_version

# ACCESS_TOKEN = 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJleHAiOjE4NzE1MzY2NjUsImlzcyI6ImViMDQyNmJmYjlkMjRlYjZiY2M5NzU2OGIyMTVlMmJmIiwiaWF0IjoxNTU2MTc2NjY1fQ.blatuvJr7cjtMbGszDH64XPHpWRyt3CnUULSNmItRnI'
ACCESS_TOKEN = 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpYXQiOjE1NTA2NzIzOTAsImlzcyI6ImVmYmU5YWFhMWZlYzQ4YTNhOGVkZTNjNTU2YWE4MTU1IiwiZXhwIjoxODY2MDMyMzkwfQ.GlA1Qb0LmIWqSvkTSgv_7bUyMxq5IfU1kPR9PBBCb5Y'


headers = {
    'Authorization': 'Bearer '+ ACCESS_TOKEN,
    'content-type': 'application/json'}

class aioRsetAPI():
    def __init__(self):
        self.headers = headers
        self.url = 'http://192.168.199.115:8123/api/'

    async def get_all_states(self):
        async with ClientSession(headers=headers) as session:
            async with session.get(self.url+'states') as r:
                print(r.url)
                return await r.read()


if __name__ == '__main__':
    now = lambda: time.time()
    api = aioRsetAPI()
    start = now()
    event_loop = asyncio.get_event_loop()
    results = event_loop.run_until_complete(api.get_all_states())
    event_loop.close()
    if python_version() is not '3.5.3':
        results = results.decode()
    states = json.loads(results)
    for state in states:
        print(state)
    print('TIME: ', now() - start)

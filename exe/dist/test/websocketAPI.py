#!/usr/bin/python3
#
# Copyright (c) 2017-2018, Fabian Affolter <fabian@affolter-engineering.ch>
# Released under the ASL 2.0 license. See LICENSE.md file for details.
#
import asyncio
import json
import time
import asyncws

ACCESS_TOKEN = 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpYXQiOjE1NTA2NzIzOTAsImlzcyI6ImVmYmU5YWFhMWZlYzQ4YTNhOGVkZTNjNTU2YWE4MTU1IiwiZXhwIjoxODY2MDMyMzkwfQ.GlA1Qb0LmIWqSvkTSgv_7bUyMxq5IfU1kPR9PBBCb5Y'


async def main():
    """Simple WebSocket client for Home Assistant."""
    websocket = await asyncws.connect('ws://192.168.199.135:8123/api/websocket')

    await websocket.send(json.dumps(
        {'type': 'auth',
         'access_token': ACCESS_TOKEN}
    ))

    await websocket.send(json.dumps(
        {'id': 1, 'type': 'get_states'}
    ))

    while True:
        message = await websocket.recv()
        if message is None:
            break
        print(message)

        if json.loads(message)['type'] == 'result':
            break

now = lambda: time.time()
start = now()
loop = asyncio.get_event_loop()
loop.run_until_complete(main())
print('TIME: ', now() - start)
loop.close()

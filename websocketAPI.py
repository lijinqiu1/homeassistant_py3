#!/usr/bin/python3
#
# Copyright (c) 2017-2018, Fabian Affolter <fabian@affolter-engineering.ch>
# Released under the ASL 2.0 license. See LICENSE.md file for details.
#
import asyncio
import json
import time
import asyncws

# ACCESS_TOKEN = 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpYXQiOjE1NTA2NzIzOTAsImlzcyI6ImVmYmU5YWFhMWZlYzQ4YTNhOGVkZTNjNTU2YWE4MTU1IiwiZXhwIjoxODY2MDMyMzkwfQ.GlA1Qb0LmIWqSvkTSgv_7bUyMxq5IfU1kPR9PBBCb5Y'
ACCESS_TOKEN = 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpYXQiOjE1NTk4NzUwMDYsImlzcyI6IjE5NTc3ZmU2YjY3YTRiMjZiODhhODMzZjQ4MzE0YWNmIiwiZXhwIjoxODc1MjM1MDA2fQ.bnEpgZcVIqwBWW-0mltkqr2ujZMG7N_YraPYdA_dCYA'

async def main():
    """Simple WebSocket client for Home Assistant."""
    websocket = await asyncws.connect('ws://guoxi3.natapp4.cc/api/websocket')

    await websocket.send(json.dumps(
        {'type': 'auth',
         'access_token': ACCESS_TOKEN}
    ))

    await websocket.send(json.dumps(
        {'id': 1, 'type': 'subscribe_events', 'event_type': 'state_changed'}
    ))

    await websocket.send(json.dumps(
        {'id': 2, 'type': 'get_states'}
    ))

    while True:
        message = await websocket.recv()
        print(message)
        if message is None:
            break
        text = json.loads(message)
        if text['type'] == 'event':
            if text['event']['data']['entity_id'] == 'switch.men_xi':
                print(text['event']['data']['new_state']['state'])
        elif text['type'] == 'result':
            if text['id'] == 2:
                for state in text['result']:
                    print(state['entity_id'])
                    print(state['state'])

now = lambda: time.time()
start = now()
loop = asyncio.get_event_loop()
loop.run_until_complete(main())
print('TIME: ', now() - start)
loop.close()

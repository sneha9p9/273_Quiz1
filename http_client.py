import requests, time
import asyncio
import sys


async def req():
    print(sys.argv[3])
    print('Request 1')
    r = requests.post(sys.argv[1], data={"ts": time.time()})
    print(r.status_code)
    await asyncio.sleep(0)
    print('Request 1 again')
    print(r.status_code)

async def reqq():
    print('Request 2')
    r = requests.post(sys.argv[1], data={"ts": time.time()})
    print(r.status_code)
    await asyncio.sleep(0)
    print('Request 2 again')
    print(r.status_code)

if sys.argv[2] == "sync":
    for i in range(int(sys.argv[3])):
        r = requests.post(sys.argv[1], data={"ts": time.time()})
        print(i, 'Request', r.status_code, r.content)

else:
    ioloop = asyncio.get_event_loop()
    tasks = [ioloop.create_task(req()), ioloop.create_task(reqq())]
    wait_tasks = asyncio.wait(tasks)
    ioloop.run_until_complete(wait_tasks)


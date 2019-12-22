from irispy import Dispatcher, Method
from irispy import objects

import logging

dp = Dispatcher(secret="<helloiris>", user_id="173427551")
logging.basicConfig(level="INFO")


@dp.event_handler(Method.SEND_MY_SIGNAL)
async def func(event: objects.SendMySignal):
    print(event.object)
    # some stuff..


dp.run_app("192.168.43.178", 8080, "/")
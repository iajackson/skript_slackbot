import os
import asyncio
import json
import nats
from nats.errors import TimeoutError, NoRespondersError

class Client:

    def __init__(self, URL) -> None:

        self.URL = URL
        self.Connection = None

    async def connect(self):
        self.Connection = await nats.connect(self.URL)
        print(self.Connection)

    async def sendMessageGetReply(self, subject, message):
        msg = None
        try:
            msg = await self.Connection.request(subject, message, timeout=0.5)
        except NoRespondersError:
            print("no responders")
        if msg != None:
            print(f"{msg.data} on subject {msg.subject}")
            #msg = None
        return msg.data

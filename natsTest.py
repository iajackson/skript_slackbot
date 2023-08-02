import os
import asyncio
import json

import nats
from nats.errors import TimeoutError, NoRespondersError
import natsByExample.natsClientClass as natsClientClass
# subject
# JSON data
# server url = "nats://<username>:<password>@url" below is from my local nats server
servers = os.environ.get("NATS_URL", "nats://local:fkoTpuoFMsyPceQnq0XyH4rj6Xt9TTkv@localhost:34281").split(",")
async def sendMessageGetReply(connection, subject, message):
    msg = None
    try:
        msg = await connection.request(subject, message, timeout=0.5)
    except NoRespondersError:
        print("no responders")
    if msg != None:
        print(f"{msg.data} on subject {msg.subject}")
        #msg = None
    return msg.data


async def main():
    connection = await nats.connect(servers=servers)
    #sub = await nc.subscribe("greet.*")
    subject = "greet.*"
    message = b'Hello'
    reply = None
    reply = await sendMessageGetReply(connection,subject,message)
    
    print(f"Sent request {message}, got reply {reply}")
#    while(1):



    



if __name__ == '__main__':
    asyncio.run(main())

 

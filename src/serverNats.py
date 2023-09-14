"""
Basic call to NATS server

Have NATS up an runnning, 

Functions:
    1. send_to(message): Will return your call to nats, with "Michael did it " in front of it

Author: Michael Vlatko
"""

import os
import asyncio
import nats
from nats.errors import TimeoutError, NoRespondersError


async def send_to(message):
    print("first hurdle")

    servers = os.environ.get("NATS_URL", "nats://nats:4222").split(",")
    nc = await nats.connect(servers=servers)

    insert = "greet." + message.replace(" ", "_")

    async def greet_handler(msg):
        name = msg.subject[6:]
        reply = f"Michael did it: , {name}"
        await msg.respond(reply.encode("utf8"))

    sub = await nc.subscribe("greet.*", cb=greet_handler)

    rep = await nc.request(insert, b"", timeout=10)

    await sub.drain()

    return rep.data.decode("utf-8")

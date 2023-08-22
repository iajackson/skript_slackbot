import os
import nats
import nats.errors
import json

"""
startCollectors Action Module

Calls the nats subject collectors.v1.process.start with the provided params

Functions:
    1. run(input): Calls the nats subject collectors.v1.process.start with the provided params

Author: Ian Jackson
Author: Michael Vlatko
"""

"""
Function name: startCollectors
Function parameter: 43779743-b56d-4bd8-a93a-c1331f345552, 2452f335-0250-48e8-a86a-0b519f1289a0, a59d9998-8088-4428-a8a9-02783409d8f6

The NATs message that this would get translated into -
NATS Subject: 'collectors.v1.process.start'
JSON Data: '{"jobType": "INCREMENTAL", "consentIds": ["43779743-b56d-4bd8-a93a-c1331f345552","2452f335-0250-48e8-a86a-0b519f1289a0","a59d9998-8088-4428-a8a9-02783409d8f6"]}'
The NATS message we would receive back from our microservice
{"status":"OK","jobStartStat":{"customers.v2.collector.start":{"succeeded":7,"failed":0}}}
"""
#takes string and converts to json
def generate_output(message):
    return json.dumps({
        "jobType": "INCREMENTAL",
        "consentIds": message
    })

#takes in user input of consent ids
def get_consent(message):
    consents_str = message[len("example"):].strip()
    consents = [cid.strip() for cid in consents_str.split(",")]
    return consents

async def run(params):
    """
    Calls the nats subject collectors.v1.process.start with the provided params

    Parameters:
        input (string): The function parameter(s) as a string

    Returns:
        string: The output of collectors.v1.process.start

    """

    #strip and assemble input
    insert = get_consent(params)
    consentString = "collectors.v1.process.start." + ''.join(insert)

    #fire up nats server
    servers = os.environ.get("NATS_URL", "nats://nats:4222").split(",")

    #connect to server
    try:
        nc = await nats.connect(servers=servers)
    except Exception as e:
        return "Failed to connect to NATS server"
    
    #function that talks to nats
    async def callback(msg):
        try:
            name = msg.subject[28:]
            reply = name
            await msg.respond(reply.encode("utf8"))
        except Exception as e:
            return "Error in callback"
    
    #set up listening for collectors.v1.process.start
    try:
        sub = await nc.subscribe("collectors.v1.process.start.*", cb=callback)
    except Exception as e:
        return "Error in subscription"
    
    #put assembled string into the server
    try:
        rep = await nc.request(consentString, b'', timeout=10)
    except Exception as e:
        return "Error in requesting"

    await sub.drain()

    #assemble output into json
    response_data = rep.data.decode("utf-8")
    output_json = generate_output(response_data)

    return output_json
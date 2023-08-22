"""
startCollectors Action Module

Calls the nats subject collectors.v1.process.start with the provided params

Functions:
    1. run(input): Calls the nats subject collectors.v1.process.start with the provided params

Author: Ian Jackson
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


def run(params):
    """
    Calls the nats subject collectors.v1.process.start with the provided params

    Parameters:
        input (string): The function parameter(s) as a string

    Returns:
        string: The output of collectors.v1.process.start

    """
    return "Placeholder"

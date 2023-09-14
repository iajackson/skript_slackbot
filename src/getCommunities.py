"""
getCommunities Action Module

Calls the nats subject organisations.v1.query with the provided params

Functions:
    1. parse_output(data): Parses the response from nats into the desired format
    2. run(input): Calls the nats subject organisations.v1.query with the provided params

Author: Ian Jackson
"""

import os
import nats
import nats.errors
import json


def parse_output(data):
    """
    Parses the response from nats into the desired format

    Parameters:
        data (string): The raw response from nats

    Returns:
        string: The formatted response

    """
    try:
        map_vars = lambda element: {"Key": element["id"], "Name": element["name"]}
        parsed_data = json.loads(data)
        data_list = parsed_data["data"]
        mapped = map(map_vars, data_list)
        return json.dumps(list(mapped), indent=2)
    except Exception as e:
        return "Error parsing nats response"


async def run(params):
    """
    Calls the nats subject organisations.v1.query with the provided params

    Parameters:
        input (string): The function parameter(s) as a string

    Returns:
        string: The output of nats organisations.v1.query

    """
    # Connect to nats server
    nats_url = os.environ.get("NATS_URL", "nats://nats:4222").split(",")
    try:
        nc = await nats.connect(servers=nats_url)
    except Exception as e:
        print(e)
        return "Failed to connect to NATS server"

    # Make call against nats server
    try:
        res = await nc.request("organisations.v1.query", b"{}", timeout=10)
        await nc.close()
    except Exception as e:
        return "Error making nats request"

    # Assemble and return response
    res_data = res.data.decode("utf-8")
    parsed_output = parse_output(res_data)
    return parsed_output

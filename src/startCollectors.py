"""
startCollectors Action Module

Calls the nats subject collectors.v1.process.start with the provided params

Functions:
    1. parse_output(data): Parses the response from nats into the desired format
    2. format_payload(params): Formats the provided params into the desired payload
    3. run(input): Calls the nats subject collectors.v1.process.start with the provided params

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
        parsed_data = json.loads(data)
        if parsed_data["status"] == "OK":
            jobStartStat = parsed_data["jobStartStat"]
            started = jobStartStat["customers.v2.collector.start"]["succeeded"]
            return "The collector job started successfully with {} consents".format(
                started
            )
        else:
            return "The collector job started failed to start"
    except Exception as e:
        return "Error parsing nats response"


def format_payload(params):
    """
    Formats the provided params into the desired payload for the nats call

    Parameters:
        params (string): The function parameter(s) as a string

    Returns:
        string: The formatted payload ready to be passed to nats

    """
    consent_ids = [id.strip() for id in params.split(",")]
    payload = {
        "jobType": "INCREMENTAL",
        "consentIds": consent_ids,
    }
    return json.dumps(payload)


async def run(params):
    """
    Calls the nats subject collectors.v1.process.start with the provided params

    Parameters:
        input (string): The function parameter(s) as a string

    Returns:
        string: The output of nats collectors.v1.process.start

    """
    # Connect to nats server
    nats_url = os.environ.get("NATS_URL", "nats://nats:4222").split(",")
    try:
        nc = await nats.connect(servers=nats_url)
    except Exception as e:
        print(e)
        return "Failed to connect to NATS server"

    # Format payload
    payload = format_payload(params)

    # Make call against nats server
    try:
        res = await nc.request(
            "collectors.v1.process.start", bytes(payload, encoding="utf-8"), timeout=10
        )
        await nc.close()
    except Exception as e:
        return "Error making nats request"

    # Assemble and return response
    res_data = res.data.decode("utf-8")
    parsed_output = parse_output(res_data)
    return parsed_output

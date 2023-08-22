"""
getDCR Action Module

Calls the nats subject organisations.v1.query with the provided params

Functions:
    1. run(input): Calls the nats subject organisations.v1.query with the provided params

Author: Ian Jackson
"""

"""
Function name: getDCR
Function parameter: ae94b39d-6f30-eb11-a81d-000d3a884a20

The NATs message that this would get translated into -
NATS Subject: 'organisations.v1.query'
JSON Data: 'nats req 'registrations.v1.get' '{"dataHolderId":"ae94b39d-6f30-eb11-a81d-000d3a884a20", "softwareProductId": "2e982fd6-91eb-ec11-a82f-000d3a8830d6"}' -H 'baggage: debug=true' 
The NATS message we would receive back from our micro service is
{ /* some big json */ }
"""


def run(params):
    """
    Calls the nats subject organisations.v1.query with the provided params

    Parameters:
        input (string): The function parameter(s) as a string

    Returns:
        string: The output of organisations.v1.query

    """
    return "Placeholder"

"""
getCommunities Action Module

Calls the nats subject organisations.v1.query with the provided params

Functions:
    1. run(input): Calls the nats subject organisations.v1.query with the provided params

Author: Ian Jackson
"""

"""
Function name: getCommunities
Function parameter: none

The NATs message that this would get translated into -
NATS Subject: 'organisations.v1.query'
JSON Data: '{}'
The NATS message we would receive back from our micro service is
{"status":"OK","data":[{"id":"0d86b4a7-1592-4967-8335-3f0ae6fb1a3b","name":"Customer 1","branding":{"logoLocation":{"key":"0d86b4a7-1592-4967-8335-3f0ae6fb1a3b/customer1.jpg","bucket":"transkript-prod-files","region":"ap-southeast-2"}},"softwareProductId":"2e982fd6-91eb-ec11-a82f-000d3a8830d6","createdDate":"2023-08-02T03:54:21.367389Z","modifiedDate":"2023-08-02T03:58:33.097134Z"},{"id":"125420d4-f84f-4c6a-8425-b0331a75d0df","name":"Customer 2","branding":{"logoLocation":{"key":"125420d4-f84f-4c6a-8425-b0331a75d0df/BDJ.jpg","bucket":"skript-prod-org-files","region":"ap-southeast-2"}},"softwareProductId":"2e982fd6-91eb-ec11-a82f-000d3a8830d6","createdDate":"2023-08-03T05:13:44.40808Z","modifiedDate":"2023-08-03T05:22:32.039394Z"},{"id":"1704c99a-81f6-4a5f-ac26-b586afbe9c80","name":"Customer 3","branding":{"brokerName":"New Quantum","orgPurpose":"validating account access and data retrieval","logoLocation":{"key":"nq-logo.png","bucket":"organisation-assets","region":"ap-southeast-2"},"orgIconLocation":{"key":"skript-dev-icon.png","bucket":"organisation-assets","region":"ap-southeast-2"},"brokerContactName":"Skript","broke ...........
"""


def run(params):
    """
    Calls the nats subject organisations.v1.query with the provided params

    Parameters:
        input (string): The function parameter(s) as a string

    Returns:
        string: The output of nats organisations.v1.query

    """
    return "Placeholder"

"""
Slackbot Module

Talks to slack. Passes messages to interpreter Returns responses to slack

Functions:
    1. message(payload): The slack api message event handler

Author: Ian Jackson, Michael Vlatko
"""

import os
import slack
from flask import Flask
from slackeventsapi import SlackEventAdapter
from slack.errors import SlackApiError

import interpreter

# authenticates app
SLACK_TOKEN = os.environ["SLACK_TOKEN"]
# used to verify slack events
SIGNING_SECRET = os.environ["SIGNING_SECRET"]
# flask port
PORT = os.environ["PORT"]


app = Flask(__name__)
slack_event_adapter = SlackEventAdapter(SIGNING_SECRET, "/slack/events", app)

client = slack.WebClient(token=SLACK_TOKEN)

awaiting_confirmation = {}
default_response = "Please confirm with 'yes' or 'no' only\n"

@slack_event_adapter.on("message")
def message(payload):
    """
    The slack api message event handler

    Parameters:
        message (payload): The slack event payload
    """
    event = payload.get("event", {})
    channel_id = event.get("channel")
    user_id = event.get("user")
    text = event.get("text")
    bot_profile = event.get("bot_profile")

    if user_id in awaiting_confirmation:
        if text == "yes":
            (func, params) = awaiting_confirmation[user_id]
            convert_message = interpreter.tuple_message(func, params)
            response = interpreter.interpret_message(convert_message)
            client.chat_postMessage(channel=channel_id, text=response)
            del awaiting_confirmation[user_id]
            return
        elif text == "no":
            client.chat_postMessage(channel=channel_id, text ="Query cancelled!")
            del awaiting_confirmation[user_id]
            return
        else:
            client.chat_postMessage(channel=channel_id, text=default_response)
            return
    
    if not bot_profile:
        (func, params) = interpreter.parse_message(text)
        confirm = interpreter.tuple_message(func, params)
        client.chat_postMessage(channel=channel_id, text=confirm)
        client.chat_postMessage(channel=channel_id, text=default_response)
        awaiting_confirmation[user_id] = (func, params)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=PORT, debug=True)

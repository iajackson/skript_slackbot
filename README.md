# slackbot_concept

Basic concept for slackbot

Created based off tutorial [here](https://www.pragnakalp.com/create-slack-bot-using-python-tutorial-with-examples/)

## Requirements

[Python3](https://www.python.org/downloads/)

`pip install slackclient flask slackeventsapi`

Needs [ngrok](https://ngrok.com/) for hosting the slackbot locally

Environment variables need to be set for slack access:

- SLACK_TOKEN The slack token authorising access for the bot
- SIGNING_SECRET The signing secret used to verify slack events

## Usage

`python slackbot.py`

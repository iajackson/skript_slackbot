# skript-slackbot

Slackbot designed to automate common admin tasks for Skript

## Running via Docker

### Requirements

[Docker Engine](https://docs.docker.com/engine/install/)

### Usage

`docker compose up`

### Environment variables

- BOT_SLACK_TOKEN - The bot user oauth token
- BOT_SIGNING_SECRET - The bot signing secret
- BOT_PORT - The port the bot will run on
- BOT_NATS_URL - The url of the nats server i.e. nats://host.docker.internal:4222

## Running Directly

### Requirements

[Python3](https://www.python.org/downloads/)

`pip install slackclient flask slackeventsapi nltk nats-py`

Needs [ngrok](https://ngrok.com/) for hosting the slackbot locally

### Usage

`python slackbot.py`

### Environment variables

- SLACK_TOKEN The slack token authorising access for the bot
- SIGNING_SECRET The signing secret used to verify slack events
- PORT The port the bot will run on
- NATS_URL - The url of the nats server i.e. nats://127.0.0.1:4222

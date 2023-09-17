import slack
import ssl
import os
from pathlib import Path
from dotenv import load_dotenv
from flask import Flask
from slackeventsapi import SlackEventAdapter

# print(os.environ)
# exit
env_path = Path('.') / '.env'
load_dotenv(dotenv_path=env_path)

app = Flask(__name__)
slack_event_adapter = SlackEventAdapter(os.environ['SIGNING_SECRET'], '/slack/events', app)

ssl._create_default_https_context = ssl._create_unverified_context

client = slack.WebClient(token=os.environ['SLACK_TOKEN'])
client.chat_postMessage(channel="#chat-bot", text="Hello, world!")


if __name__ == "__main__":
    app.run(debug=True)
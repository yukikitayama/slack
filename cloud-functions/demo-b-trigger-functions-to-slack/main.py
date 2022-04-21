"""
- Set the following environment variables for Cloud Functions
  - SLACK_TOKEN: Bot user OAuth token
"""


import requests
import base64
import json
import os


def send_message_to_slack(channel_name, text):
    headers = {
        'Content-Type': 'application/x-www-form-urlencoded',
        'Authorization': f'Bearer {os.environ["SLACK_TOKEN"]}'
    }
    payload = {
        'channel': channel_name,
        'text': text
    }
    r = requests.post(
        url='https://slack.com/api/chat.postMessage',
        headers=headers,
        params=payload
    )
    print(f'Status code: {r.status_code}')


def main(event, context):
    """
    Two request objects received when the Cloud Functions are invoked by PubSub
    :param event: PubSub message content data
    :param context: PubSub metadata
    :return:
    """

    # Extract PubSub message data
    message = base64.b64decode(event['data']).decode('utf-8')
    message = json.loads(message)
    channel_name = message['channel_name']

    # Sent message to Slack
    text = 'Doing B'
    send_message_to_slack(channel_name=f'#{channel_name}', text=text)

"""
- Set the following environment variables for Cloud Functions
  - PROJECT_ID
  - TOPIC_ID_A
  - TOPIC_ID_B
"""


from flask import jsonify
from google.cloud import pubsub_v1
import os
import json


def publish_message(topic_id, channel_name):
    publisher = pubsub_v1.PublisherClient()
    topic_path = publisher.topic_path(os.environ['PROJECT_ID'], topic_id)
    message = json.dumps({'channel_name': channel_name})
    publisher.publish(topic_path, message.encode('utf-8'))


def main(request):

    # Extract data from Slack
    # channel_name doesn't include prefix #
    channel_name = request.form['channel_name']
    # request.form['text'] contains string after slash command
    text = request.form['text']

    if text == 'a':
        publish_message(topic_id=os.environ['TOPIC_ID_A'], channel_name=channel_name)
    elif text == 'b':
        publish_message(topic_id=os.environ['TOPIC_ID_B'], channel_name=channel_name)
    else:
        text = 'No action given, so not running another Cloud Functions'

    message = {
        'response_type': 'in_channel',
        'text': f'Running {text}'
    }

    # import json; json.dumps(message) doesn't make a message appear nicely in slack
    return jsonify(message)

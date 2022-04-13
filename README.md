# Slack API

How to use Slack API

In the following code, please replace the token and channel name with yours. Please ignore `boto3` Secrets Manager 
section, because it's not related to Slack API. I just don't wanna show my secrets in GitHub.

- [send_message_to_channel.py](https://github.com/yukikitayama/slack/blob/main/send_message_to_channel.py)
  - Send a message to a channel by using Slack API endpoint.
- [demo_slack_sdk.py](https://github.com/yukikitayama/slack/blob/main/demo_slack_sdk.py)
  - Using Slack SDK for Python to send message and upload file to channel.
from slack_sdk import WebClient
import boto3
import json


SECRET_NAME = 'slack'
REGION_NAME = 'us-west-1'
PROFILE_NAME = 'yuki'
CHANNEL = '#webapp'
CSV = './test.csv'


def get_secret(region_name: str, secret_name: str, profile_name: str) -> dict:
    session = boto3.session.Session(profile_name=profile_name)
    client = session.client(service_name="secretsmanager", region_name=region_name)
    secret_value = client.get_secret_value(SecretId=secret_name)
    secret_string = secret_value['SecretString']
    secret = json.loads(secret_string)
    return secret


def main():

    # Get token
    secret = get_secret(
        region_name=REGION_NAME,
        secret_name=SECRET_NAME,
        profile_name=PROFILE_NAME
    )
    token = secret['bot-user-oauth-token']

    # Post message by Slack SDK client
    client = WebClient(token=token)
    text = 'Test for sending a message by Slack SDK'
    response = client.chat_postMessage(channel=CHANNEL, text=text)
    print('Post message response')
    print(response)
    print()

    # Make a CSV file to test uploading files
    content = 'This is a text content for CSV'
    f = open(CSV, 'w')
    f.write(content)
    f.close()

    # Upload CSV file to Slack channel
    message = 'This message is shown together with the uploaded file'
    filename = 'test.csv'
    response = client.files_upload(
        channels=CHANNEL,
        file=CSV,
        filename=filename,
        initial_comment=message
    )
    print('Upload file response')
    print(response)
    print()


if __name__ == '__main__':
    main()

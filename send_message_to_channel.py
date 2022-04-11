import boto3
import requests
import json
import pprint


SECRET_NAME = 'slack'
REGION_NAME = 'us-west-1'
PROFILE_NAME = 'yuki'
CHANNEL = '#webapp'


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

    # Post message to Slack
    headers = {
        'Content-Type': 'application/x-www-form-urlencoded',
        'Authorization': f'Bearer {token}'
    }
    payload = {
        'channel': CHANNEL,
        'text': 'This is a test message.'
    }
    r = requests.post(
        url='https://slack.com/api/chat.postMessage',
        headers=headers,
        params=payload
    )
    print(f'Status code: {r.status_code}')
    print('Response JSON')
    pprint.pprint(r.json())


if __name__ == '__main__':
    main()

import requests
import json
import time
import urllib.parse
from flask import Flask, request

# Set up Telegram bot information
BOT_TOKEN = 'TELEGRAM_BOT_TOKEN'
CHAT_ID = 'TELEGRAM_CHAT_ID'

# Set up Emby information
EMBY_URL = 'http://yourembyserver:8096'
EMBY_API_KEY = 'YOURE_EMBY_API_KEY'

# Set up webhook endpoint
WEBHOOK_ENDPOINT = 'http://127.0.0.1:5000/webhook'

# Set up Flask app
app = Flask(__name__)

# Set up route for webhook
@app.route('/webhook', methods=['POST'])
def webhook():
    process_notifications()
    return 'OK'

# Function to send a message to Telegram
def send_telegram_message(message):
    url = f'https://api.telegram.org/bot{BOT_TOKEN}/sendMessage'
    params = {'chat_id': CHAT_ID, 'text': message}
    response = requests.post(url, params)
    return response.json()

# Function to process Emby notifications and send them to Telegram
def process_notifications():
    url = f'{EMBY_URL}/emby/Notifications?api_key={EMBY_API_KEY}&IsRead=false&Limit=5&SortBy=DateCreated&SortOrder=Descending'
    response = requests.get(url)
    notifications = response.json()['Items']
    for notification in notifications:
        message = f'{notification["Date"]} - {notification["Message"]}'
        send_telegram_message(message)
    time.sleep(60)

# Set up webhook to listen for Emby events
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

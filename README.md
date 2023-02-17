# INSTALL

    git clone https://github.com/raistech/emby-webhook-telegram.git
    cd emby-webhook-telegram
    #don't forget edit your env
    nano bot.py
    
    # Set up Telegram bot information
    BOT_TOKEN = 'TELEGRAM_BOT_TOKEN'
    CHAT_ID = 'TELEGRAM_CHAT_ID'
    # Set up Emby information
    EMBY_URL = 'http://yourembyserver:8096'
    EMBY_API_KEY = 'YOURE_EMBY_API_KEY'
    
    #save youre edit
    python3 bot.py

To use the above code with Nginx, first make sure that Nginx is installed and configured properly. 
The following is an example of a Nginx block server configuration:

    
    server {
    listen 80;
    server_name example.com;
    
    location /webhook
        proxy_pass http://127.0.0.1:5000;
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
    }

The above configuration will forward requests to /webhook to our Flask application running on port 5000 on 127.0.0.1. 
Additionally, additional headers such as Host and X-Real-IP will be included to ensure security and accuracy of requests.

Once Nginx is configured, run the Flask application with the python app.py command. 
Then, create and register your Telegram bot, then change the value of BOT_TOKEN and CHAT_ID in the Python code according to your Telegram bot chat token and ID. 
Finally, change the values ​​of the EMBY_URL and EMBY_API_KEY according to your Emby URL and Emby API key. Now Emby notifications will be forwarded to your Telegram bot via a webhook set up with Nginx.


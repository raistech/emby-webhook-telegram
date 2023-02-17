![Logo](https://cdn.ra-is.tech/raistech.jpeg)

## INSTALL

    
    git clone https://github.com/raistech/emby-webhook-telegram.git
    cd emby-webhook-telegram
    # Don't forget edit your env
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

## Contributing

Pull requests are welcome. For major changes, please open an issue first
to discuss what you would like to change.

Please make sure to update tests as appropriate.

<h2 id="connect-with-me">Connect with me</h2>
<div align="center">
<a href="https://github.com/raistech" target="_blank">
<img src=https://img.shields.io/badge/github-%2324292e.svg?&style=for-the-badge&logo=github&logoColor=white alt=github style="margin-bottom: 5px;" />
</a>
<a href="https://twitter.com/vpsmusicbottk" target="_blank">
<img src=https://img.shields.io/badge/twitter-%2300acee.svg?&style=for-the-badge&logo=twitter&logoColor=white alt=twitter style="margin-bottom: 5px;" />
</a>
<a href="https://instagram.com/sepidolsenowman" target="_blank">
<img src=https://img.shields.io/badge/instagram-%23000000.svg?&style=for-the-badge&logo=instagram&logoColor=white alt=instagram style="margin-bottom: 5px;" />
</a>
</div>

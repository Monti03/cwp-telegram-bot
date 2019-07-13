# cwp-telegram-bot
---
You can control changes in web pages and get a notification on telegram through this bot

## Installation

- pip3 install python-telegram-bot
- pip3 install beautifulsoup4
- pip3 install urllib3

## Usage
Follow this [guide](https://core.telegram.org/bots#6-botfather) to create your bot, then put the token in a new file ```token.txt``` in the same folder of ```main.py```

Run the bot code on your pc with ```python3 main.py```  

Then look for the bot you created on telegram and start the conversation.

## Commands
- ```/start``` starts the conversation with the bot
- ``` link``` starts a thread that controls ```link```
- ```/stop link``` stops the control of ```link```
- ```/list``` lists the links you are controlling
- ```/delete_all``` stops the controll of each link
